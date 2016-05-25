#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from CI_sample import CI_sample


class CI_sample_test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(CI_sample_test, self).__init__(*args, **kwargs)

    def test_good(self):
        status = 'good'

        ret, rc = CI_sample.cisample(status)
        assert_ret = ('call good', 0)
        self.assertEqual((ret, rc), assert_ret)
