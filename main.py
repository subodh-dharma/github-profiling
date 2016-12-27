import os
import json
from github import GitHub

#from agithub import GitHub
git_token = os.environ['GITTOKEN']

#gitapi = GitHub(token=git_token)
#gitapi.users.get();
gitapi = GitHub(access_token=git_token)
# GET /users/:user
user_info = gitapi.users('subodh-dharma').get()

#GET /user/repos
repos = gitapi.users('subodh-dharma').repos().get()
#repos_print = json.loads(repos)
#print json.dumps(repos, indent=4, sort_keys=True)
#print repos[0]['name']

for index in range(len(repos)):
    print repos[index]['name']

for repo in repos:
    print repo['clone_url']
