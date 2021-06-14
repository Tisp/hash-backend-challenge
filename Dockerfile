FROM python:3.9

WORKDIR /app

COPY . /app

ENV FLASK_RUN_PORT 9091

RUN pip install setuptools==49.6.0  \
    && pip3 install -r requirements.txt \
    && rm -rf /var/cache/apk/*

CMD [ "python", "-m", "flask", "run", "-h", "0.0.0.0" ]