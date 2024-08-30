FROM python:3.11

WORKDIR /app

COPY ./app /app

RUN pip install -r requirements.txt

expose 5000

CMD gunicorn --workers=5 --bind=0.0.0.0:5000 app:app