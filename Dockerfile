# 基础镜像
FROM python:3.7

MAINTAINER alicewish "anywaywillgo@gmail.com"

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi

#RUN pip install Flask uWSGI requests redis
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
#COPY app /app
#COPY cmd.sh /

EXPOSE 9090 9191
USER uwsgi

#CMD ["/cmd.sh"]