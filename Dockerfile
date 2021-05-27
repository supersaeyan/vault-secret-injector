FROM python:3.8-alpine

RUN pip --default-timeout=1000 install --upgrade pip

RUN pip install pipenv

COPY ./requirements.txt /api/requirements.txt

RUN pipenv install -r /api/requirements.txt

COPY . /api

WORKDIR /api

CMD ["python", "./main.py"]
