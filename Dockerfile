FROM python:3.6-alpine

COPY app/* .
COPY requirements.txt .

RUN pip install requirements.txt

EXPOSE 8080

ENV DB_BASE_URL localhost:9876

CMD ["python", "main.py"]