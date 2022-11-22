FROM python:3.9

RUN mkdir /code
WORKDIR /code

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY test_stripe ./code
WORKDIR /code/

EXPOSE 8000