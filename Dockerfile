FROM python:alpine

RUN apk add --no-cache \
    make 


RUN adduser -D -h /home/pruebatest pruebatest

USER pruebatest

RUN mkdir -p /home/userTest/.cache && \
    chmod -R a+w /home/userTest/.cache && \
    mkdir -p /home/userTest/.venv && \
    chmod -R a+w /home/userTest/.venv 

ENV PATH="/home/pruebatest/.local/bin:$PATH"


RUN wget -qO- https://astral.sh/uv/install.sh | sh

ENV UV_CACHE_DIR=/home/userTest/.cache/uv
ENV UV_PROJECT_ENVIRONMENT=/home/userTest/.venv

WORKDIR /app/test   

ENTRYPOINT ["make", "test"]
