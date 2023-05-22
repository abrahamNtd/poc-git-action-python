FROM python:latest

LABEL Maintainer="abraham.morales@globant.com"

RUN apt-get update && apt-get install -y zip unzip && pip3 install paramiko jumpssh

RUN mkdir -p /app/

COPY main.py /app/main.py

RUN chmod +x /app/main.py

CMD ["/app/main.py"]