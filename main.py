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

# Language LOC aggregation
lang_summary = {}
contributor_list = set()

for index in range(len(repos)):
    repo_name = repos[index]['name']
    forked = repos[index]['fork']
#    if forked == True:
#        print repo_name, 'forked'
#    else:
#        print repo_name, 'original'
    # /repos/:user/:reponame/languages
    languages_json = gitapi.repos(git_user)(repo_name).languages().get()
    lang_names = languages_json.keys()
    for name in range(len(lang_names)):
        l_name = lang_names[name]
        loc = languages_json[lang_names[name]]
        try:
            prev_loc = lang_summary[l_name]
        except KeyError, e:
            prev_loc = 0;
            lang_summary[l_name] = loc

        lang_summary[l_name] = prev_loc + loc
        #print lang_names[name], languages_json[lang_names[name]]

# print lang_summary

for index in range(len(repos)):
    #/repos/:user/:reponame/contributors
    repo_name = repos[index]['name']
    contributors = gitapi.repos(git_user)(repo_name).contributors().get()
    #contributors = contributors.encode('utf8')
    for c in contributors:
        contributor_list.add(c['login'].encode('utf8'))
        #print type(c['login'])
print list(contributor_list)
