#!/bin/bash
# -----------------------------------------------------------------------------
# bash script to copy docker-compose.yml and convert it to kubernetes yaml files
# -----------------------------------------------------------------------------
# run script from ./kubernetes as cwd
#
# Attention: install kompose before running (https://github.com/kubernetes/kompose)
GREEN="\033[0;32m"
RED="\033[0;31m"
NC="\033[0m" # No Color

# get arguments
while getopts u: flag
do
    case "${flag}" in
        u) username=${OPTARG};;
    esac
done

# ------------------------------------------------------------------------------
echo "Loging in to Docker hub"
docker login
echo -e "${GREEN}... login to Docker Hub successful${NC}"

# ------------------------------------------------------------------------------
# build docker images from docker-compose.yml
echo "Building docker images ..."
docker-compose build
echo -e "${GREEN}... building images complete${NC}"

# ------------------------------------------------------------------------------
# push images to docker hub, if username is provided
echo "Pushing images to docker hub ..."

if [ -z "$username" ]
then
    echo -e "${RED}... no username provided, skipping push${NC}"
else
    docker tag pibloom-proxy:latest $username/pibloom-proxy:latest
    docker push $username/pibloom-proxy:latest

    docker tag pibloom-web:latest $username/pibloom-web:latest
    docker push $username/pibloom-web:latest

    docker tag pibloom-api:latest $username/pibloom-api:latest
    docker push $username/pibloom-api:latest

    echo -e "${GREEN}... pushing images complete${NC}"
fi

# ------------------------------------------------------------------------------
# copy docker-compose.yml to kubernetes folder
echo "Copying docker-compose.yml to kubernetes ..."
cp ./docker-compose.yml ./kubernetes
echo -e "${GREEN}... copying complete${NC}"

# ------------------------------------------------------------------------------
# update docker-compose.yml to use images from docker hub and update restart policy
echo "Updating docker-compose.yml for kubernetes deployment ..."

cd ./kubernetes
sed "s/unless-stopped/always/g" docker-compose.yml > docker-compose-one.yml
rm docker-compose.yml

if [ -z "$username" ]
then
    mv docker-compose-one.yml docker-compose-k8s.yml
    echo -e "${RED}... no username provided, skipping image name update${NC}"
else
    sed "s/image: /image: $username\//g" docker-compose-one.yml > docker-compose-k8s.yml
    rm docker-compose-one.yml
fi

echo -e "${GREEN}... updating complete${NC}"

# ------------------------------------------------------------------------------
# convert docker-compose.yml to kubernetes yaml files
echo "Converting docker-compose.yml to kubernetes yaml files ..."
kompose convert -f docker-compose-k8s.yml # -o k8s-deploy.yml
rm docker-compose-k8s.yml
echo -e "${GREEN}... converting complete${NC}"

# ------------------------------------------------------------------------------
echo -e "${GREEN}Script complete!${NC}"