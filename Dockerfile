FROM alpine:latest

RUN apk add --no-cache \
    make \
    python3


RUN adduser -D -h /home/pruebatest pruebatest

USER pruebatest




ENV PATH="/home/pruebatest/.local/bin:$PATH"

ENV PYTHON_VERSION 3.11.11

RUN wget -qO- https://astral.sh/uv/install.sh | sh


WORKDIR /app/test   

ENTRYPOINT ["make", "test"]
