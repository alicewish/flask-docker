# 基础镜像
FROM python:3.7

MAINTAINER alicewish "anywaywillgo@gmail.com"

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi

RUN pip install uWSGI requests redis

RUN pip install Flask
RUN pip install Flask-Bootstrap Flask-HTTPAuth Flask-Login \
                Flask-Mail Flask-Migrate Flask-Moment \
                Flask-PageDown Flask-SQLAlchemy Flask-WTF

RUN pip install html2text beautifulsoup4

RUN pip install jieba

#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt

#COPY requirements-common.txt requirements-common.txt
#RUN pip install -r requirements-common.txt
#
#COPY requirements-web.txt requirements-web.txt
#RUN pip install -r requirements-web.txt
#
#COPY requirements-science.txt requirements-science.txt
#RUN pip install -r requirements-science.txt

WORKDIR /app
#COPY app /app
#COPY cmd.sh /

EXPOSE 9090 9191
USER uwsgi

#CMD ["/cmd.sh"]