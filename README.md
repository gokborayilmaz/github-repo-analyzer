# 📊 GitHub Repository Analyzer - Day 17/21

This agent is part of the **Everyday New AI Agent** series - **Day 17/21** 🚀

## 📌 Overview

The **GitHub Repository Analyzer** is an AI-powered tool that retrieves key repository metrics and determines whether a GitHub repository is actively maintained.

### 🔹 Features:

- Fetches repository statistics using **GitHub MCP**:
  - 📅 Last Commit Date
  - ✅ Active Development Status
- ✅ Determines if the repository is actively developed:
  - Checks if the last commit was within the last **7 days**
  - Verifies **issue engagement** (responses to open issues)

---

## 🛠️ Installation & Setup

### **Prerequisites**

- Python 3.9 or higher
- Git
- Virtual environment (recommended)
- **GitHub Personal Access Token** (for MCP authentication)

### **Installation**

1️⃣ Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Set up your environment variables:
Create a `.env` file in the root directory and configure it as follows:

```env
GITHUB_PERSONAL_ACCESS_TOKEN="your_github_token"
AZURE_OPENAI_ENDPOINT="your_azure_openai_endpoint"
AZURE_OPENAI_API_VERSION="your_azure_openai_api_version"
AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
```

---

## 🚀 Running the Application

Start the FastAPI server:

```bash
uvicorn upsonicai:app --reload
```

Open the UI in your browser:

```
http://127.0.0.1:8000/
```

---

## 🔗 API Endpoints

### **1️⃣ Analyze a GitHub Repository**

- **Endpoint:** `GET /analyze_repo`
- **Query Parameter:** `repo` (GitHub repository in `owner/repo` format)
- **Example Usage:**

```bash
curl "http://127.0.0.1:8000/analyze_repo?repo=torvalds/linux"
```

- **Response:**

```json
{
  "repository": "torvalds/linux",
  "stats": {
    "last_commit_date": "2024-02-10",
    "active_development": true
  }
}
```

---

## 🏆 Why Use This Agent?

✅ No scraping, uses **GitHub MCP** for stable access.
✅ Easily determine if a repository is **actively maintained**.
✅ Quick & simple FastAPI interface with a **modern UI**.
✅ Built with **Upsonic Framework** for seamless AI-powered automation.

---

🔗 **Explore More:** [GitHub Repository](https://github.com/your-repo-url)

🚀 **UpsonicAI - Making AI Agents Simple & Scalable!**

