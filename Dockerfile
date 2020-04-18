FROM python:3

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y pipenv libtag1-dev libchromaprint-tools ffmpeg

COPY Pipfile* ./
RUN pipenv install

COPY fingerprint.py .

CMD [ "pipenv", "run", "python", "-u", "./fingerprint.py" ]