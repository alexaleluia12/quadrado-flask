#-*- coding:utf-8 -*-

import os
import unittest
import tempfile
import json
import urllib

import quadrado

def helperQuery(initString, dictToAdd):
    """Return a query string"""
    return initString + '?' + urllib.urlencode(dictToAdd)


class QuadradoAppTest(unittest.TestCase):

    def setUp(self):
        self.app = quadrado.app.test_client()

    def test_home_page(self):
        site = self.app.get('/')
        self.assertTrue('[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]' in site.data)

    def test_api_success(self):
        toGet = helperQuery('/numdata', {'init': 21, 'end': 30})
        site = self.app.get(toGet)
        jsonData = json.loads(site.data)
        self.assertEqual(
            [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            jsonData['numList']
        )

    def test_api_fail(self):
        toGet = helperQuery('/numdata', {'init': 4, 'end': 10})
        site = self.app.get(toGet)
        jsonData = json.loads(site.data)
        self.assertNotEqual(
            [4, 5, 6 , 7, 8, 9, 10],
            jsonData
        )

if __name__ == '__main__':
    unittest.main()

