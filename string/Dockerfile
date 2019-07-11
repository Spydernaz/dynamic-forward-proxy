FROM python:latest

RUN apt update


EXPOSE 80 5000

COPY package /application

RUN pip install -r /application/requirements.txt

WORKDIR /application

ENTRYPOINT [ "python", "app.py"]