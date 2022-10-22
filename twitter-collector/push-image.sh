#!/usr/bin/env bash

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 678376684750.dkr.ecr.us-east-1.amazonaws.com

docker tag twitter-collector:latest 678376684750.dkr.ecr.us-east-1.amazonaws.com/twitter-collector:${1:-latest}

docker push 678376684750.dkr.ecr.us-east-1.amazonaws.com/twitter-collector:${1:-latest}