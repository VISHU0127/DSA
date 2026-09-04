import os
import requests
import json

# Fetch credentials from GitHub Secrets
LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION")
CSRF_TOKEN = os.environ.get("LEETCODE_CSRF_TOKEN")

if not LEETCODE_SESSION or not CSRF_TOKEN:
    print("Missing LeetCode credentials.")
    exit(1)

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRF_TOKEN}",
    "X-CSRFToken": CSRF_TOKEN,
    "Referer": "https://leetcode.com"
}

# 1. Fetch your recent accepted submissions
submissions_query = {
    "query": """
    query recentSubmissions($username: String!, $limit: Int!) {
        recentACSubmissions(username: $username, limit: $limit) {
            titleSlug
            title
            lang
        }
    }
    """,
    "variables": {"username": "BEABADOOBEEDO", "limit": 20}  # Change limit as preferred
}

# 2. GraphQL Query helper to get topics and raw code
def get_problem_details(title_slug):
    query = {
        "query": """
        query questionData($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                topicTags { name }
                codeSnippets { lang langSlug code }
            }
        }
        """,
        "variables": {"titleSlug": title_slug}
    }
    res = requests.post("https://leetcode.com", json=query, headers=headers).json()
    return res.get("data", {}).get("question", {})

response = requests.post("https://leetcode.com", json=submissions_query, headers=headers)
submissions = response.json().get("data", {}).get("recentACSubmissions", [])

ext_mapping = {"python3": "py", "python": "py", "cpp": "cpp", "java": "java", "javascript": "js", "typescript": "ts"}

for sub in submissions:
    slug = sub["titleSlug"]
    title = sub["title"]
    lang = sub["lang"]
    
    details = get_problem_details(slug)
    topics = [t["name"] for t in details.get("topicTags", [])]
    
    # Select primary topic (defaulting to "General" if none exists)
    primary_topic = topics[0] if topics else "General"
    
    # Create the directory path grouped by topics
    dir_path = f"Topics/{primary_topic}/{title.replace(' ', '_')}"
    os.makedirs(dir_path, exist_ok=True)
    
    # File naming config
    ext = ext_mapping.get(lang, "txt")
    file_path = f"{dir_path}/solution.{ext}"
    
    # Ideally fetch submission raw code here or save placeholder/snippet
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(f"# Solution for {title}\n# Language: {lang}\n# Topics: {', '.join(topics)}\n")
        print(f"Synced: {title} inside {primary_topic}")
