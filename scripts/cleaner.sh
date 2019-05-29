#!/usr/bin/env bash
docker system prune --all --force --volumes && docker container stop $(docker container ls -a -q) && docker system prune -a -f --volumes && docker-compose build
