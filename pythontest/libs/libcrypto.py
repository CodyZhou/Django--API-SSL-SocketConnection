#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : libcrypto.py
# @Time    : 2017/3/16 22:30
# @Author  : Cody Zhou
# @Software: PyCharm
# @Description: 
#
#
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from pythontest.settings import (
    PUBLIC_KEY,
    PRIVATE_KEY,
    SECURITY_CODE
)


def encrypt(message):
    """
        Used to encrypt the information.
    """
    public_key = open(PUBLIC_KEY, 'rb').read()
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    encrypt_data = cipher_rsa.encrypt(bytes(message, 'utf-8'))

    # print(encrypt_data)
    return encrypt_data


def decrypt(data):
    """
        Used to decrypt the information
    """

    # print(data)
    private_key = open(PRIVATE_KEY, 'rb').read()
    recipient_key = RSA.import_key(private_key, passphrase=SECURITY_CODE)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    result = cipher_rsa.decrypt(data)

    # print(result)

    return str(result, 'utf-8')

    # Encrypt Data

if __name__ == '__main__':
    data = encrypt('This is a test text!')

    message = decrypt(data)

    print(message)


