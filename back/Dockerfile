FROM python:3.7.3-stretch

RUN mkdir -p /app
WORKDIR /app

RUN pip install --upgrade pip
ADD requirements.txt .
RUN pip install -r requirements.txt

ADD run.py /app/
ADD techtest /app/techtest

CMD ["gunicorn","-w","1","--bind","0.0.0.0:8001","run:app"]