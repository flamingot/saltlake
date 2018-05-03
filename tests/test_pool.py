#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import logging
from datetime import datetime
import thriftpy
from thriftpy.rpc import client_context
import thrift_connector.connection_pool as connection_pool


_LOG_FILE = 'saltlake.log'
goods = thriftpy.load("../services/def/goods.thrift", module_name="goods_thrift")


if __name__ == '__main__':
    logging.basicConfig(filename = _LOG_FILE, level = logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    reload(sys)
    sys.setdefaultencoding("utf8")

    logging.info('[client] ===========================================')
    logging.info('[client] running at %s' % datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
    logging.info('client] ===========================================')

    pool = connection_pool.ClientPool(
        goods.GoodsService,
        'localhost',
        8000,
        connection_class=connection_pool.ThriftPyCyClient
    )

    for i in range(100):
        print pool.getCategories(3724)
