### GIT commands

* Config particular user for the repo

        git config user.name <your_user_name>
        git config user.email <your_email_address>

* Clone the remote repo to local

        git clone git@github.com:username/repo.git

* Undo local changes

        git checkout .

* Undo the recent commit

        git reset HEAD~

* Undo git add .       

        git reset

* Work with branches

        git branch
        git branch -a (use '-a' to display both local and remote branches)
        git branch -d <branch name> (delete branch if it is already merged)
        git branch -D <branch name> (force to delete the branch)
        git branch <branch name> (create new branch and stay in the current branch)
        git checkout -b <branch name> (create new branch and switch to it)
        git checkout <branch name> (switch to the specific branch)
        git checkout - (switch to the previous branch)
        git checkout -b <local branch name> origin/<remote branch name> (grab the remote branch to local repo)
        git push <remote name> :<branch name> (delete remote branch)

* Go back to the previous commit state

        git reset --hard <hard value from git log>

* Change the default editor to nano

        git config --global core.editor "nano"

* Solution for refusing to merge unrelated histories

        git pull origin master --allow-unrelated-histories

* Config the repo origin

        git remote add origin [personal_repo_url]

* Config the repo upstream

        git remote add upstream [the_project_url_you_fork_from]

* Creating annotated tags

        git tag -a v1.4 -m "my version 1.4"

* Listing tags

        git tag

* Sharing tags

        git push origin v1.4
        git push origin --tags (push all tags)

* Deleting tags

        git tag -d v1.4 (locally)
        git push origin :refs/tags/v1.4 (remotely)

* Fixing merge conflicts in different branches         

        in the current branch pull the updates from the updated branch (updates in this branch have been merged into master)       
        `git pull origin <updated branch>`
        fix the conflicts locally, commit it and push it to the remote current branch      
        create a new pr from the current branch to master     
