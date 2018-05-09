#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

_VERSION = '0.1'

def getHostIp():
    si = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]]
    return si[0][1]

class GoodsDispatcher(object):
    def getCategories(self, cid):
        return [
            _VERSION, 'getCategories', str(cid), getHostIp()
        ]
