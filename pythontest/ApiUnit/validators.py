#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : validators.py
# @Time    : 2017/3/16 21:35
# @Author  : Cody Zhou
# @Software: PyCharm
# @Description: 
#
#
from django.core.validators import ValidationError


def command_validator(value):
    """
    Used to check the command. Only 'run' can be accepted.
    """
    if value == 'run':
        return value
    else:
        raise ValidationError('This command can not be accepted!')



