from github import Github
from creds import GithubCreds

ghc = GithubCreds()
g = Github(ghc.get_access_token())

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)