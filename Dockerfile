FROM python:alpine

RUN apk add --no-cache \
    make 


RUN adduser -D -h /home/pruebatest pruebatest

USER pruebatest

RUN mkdir -p /home/userTest/.cache && \
    chmod -R a+w /home/userTest/.cache


ENV PATH="/home/pruebatest/.local/bin:$PATH"


RUN wget -qO- https://astral.sh/uv/install.sh | sh

ENV UV_CACHE_DIR=/home/userTest/.cache/uv

WORKDIR /app/test   

ENTRYPOINT ["make", "test"]
