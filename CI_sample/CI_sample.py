#!/usr/bin/env python
# -*- coding: utf-8 -*-


def calltest(args):
    call, status = args
    if status == 'good':
        return 'good', 0
    else:
        return 'bad', 0


def cisample(status):
    args = 'call', status
    ret, rc = calltest(args)
    return 'call %s' % ret, rc
