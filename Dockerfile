# Use official Docker image as base
FROM registry.gitlab.com/fdroid/repomaker:latest
# copy my own settings for additional customizations
WORKDIR /repomaker
COPY settings_docker.py ./repomaker/
# make database and media folder writable for our user
RUN chown www-data /repomaker/data/db.sqlite3
RUN chown www-data /repomaker/data/media
