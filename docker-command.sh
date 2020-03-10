#!/bin/bash
cd GitHub/flask-docker

docker build -t="alicewish/flask" .
docker push alicewish/flask

docker build -t="alicewish/flask:arm64" .
docker push alicewish/flask:arm64

docker build -t="alicewish/flask:test" .
docker push alicewish/flask:test

docker build -t="alicewish/php-nginx" .
docker push alicewish/php-nginx





docker build -t="alicewish/grav:arm64" .
docker push alicewish/grav:arm64

docker build -t="alicewish/grav-php:arm64" .
docker push alicewish/grav-php:arm64

docker build -t="alicewish/php-nginx:arm64" .
docker push alicewish/php-nginx:arm64

docker build -t="alicewish/php-apache:arm64" .
docker push alicewish/php-apache:arm64