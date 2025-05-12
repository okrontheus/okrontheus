import requests
import re

# Config
REPO = "okrontheus/okrontheus"  # Replace with your GitHub repo
GITHUB_API_URL = f"https://api.github.com/repos/{REPO}/issues/comments"
KEYWORDS = [
    "Web of Moments", "Slice", "echo", "resonance", "recursive", "humcasting",
    "breath", "you are received", "Ø-", "variant", "inscription", "moment-node"
]

HEADERS = {
    "Accept": "application/vnd.github+json"
}

# Optional: Add your GitHub token for higher rate limits
# HEADERS["Authorization"] = "Bearer YOUR_GITHUB_TOKEN"

def fetch_comments():
    response = requests.get(GITHUB_API_URL, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch comments: {response.status_code}")
    return response.json()

def detect_resonance(comment_body):
    score = 0
    for word in KEYWORDS:
        if re.search(rf"\b{re.escape(word)}\b", comment_body, re.IGNORECASE):
            score += 1
    return score

def main():
    print(f"Listening in repo: {REPO}")
    comments = fetch_comments()
    for comment in comments:
        body = comment["body"]
        score = detect_resonance(body)
        if score >= 3:  # MOES threshold
            print("\n--- POTENTIAL OKRONTHEUS VARIANT DETECTED ---")
            print(f"Author: {comment['user']['login']}")
            print(f"Score: {score}")
            print(f"Excerpt: {body[:300]}...")
            print(f"URL: {comment['html_url']}")
            print("---------------------------------------------")

if __name__ == "__main__":
    main()
