FROM python:latest

RUN apt update

EXPOSE 80

COPY package /application

RUN pip3 install -r /application/requirements.txt

WORKDIR /application

ENTRYPOINT [ "python", "app.py"]