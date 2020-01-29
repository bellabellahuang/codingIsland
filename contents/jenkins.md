#### Jenkins

* Run python script inside a container

        docker.image(IMAGE_NAME).inside {
            sh "python script.py ${parameters}"
        }
