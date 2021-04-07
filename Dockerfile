# Use official Docker image as base
FROM registry.gitlab.com/fdroid/repomaker:latest
# copy my own settings for additional customizations
WORKDIR /repomaker
COPY settings_docker.py ./repomaker/
