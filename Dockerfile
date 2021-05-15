FROM python:3.8
USER root

RUN apt-get update
RUN apt-get install -y sudo
RUN apt-get install -y wget
RUN apt-get install -y python3-dev libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev

RUN pip install -U pip
RUN pip install -U setuptools
RUN pip install scrapy
RUN pip install scrapy-splash

# mysqlclient
RUN apt-get install -y libssl-dev
RUN sudo apt-get install -y python3-dev libmariadb-dev
RUN pip install mysqlclient
RUN pip install PyMySQL