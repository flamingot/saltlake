FROM python:2-alpine
WORKDIR /usr/src/saltlake/services

COPY . .
RUN cd /usr/src/saltlake/services/

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    freetype-dev \
    musl-dev
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del .build-deps

EXPOSE 8000
ENTRYPOINT ["/usr/src/saltlake/services/run.sh", "goods.app", "2", "8000"]
