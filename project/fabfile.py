from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

def push():
    local('git push origin master')

def commit():
    local("git add .")
    commit_message = raw_input("Enter a commit message")
    local("git commit -m '{}'".format(commit_message))

def test():
    with settings(warn_only=True):
        result = local("nosetests -v")
    if result.failed and confirm("Tests failed. Continue?"):
        abort("Aborting.")

def heroku():
    local('git push heroku master')

def deploy():
    commit()
    test()
    push()


