#### Jenkins

* Run python script inside a container

        docker.image(IMAGE_NAME).inside {
            sh "python script.py ${parameters}"
        }

* Enable Ansicolor in pipeline

        tryStage("SnowflakeImport", {
            ansiColor('xterm') {
                // do something here
                // if there is a dockerized environment here
                // make sure to run docker with -t to set TERM to xterm
            }
        })
