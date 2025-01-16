# syntax = docker/dockerfile:1.5
FROM python:3.13.1-slim-bookworm

WORKDIR /usr/src/app

COPY --link requirements.txt /usr/src/app/
RUN --mount=type=cache,target=/root/.cache \
  pip3 install --require-hashes -r requirements.txt

COPY --link . /usr/src/app/

EXPOSE 8001

CMD ["python3", "app.py"]
