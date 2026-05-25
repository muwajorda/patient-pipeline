FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    openjdk-11-jre

RUN pip3 install pandas

WORKDIR /work
