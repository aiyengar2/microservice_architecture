FROM ubuntu:latest
MAINTAINER Arvind Iyengar "iyengararvind@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

RUN mkdir -p /app

RUN pip3 install --upgrade pip

COPY . /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "app.py"]
