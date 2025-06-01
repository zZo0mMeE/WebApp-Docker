# syntax=docker/dockerfile:1

FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --prefix=/install -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY src/ .
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV WEATHER_API_KEY=none

EXPOSE 8080
CMD ["flask", "run", "--port=8080"]
