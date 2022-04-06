FROM python:latest
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
ADD app /app

CMD python /app/main.py
