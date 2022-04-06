#!/usr/bin/env bash
docker run -d hello-world
ls -la /home/ubuntu
docker run -d -p 8080:8080 -v /home/ubuntu/log:/log abishake98/spartanpy:0.1
