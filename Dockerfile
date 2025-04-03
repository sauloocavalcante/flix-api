FROM python:3.10.12-slim

WORKDIR /notify

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . . 

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8001

CMD sh -c "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8001"
