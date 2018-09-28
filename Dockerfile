FROM ubuntu:latest
MAINTAINER Rajdeep Dua "dua_rajdeep@yahoo.com"
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip build-essential
RUN pip3 install flask
RUN pip3 install SQLAlchemy
RUN pip3 install flask_sqlalchemy
COPY . /app
WORKDIR /app
# RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3.6"]
CMD ["app.py"]