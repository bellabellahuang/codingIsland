### DOCKER commands

* [docker run reference](https://docs.docker.com/engine/reference/run/)

* [docker build reference](https://docs.docker.com/engine/reference/builder/)

* Build docker image

        Go to the directory of the Dockerfile
        docker build -t [image-name] .

* Build docker image with tags

        docker build -t [image-name]:[tag] .

* Push an image to Docker Hub

        docker push [image-name]

* List all the running containers

        docker ps

* List all containers including stopped ones

        docker ps -a

* List containers ids only

        docker ps -q

* Stop running a container

        docker stop [container-id]

* Restart a container

        docker start [container-id]

* Remove all stopped containers

        docker container prune

* Remove a contrainer by id

        docker container rm [container-id]

* List all the local images

        docker images

* List images ids only

        docker images -q

* Remove a local image by id

        docker image rm [image-id]

* Force to delete an image

        docker image rm -f [image-id]

* To access MySQL running locally from docker container

        docker run --rm -it --network=host mysql mysql -h 127.0.0.1 -uroot -p

* Bind mount a volume from local storage with container storage

        docker run -v [local-path]:[container-path]

* Pull an image from Docker Hub

        docker pull [image-name]

* Install mysql-client on Debian

        In the Dockerfile
        FROM debian
        RUN apt-get update && apt-get install -y default-mysql-client && rm -rf /var/lib/apt

* Run script(s) using image

        ENTRYPOINT [ "python", "/app/exporter.py" ] - accept parameters passing to the script
        CMD [ "python", "/app/exporter.py" ] - the command to run exactly