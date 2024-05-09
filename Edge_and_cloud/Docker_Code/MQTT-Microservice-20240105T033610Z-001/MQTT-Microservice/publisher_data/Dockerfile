FROM python:3.11
LABEL developer="diot-sept-2023"
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt
COPY mqtt_publish.py /usr/src/app
