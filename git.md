### GIT commands

* Config particular user for the repo

        git config user.name <your_user_name>
        git config user.email <your_email_address>

* Undo local changes

        git checkout .

* Undo the recent commit

        git reset HEAD~

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
