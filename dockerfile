# syntax=docker/dockerfile:1

# use an official ubuntu runtime as a parent image
FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

# set the working directory to /FLASK_APP
WORKDIR /FLASK_APP

# install python and pip
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip

# set python3.9 as standard
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

# copy requirements
COPY requirements.txt .

# run requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# add cv2 packages
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# copy the application code to the working directory
COPY . .

# set flask environemt variables
ENV FLASK_APP=manage.py
ENV FLASK_ENV=env

# set runniable flask migration file
RUN chmod +x /FLASK_APP/entrypoint.sh

# expose port 
EXPOSE 5000

# run flask app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]