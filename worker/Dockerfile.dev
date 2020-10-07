FROM python:3.7.9-stretch

WORKDIR '/app'

RUN pip3 install redis python-dotenv

COPY . .

CMD ["python3", "worker.py"]
