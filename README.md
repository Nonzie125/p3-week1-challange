MY WEEK ONE CODE CHALLANGE
This is my week one code challange which has been so difficult for me to finish considering the situation i had but as a developer i had to do something, so this This repository is part of my week 1 challenge for the P3 project. It contains various coding exercises, troubleshooting, and problem-solving steps. Below is a summary of the challenges faced during the project and how I resolved them.
the challanges i encountered are:
  - Git Configuration Issues(
  - SSH Key Authentication Error
  - GitHub Push Error

1. Git Configuration Issues
While attempting to commit, I encountered an error due to missing Git identity details name and email. 
I solved this by configuring Git globally using the following commands:

```bash
git config --global user.email "github@github.com:Nonzie125"
git config --global user.name "Nonzie125"
sign_and_send_pubkey: signing failed for RSA "/home/amali2/.ssh/id_rsa" from agent: agent refused operation
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.
so i Generated a new SSH key,then i added the SSH private key to the agent:
ssh-keygen -t rsa -b 4096 -C "git@github.com:Nonzie125"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
After fixing the SSH issue, I encountered the following error when pushing changes to GitHub and the issue was caused by trying to push to the wrong branch. I resolved it by renaming the local master branch to main, then pushing the changes
After sucessfully doing it i cloned the repository,then navigated to the project folder and run the python script.I later git pushed to my github account

For more information feel fee to reach me via my email: nonzamomwende57@gmail.com
