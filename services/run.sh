#!/bin/sh

service=$1
workers=${2:-2}
port=${3:-8000}

gunicorn_thrift $service:app -w $workers -b ":$port" -k thriftpy_sync \
  --thrift-protocol-factory \
    thriftpy.protocol:TCyBinaryProtocolFactory \
  --thrift-transport-factory \
    thriftpy.transport:TCyBufferedTransportFactory
