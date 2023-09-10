FROM ubuntu:18

ENV TZ=Europe/Rome
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update
#RUN apt install -y tzdata


RUN apt-get update && apt-get upgrade && apt-get install -y \
    python3.8\
    tesseract-ocr \
    tesseract-ocr-ita \
    python3-opencv \
    python3-pip 

RUN mkdir -p /workspace
WORKDIR /workspace
COPY . /workspace
COPY . /requirements.txt



RUN pip3 install -r requirements.txt





