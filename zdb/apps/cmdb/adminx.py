# _*_ coding: utf-8 _*_
# @time     : 2018/12/03
# @Author   : Amir
# @Site     : 
# @File     : adminx.py
# @Software : PyCharm

import xadmin
from .models import Zones, Servers, Business


class ZonesAdmin(object):
    list_display = ["name", "city", "status", "add_time"]
    list_filter = ["name", "city"]
    search_fields = ['name', ]


class ServersAdmin(object):
    list_display = ["ip", "port", "user", "user_pass", "host_name", "memory", "cpu", "raid", "disk", "zone", "status",
                    "add_time"]
    list_filter = ["ip", ]
    search_fields = ['ip', ]


class BusinessAdmin(object):
    list_display = ["name", "status", "add_time"]
    list_filter = ["name", ]
    search_fields = ['name', ]


xadmin.site.register(Zones, ZonesAdmin)
xadmin.site.register(Servers, ServersAdmin)
xadmin.site.register(Business, BusinessAdmin)
