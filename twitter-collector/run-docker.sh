#!/usr/bin/env bash

docker run \
   -v $HOME/.aws/credentials:/root/.aws/credentials:ro \
   -e AWS_PROFILE \
   -it --rm --name twitter-collector-app twitter-collector