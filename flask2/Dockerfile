FROM python:latest

COPY requirements.txt /
RUN apt update && pip install -r /requirements.txt

EXPOSE 5000

COPY app.py /
WORKDIR /
ENTRYPOINT [ "python", "app.py"]