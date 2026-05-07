FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
