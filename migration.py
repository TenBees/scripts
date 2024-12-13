import os
import subprocess
 
repos = ["", ""]
codecommit_url = ""
github_url = ""
 
def execute(command):
    try:
        result = subprocess.run(command , check=True , shell=True, text=True, capture_output=True)
        print(result.stdout)
 
    except subprocess.CalledProcessError as e:
        print( F"error while running command: {command}. Error: {e}")
        exit(1)
 
for repo in repos:
    repoNames = repo.split(":")
    print(f"Starting migration of repo: {repoNames[0]}")
 
    clone = f"git clone --mirror {codecommit_url}{repoNames[0]}"
    execute(clone)
    print("Cloned")
 
    repo_dir = f"{repoNames[0]}.git"
 
    os.chdir(repo_dir)
    print("changing directory")
 
    set_remote = f"git remote set-url origin {github_url}{repoNames[1]}.git"
    execute(set_remote)
    print(f"Set remote to {github_url}{repoNames[1]}")
 
    push = f"git push --mirror"
    execute(push)
    print(f"Pushed to new remote")
 
    os.chdir("..")
 
    print(f"miration for {repoNames[0]} complete")
 
print("all migrations complete")
