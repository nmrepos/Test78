FROM mcr.microsoft.com/devcontainers/universal:latest

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install mysql-client mysql-server

RUN apt-get update && \
    apt-get install -y chromium-browser chromium-chromedriver

COPY requirements.txt .
RUN pip install -r requirements.txt