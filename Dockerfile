FROM python:3.7-slim-buster
MAINTAINER Artur Nebot
RUN apt-get update -y

ENV INSTALL_DIR=/opt/gscrapper

COPY ./requirements.txt $INSTALL_DIR/requirements.txt
COPY manage.py $INSTALL_DIR/
COPY gscrapper/ $INSTALL_DIR/gscrapper
COPY web/ $INSTALL_DIR/web

WORKDIR $INSTALL_DIR
RUN pip3 install -r requirements.txt

EXPOSE 5001
CMD ["python","manage.py","runserver","0.0.0.0:5001"]
