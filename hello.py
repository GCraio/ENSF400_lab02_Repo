from github import Github
import os

# Authenticate (Use a Personal Access Token from environment variable)
token = os.getenv("GIT_TOKEN")
if not token:
    raise ValueError("GIT_TOKEN environment variable not set")
g = Github(token)

# Replace with your GitHub username and repo name
repo = g.get_user().get_repo("ENSF400_lab02_Repo")

# Get all branches
branches = repo.get_branches()


#Random change
# Print branch names
for branch in branches:
    print(branch.name)


# Get all pull requests created by you
pulls = repo.get_pulls(state="all")

# Filter pull requests where the author is you
username = g.get_user().login
your_pulls = [pr for pr in pulls if pr.user.login == username]

# Print PR details
for pr in your_pulls:
    print(f"PR #{pr.number}: {pr.title} (State: {pr.state})")



# Get commits from the main branch
commits = repo.get_commits(sha="main")

# Filter commits made by you
your_commits = [commit for commit in commits if commit.author and commit.author.login == username]

# Print commit details
for commit in your_commits:
    print(f"Commit {commit.sha[:7]}: {commit.commit.message}")
