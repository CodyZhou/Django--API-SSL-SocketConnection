#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : libclient.py
# @Time    : 2017/3/17 0:30
# @Author  : Cody Zhou
# @Software: PyCharm
# @Description: 
#
#
import socket

from pythontest.settings import (
    SERVER_HOST,
    SERVER_PORT
)

from pythontest.libs.libcrypto import encrypt


class Minion():
    def __init__(self, listen_num=5):
        try:
            self.host = SERVER_HOST
            self.port = SERVER_PORT
            self.listen_number = listen_num
        except:
            raise ValueError("Please check SERVER_HOST and SERVER_PORT from settings.py!")

    def set_message(self, message):
        self.data = encrypt(message=message)

    def run(self):
        minion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        minion.connect((self.host, int(self.port)))

        result = ''
        minion.send(self.data)
        recv_data = minion.recv(1024)

        result = str(recv_data, 'utf8')

        minion.close()
        return result


if __name__ == '__main__':
    client = Minion()
    client.set_message('Get a message from client!')

    result = client.run()
    print(result)
