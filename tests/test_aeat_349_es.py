#!/usr/bin/env python
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends


class Aeat349EsTestCase(unittest.TestCase):
    '''
    Test AEAT 349 ES module.
    '''

    def setUp(self):
        trytond.tests.test_tryton.install_module('aeat_349_es')

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            Aeat349EsTestCase))
    return suite
