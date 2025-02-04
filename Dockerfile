FROM python:alpine

RUN apk add --no-cache \
    make 


RUN adduser -D -h /home/pruebatest pruebatest

USER pruebatest




ENV PATH="/home/pruebatest/.local/bin:$PATH"


RUN wget -qO- https://astral.sh/uv/install.sh | sh


WORKDIR /app/test   

ENTRYPOINT ["make", "test"]
