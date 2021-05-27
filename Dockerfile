FROM python:3.8-alpine

RUN pip --default-timeout=1000 install --upgrade pip

RUN pip install pipenv

COPY ./Pipfile ./

COPY ./Pipfile.lock ./

RUN pipenv install --system --deploy

COPY . /api

WORKDIR /api

CMD ["python", "./main.py"]
