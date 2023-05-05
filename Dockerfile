FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

ENV bot_env production
EXPOSE 8000
CMD["python", "app.py"]