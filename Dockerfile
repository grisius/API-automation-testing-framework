FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1
ENV ALLURE_VERSION=2.43.0

WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace/
RUN pip3 install --no-cache-dir -r requirements.txt

RUN apk update && apk add --no-cache \
    openjdk11-jre-headless \
    bash \
    curl \
    tar \
    && curl -o allure-${ALLURE_VERSION}.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VERSION}/allure-commandline-${ALLURE_VERSION}.tgz \
    && tar -zxvf allure-${ALLURE_VERSION}.tgz -C /opt/ \
    && ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/bin/allure \
    && rm allure-${ALLURE_VERSION}.tgz \
    && apk del curl tar \
    && rm -rf /var/cache/apk/*

COPY . /usr/workspace