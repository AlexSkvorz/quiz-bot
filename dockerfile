FROM python:3.9-slim

RUN pip install pipenv

WORKDIR /quiz_bot

COPY Pipfile Pipfile.lock /quiz_bot/

RUN pipenv install --deploy --system --ignore-pipfile

COPY . /quiz_bot

CMD ["python", "main.py"]