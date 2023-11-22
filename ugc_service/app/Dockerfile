FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/home/src
ENV PYTHONPATH=/home

RUN apt update -y \
    && apt upgrade -y \
    && apt install -y \
    netcat-traditional

WORKDIR /home/src

COPY requirements.txt /home

RUN pip install --upgrade pip \
    && pip install -r /home/requirements.txt

COPY src/ /home/src
COPY entrypoint.sh /home

RUN chmod +x /home/entrypoint.sh

ENTRYPOINT ["/home/entrypoint.sh"]
