#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 3/22/2017 2:04 PM
# @Author  : Cody Zhou
# @File    : tests2.py
# @Software: PyCharm
# @Description:
#   
#   
from rest_framework import status
from rest_framework.test import APITestCase


class MasterServerTests2(APITestCase):
    url = 'http://localhost:8000/api/master/'
    data_valid = {"command":"run","message": "This is a test from client!"}

    def test_post_data_valid(self):
        """
        Used to test send a valid data, the master server does not run, everything is working.
        Notice: this method can not do the test at the same time with method test_post_master_server_no_run().
            Because this method need run master server first.
        """
        reponse = self.client.post(self.url, data=self.data_valid, format='json')
        # print(reponse.content)
        self.assertEqual(reponse.status_code, status.HTTP_200_OK)
        self.assertEqual(reponse.content.decode('utf8'), '{"result":"successful"}')

if __name__ == '__main__':

    mst = MasterServerTests2()
    mst.test_post_data_valid()
