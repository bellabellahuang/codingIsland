### SSH Config

* Handling multiple SSH Keys for different hosts

        $ nano ~/.ssh/config

        # first host
        Host github.com
            HostName github.com
            User git
            IdentityFile ~/.ssh/id_rsa_github

        # second host
        Host bitbucket.org
            HostName bitbucket.org
            User git
            IdentityFile ~/.ssh/id_rsa_bitbucket
