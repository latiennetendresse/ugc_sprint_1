FROM python:3.11

WORKDIR /home

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /home

RUN  apt-get update \
     && apt-get install -y gcc \
     && pip3 install -r /home/requirements.txt


COPY . .

ENTRYPOINT ["python", "main.py"]