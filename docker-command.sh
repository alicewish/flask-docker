#!/bin/bash
cd GitHub/flask-docker
docker build -t="alicewish/flask:arm64-20200229" .
docker push alicewish/flask:arm64-20200229

docker build -t="alicewish/flask:test" .
docker push alicewish/flask:test