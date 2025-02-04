FROM alpine:latest

RUN apk add --no-cache \
    make \
    python3 

WORKDIR /app/test

RUN adduser -D -h /home/userTest userTest

USER userTest

ENV PATH="/home/userTest/.local/bin:$PATH"

RUN wget -qO- https://astral.sh/uv/install.sh | sh

ENTRYPOINT ["make", "test"]
