#!/usr/bin/env python
# -*- coding: utf-8 -*-

import thriftpy
from thriftpy.thrift import TProcessor
from dispatcher import GoodsDispatcher

goods = thriftpy.load("def/goods.thrift", module_name="goods_thrift")

app = TProcessor(goods.GoodsService, GoodsDispatcher())
