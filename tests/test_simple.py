#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import logging
from datetime import datetime
import thriftpy
from thriftpy.rpc import client_context


_LOG_FILE = 'saltlake.log'
goods = thriftpy.load("services/def/goods.thrift", module_name="goods_thrift")


class RpcClient():


    def __init__(self, zookhost, appname):
        self.zookhost=zookhost
        self.appname=appname


    def request(self):
        host,port=("localhost", 8001)
        with client_context(goods.GoodsService, host, port) as c:
            response = c.getCategories(3724)
            print(response)


if __name__ == '__main__':
    logging.basicConfig(filename = _LOG_FILE, level = logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    reload(sys)
    sys.setdefaultencoding("utf8")

    logging.info('[client] ===========================================')
    logging.info('[client] running at %s' % datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    logging.info('client] ===========================================')

    client=RpcClient('localhost:2181', 'flamingo')
    client.request()
