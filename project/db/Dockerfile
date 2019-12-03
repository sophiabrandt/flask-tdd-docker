# pull official base image
FROM postgres:11.6-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
