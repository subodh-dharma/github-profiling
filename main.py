import os
import sys
import json
from github import GitHub

#git_user='subodh-dharma'
#from agithub import GitHub
git_token = os.environ['GITTOKEN']
gitapi = GitHub(access_token=git_token)
# REF: http://stackoverflow.com/questions/230751/how-to-flush-output-of-python-print
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
git_user = raw_input("Enter Git User Name: ")
# GET /users/:user
user_info = gitapi.users(git_user).get()

#GET /users/:user/repos
repos = gitapi.users(git_user).repos().get()
#repos_print = json.loads(repos)
#print json.dumps(repos, indent=4, sort_keys=True)
#print repos[0]['name']

for index in range(len(repos)):
    print repos[index]['name']

for repo in repos:
    print repo['clone_url']
