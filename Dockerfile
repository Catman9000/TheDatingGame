FROM python:3.9
WORKDIR /app
COPY . .
RUN pip freeze > requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]

