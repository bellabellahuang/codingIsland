### GIT commands

* Clone the remote repo to local

        git clone [repo url]

* Config user

        git config user.name [name]
        git config user.email [email]

* Config origin and upstream

        git remote add origin [origin url]
        git remote add upstream [upstream url]

* Undo

        git checkout . (undo local changes)
        git reset HEAD~ (undo recent commit)
        git reset (undo git add .)

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

* Using tag

        git tag
        git show [tag]
        git tag -a [tag]
        git tag -a [tag] -m "description"
        git push origin/upstream [tag]
        git push origin/upstream --tags
        git tag -d [tag]
        git push origin :refs/tags/[tag]
        git push --delete origin/upstream [tag]
        git push upstream :[tag] // remove old tag

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
