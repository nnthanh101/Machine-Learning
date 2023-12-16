ARG DEBIAN_FRONTEND=noninteractive
ARG VARIANT="jammy"
FROM mcr.microsoft.com/devcontainers/base:${VARIANT}

LABEL maintainer="nnthanh101@gmail.com"
LABEL version="1.0.1"

ENV LANG=C.UTF-8
ENV TZ=Pacific/Auckland
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# ARG USERNAME=vscode
# ARG USER_UID=1000
# ARG USER_GID=$USER_UID

## Minimal Ubuntu https://wiki.ubuntu.com/Minimal
RUN apt-get update && yes | unminimize
# RUN update-ca-certificates

## Install OS packages
RUN apt-get update -qq &&     \
    apt-get install -y --no-install-recommends \
      imagemagick             \
      postgresql-client       \
      libsqlite3-dev          \
      graphviz                \
      s3cmd                   \
      openjdk-11-jre-headless \
    && rm -rf /var/lib/apt/lists/*             \
    && apt-get clean

RUN wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip \
  && unzip ngrok-stable-linux-amd64.zip \
  && mv ngrok /usr/local/bin \
  && rm ngrok-stable-linux-amd64.zip

RUN echo "$(ngrok --version)"

COPY install-dependencies.sh /usr/local/bin/install-dependencies
RUN chmod +x /usr/local/bin/install-dependencies
RUN echo "./install-dependencies ..."

# RUN groupadd $USERNAME \
#     && usermod -g $USER_GID -a -G users $USERNAME
# USER vscode

# ENV HOME /root
# WORKDIR /root/