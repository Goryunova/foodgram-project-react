FROM python:3.8.5

WORKDIR /code
COPY . /code
RUN pip install -r /code/requirements.txt
CMD qunicorn foodgram.wsgi:application --build 0.0.0.0:8000