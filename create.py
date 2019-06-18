from github import Github
import os
# url 
api= '7069f1cecdd55e9bdafa9af93bd9b03287c16dce'


title = input("Name your repo: ")
private = input("Is your Repo private T or F?: ")
g = Github(api)

u = g.get_user()
def create(title, private): 
    if private == "t":
        repo = u.create_repo(title, private=True)
        print('Private repo %s created.' % title)
    else:
        repo = u.create_repo(title, private=False)
        print('Public repo %s created.' % title)
create(title, private)


