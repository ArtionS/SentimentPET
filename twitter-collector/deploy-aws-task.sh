#!/usr/bin/env bash

aws ecs create-service \
    --service-name petmedic-twitter-collector \
    --cluster petmedic-prod \
    --task-definition tweeter-collector \
    --launch-type fargate \
    --desired-count 1 \

