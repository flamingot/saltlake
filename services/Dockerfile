FROM python:2-stretch
WORKDIR /usr/src/saltlake/services

RUN pip install gunicorn_thrift thriftpy

COPY . .

EXPOSE 8000

RUN cd /usr/src/saltlake/services/
ENTRYPOINT ["/usr/src/saltlake/services/run.sh", "goods.app", "2", "8000"]
