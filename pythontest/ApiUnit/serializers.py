#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : serializers.py
# @Time    : 2017/3/16 20:54
# @Author  : Cody Zhou
# @Software: PyCharm
# @Description: 
#
#
from rest_framework import serializers
from pythontest.ApiUnit.validators import command_validator


class ApiDataSerializer(serializers.Serializer):
    command = serializers.CharField(max_length=20, validators=[command_validator])
    message = serializers.CharField(allow_blank=True)





