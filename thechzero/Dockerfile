FROM --platform=amd64 python:3.11-buster
ENV PYTHONUNBUFFERED=1 
WORKDIR / thechzero
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:8000

