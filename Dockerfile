FROM jfloff/alpine-python:2.7

ENV MONGO_HOST mongodb
ENV MONGO_DB development

WORKDIR /src
COPY requirements.txt /src/

RUN pip install -r requirements.txt

COPY app.py /src/
COPY app /src/app

CMD python app.py
