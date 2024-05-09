FROM ubuntu:20.04

LABEL "developer"="diot:2023"

RUN apt update -y && apt install mosquitto -y

CMD ["/usr/sbin/mosquitto"]

EXPOSE 1883
