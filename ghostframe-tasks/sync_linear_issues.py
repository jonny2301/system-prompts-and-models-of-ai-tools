"""Stub script to sync GitHub issues to Linear.

Requires LINEAR_API_KEY environment variable and optionally GITHUB_TOKEN.
"""
import os
import requests

LINEAR_API_URL = "https://api.linear.app/graphql"


def create_linear_issue(title: str, description: str) -> None:
    token = os.environ.get("LINEAR_API_KEY")
    if not token:
        raise RuntimeError("LINEAR_API_KEY not set")
    headers = {"Authorization": token, "Content-Type": "application/json"}
    query = {
        "query": "mutation IssueCreate($input: IssueCreateInput!) { issueCreate(input: $input) { success } }",
        "variables": {"input": {"title": title, "description": description}}
    }
    response = requests.post(LINEAR_API_URL, json=query, headers=headers)
    if response.status_code != 200:
        raise RuntimeError(f"Linear API error: {response.text}")


# Placeholder: fetch repo issues and call create_linear_issue for each.
# Actual implementation would use the GitHub API.

def main() -> None:
    print("Stub for syncing issues. Implement GitHub issue retrieval and mapping to Linear here.")


if __name__ == "__main__":
    main()
