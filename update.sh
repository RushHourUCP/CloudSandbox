# The argument is the docker_id of the previous version 
# (aka. the current container running - use 'docker ps')
docker stop $1
docker rm $1
docker rmi flask_container
docker build -t flask_container:latest .
docker run -d -p 5000:5000 flask_container:latest