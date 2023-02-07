import requests
import openai

# OpenAI API key
openai.api_key = "your-openai-api-key"

# Base URL for Bitbucket API
BITBUCKET_API_BASE_URL = "https://api.bitbucket.org/2.0"

# Pull request details
repo_owner = "my-repo-owner"
repo_slug = "my-repo-slug"
pull_request_id = "123"

# API endpoint to get pull request details
pull_request_endpoint = f"{BITBUCKET_API_BASE_URL}/repositories/{repo_owner}/{repo_slug}/pullrequests/{pull_request_id}"

# Get pull request details
response = requests.get(pull_request_endpoint)
pull_request = response.json()

# Get list of changes in the pull request
changes = pull_request["changes"]

# Generate a summary of changes
change_summary = []
for change in changes:
    file_path = change["new"]["path"]["to_string"]
    change_type = change["type"]
    change_summary.append(f"{change_type}: {file_path}")

# Generate a summary of the code changes using OpenAI's GPT-3
model_engine = "text-davinci-002"
change_summary_text = "\n".join(change_summary)
prompt = f"Generate a summary for these code changes:\n{change_summary_text}"

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

code_changes_summary = completions.choices[0].text
print(code_changes_summary)
