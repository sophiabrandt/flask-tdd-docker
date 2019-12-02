# base image
FROM python:3.8.0-slim-buster

# install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add and install requirements
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# add user
RUN addgroup --system user && adduser --system --no-create-home --group user
RUN chown -R user:user /usr/src/app && chmod -R 755 /usr/src/app
USER user

# run server
CMD python manage.py run -h 0.0.0.0
