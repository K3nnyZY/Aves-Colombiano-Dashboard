FROM python:3.9

WORKDIR /app

COPY ./src/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app

EXPOSE 8050

CMD ["python", "app.py"]
