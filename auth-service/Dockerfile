FROM python:3.10-buster

WORKDIR /opt/auth-service

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD /bin/sh -c ./start.sh
