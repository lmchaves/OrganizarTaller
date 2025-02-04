FROM alpine:latest

RUN apk add --no-cache \
    make \
    python3


RUN adduser -D -h /home/pruebatest pruebatest

USER pruebatest


RUN mkdir -p /home/pruebatest/.cache && \
    chmod -R a+w /home/pruebatest/.cache && \
    mkdir -p /home/pruebatest/.venv && \
    chmod -R a+w /home/pruebatest/.venv 

ENV PATH="/home/pruebatest/.local/bin:$PATH"

ENV PYTHON_VERSION 3.11.11

RUN wget -qO- https://astral.sh/uv/install.sh | sh

ENV UV_CACHE_DIR=/home/pruebatest/.cache/uv
ENV UV_PROJECT_ENVIRONMENT=/home/pruebatest/.venv

WORKDIR /app/test   

ENTRYPOINT ["make", "test"]
