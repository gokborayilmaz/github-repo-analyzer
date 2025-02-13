import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, JSONResponse
from dotenv import load_dotenv
from upsonic import Agent, Task, ObjectResponse

# Load environment variables
load_dotenv()

app = FastAPI(title="GitHub Repository Analyzer")

# Initialize the AI agent
github_agent = Agent("GitHub Repo Analyzer", model="azure/gpt-4o", reflection=True)

# Define GitHub MCP
class GitHubMCP:
    command = "npx"
    args = ["-y", "@modelcontextprotocol/server-github"]
    env = {"GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")}

# Define response format for repository analysis
class RepoStats(ObjectResponse):
    last_commit_date: str
    active_development: bool

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GitHub Repo Analyzer</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-100 flex justify-center items-center h-screen">
        <div class="bg-white p-8 rounded-lg shadow-lg w-[40rem]">
            <h1 class="text-2xl font-bold text-center mb-4">📊 GitHub Repo Analyzer</h1>
            <input id="repo" type="text" placeholder="Enter GitHub repository (owner/repo)" class="w-full p-2 border rounded mb-4">
            <button onclick="analyzeRepo()" class="bg-blue-500 text-white px-4 py-2 rounded w-full">Analyze Repository</button>
            <div id="result" class="mt-4 text-sm text-gray-800 bg-gray-50 p-4 rounded overflow-y-auto h-64"></div>
        </div>
        <script>
            async function analyzeRepo() {
                const repo = document.getElementById("repo").value;
                if (!repo) {
                    alert("Please enter a GitHub repository in the format owner/repo.");
                    return;
                }
                const response = await fetch(`/analyze_repo?repo=${encodeURIComponent(repo)}`);
                const data = await response.json();
                document.getElementById("result").innerText = JSON.stringify(data, null, 2);
            }
        </script>
    </body>
    </html>
    """

@app.get("/analyze_repo", response_class=JSONResponse)
async def analyze_repo(repo: str = Query(..., title="GitHub Repository (owner/repo)")):
    """Fetches repository statistics using GitHub MCP."""
    try:
        repo_task = Task(
            f"Retrieve repository statistics for {repo}, including the latest commit date and determine if the repository is actively developed (last commit within a week and active issue responses).",
            tools=[GitHubMCP],
            response_format=RepoStats
        )
        github_agent.do(repo_task)
        repo_stats = repo_task.response if repo_task.response else {}
        return {"repository": repo, "stats": repo_stats}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
