# coding=utf-8
# Copyright (C) 2018-2025 by dream-alpha
# License: GNU General Public License v3.0 (see LICENSE file for details)


from Components.Converter.ServiceTime import ServiceTime


class COCServiceTime(ServiceTime):
    def __init__(self, atype):
        ServiceTime.__init__(self, atype)
