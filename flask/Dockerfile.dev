FROM python:3.7.9-stretch

WORKDIR '/app'

RUN pip3 install flask redis python-dotenv psycopg2-binary uwsgi

COPY . .

CMD ["uwsgi", "app.ini"]
