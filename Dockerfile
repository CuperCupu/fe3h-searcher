FROM python:3.7.4-alpine3.10 AS BUILD

RUN apk add g++

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN rm requirements.txt

FROM python:3.7.4-alpine3.10

COPY --from=BUILD /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/
COPY --from=BUILD /usr/local/bin/gunicorn /usr/local/bin/gunicorn

WORKDIR /app
ADD src/data data
ADD src/server server
ADD data.json data.json

CMD gunicorn server.main:app -b 0.0.0.0:${PORT:-8080}