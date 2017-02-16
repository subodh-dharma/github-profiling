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

lang_summary = {}
for index in range(len(repos)):
    repo_name = repos[index]['name']
    print repo_name
    # /repos/:user/:reponame/languages
    languages_json = gitapi.repos(git_user)(repo_name).languages().get()
    lang_names = languages_json.keys()
    for name in range(len(lang_names)):
        print languages_json[lang_names[name]]
