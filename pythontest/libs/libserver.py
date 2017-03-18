#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : libserver.py
# @Time    : 2017/3/16 22:43
# @Author  : Cody Zhou
# @Software: PyCharm
# @Description: 
#
#
import socket
import time

from pythontest.settings import (
    SERVER_RECV_MESSAGE_FILE,
    SERVER_HOST,
    SERVER_PORT
)
from pythontest.libs.libcrypto import decrypt


class MasterServer():
    """
        Master Server.
        Used to get the information from the clients.
    """

    def __init__(self, listen_num=5):
        try:
            self.host = SERVER_HOST
            self.port = SERVER_PORT
            self.listen_number = listen_num
        except:
            raise ValueError("Please check SERVER_HOST and SERVER_PORT from settings.py!")

    def run(self):
        master_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print('Master Server Started ... ')

        master_server.bind((self.host, int(self.port)))
        master_server.listen(self.listen_number)

        print('Master Server is listening {0}:{1} ...' . format(self.host, self.port))

        while True:
            conn, addr = master_server.accept()

            data = conn.recv(1024)

            # Use RSA to decrypt data
            try:
                message = decrypt(data=data)

            except:
                conn.send(bytes('Unauthenticated connection!', 'utf8'))
                conn.close()
                break

            print(message)

            self.write_data_to_file(addr, message)

            # Send successful message to client
            conn.send(bytes('successful', 'utf8'))
            # conn.close()

    def write_data_to_file(self, addr, data):
        result = '[{0}] From {1} get message: {2} ' . format(time.strftime('%m/%d/%Y %H:%M:%S', time.localtime()), addr, data)

        print(result)

        with open(SERVER_RECV_MESSAGE_FILE, 'a') as file:
            file.write(result)
            file.write('\n')


if __name__ == '__main__':

    serv = MasterServer()
    serv.run()


