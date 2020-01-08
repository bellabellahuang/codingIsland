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

* Checkout to a remote branch

        git fetch
        git checkout -t origin/<branch name>

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

        git tag -a [tag] -m "description"

* Listing tags

        git tag

* Listing details of a tag

        git show [tag]

* Sharing tags

        git push origin [tag]
        git push origin --tags (push all tags)

* Creating tags to upstream

        create a pr to merge other branches into master in upstream
        in local origin repo
        git checkout master
        git pull upstream master
        git tag -a [tag]
        git push upstream --tags

* Deleting tags

        git tag -d [tag] (locally)
        git push origin :refs/tags/[tag] (remotely)
        git push --delete origin [tag] (remotely)
        git push --delete upstream [tag] (upstream)

* Fixing merge conflicts in different branches         

        - in the current branch pull the updates from the updated branch (updates in this branch have been merged into master)       
        - git pull origin <updated branch>
        - fix the conflicts locally, commit it and push it to the remote current branch      
        - create a new pr from the current branch to master     

* Keeping a downstream git repo current with upstream repo changes       

        - upstream merged some changes by PRs        
        - in local repo, checkout to the branch that you want to keep updated with the upstream      
        - use the master branch at this example: git checkout master       
        - fetch the new updates from upstream: git fetch upstream
        - merge with the branch you want: git merge upstream/<branch>    
        - push the updates to your own repo: git push origin master            
