FROM alpine:latest

RUN apk add --no-cache \
    make \
    python3

WORKDIR /app/test

RUN adduser -D -h /home/userTest userTest

USER userTest


RUN mkdir -p /home/userTest/.cache && \
    chmod -R a+w /home/userTest/.cache


ENV PATH="/home/userTest/.local/bin:$PATH"

RUN wget -qO- https://astral.sh/uv/install.sh | sh

ENV UV_CACHE_DIR=/home/userTest/.cache/uv

ENTRYPOINT ["make", "test"]
