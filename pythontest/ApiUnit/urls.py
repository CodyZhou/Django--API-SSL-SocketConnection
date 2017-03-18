#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : urls.py
# @Time    : 2017/3/16 20:41
# @Author  : Cody Zhou
# @Software: PyCharm
# @Description: 
#
#
from django.conf.urls import url

from pythontest.ApiUnit.views import MasterServerView

app_name = 'API'

urlpatterns = [
    url(r'^master/$', MasterServerView.as_view(), name='master_server_run')
]
