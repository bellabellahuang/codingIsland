### SSH Config

* Generating new SSH key

        $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

* Starting the ssh-agent in the background

        $ eval "$(ssh-agent -s)"

* Adding the private key to the ssh-agent

        $ ssh-add -K ~/.ssh/[your_private_key]

* Copying the public key to the clipboard

        $ pbcopy < ~/.ssh/[your_public_key]

* Handling multiple SSH Keys for different hosts

        $ nano ~/.ssh/config

        # first host
        Host github.com
            HostName github.com
            User git
            AddKeysToAgent yes
            UseKeychain yes
            IdentityFile ~/.ssh/id_rsa_github

        # second host
        Host bitbucket.org
            HostName bitbucket.org
            User git
            AddKeysToAgent yes
            UseKeychain yes
            IdentityFile ~/.ssh/id_rsa_bitbucket
