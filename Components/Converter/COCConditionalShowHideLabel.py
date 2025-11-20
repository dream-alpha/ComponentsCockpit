# coding=utf-8
# Copyright (C) 2018-2025 by dream-alpha
# License: GNU General Public License v3.0 (see LICENSE file for details)


from Components.Converter.ConditionalShowHide import ConditionalShowHide


class COCConditionalShowHideLabel(ConditionalShowHide):
    def __init__(self, args):
        ConditionalShowHide.__init__(self, args)

    def getText(self):
        return ""

    text = property(getText)
