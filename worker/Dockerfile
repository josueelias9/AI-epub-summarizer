FROM python:3.11-slim

WORKDIR /josue_app

COPY /worker .
COPY /src /src

RUN pip install -r requirements.txt

CMD ["python", "-m", "app.worker"]
