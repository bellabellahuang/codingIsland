### GIT commands

* Config particular user for the repo

        git config user.name <your_user_name>
        git config user.email <your_email_address>

* Undo local changes

        git checkout .

* Undo the recent commit

        git reset HEAD~

* Work with branches

        git branch
        git branch -a (use '-a' to display both local and remote branches)
        git branch <branch name> (create new branch and stay in the current branch)
        git checkout -b <branch name> (create new branch and switch to it)
        git checkout <branch name> (switch to the specific branch)
        git checkout - (switch to the previous branch)
        git checkout -b <local branch name> origin/<remote branch name> (grab the remote branch to local repo)

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
