# coding=utf-8
# Copyright (C) 2018-2025 by dream-alpha
# License: GNU General Public License v3.0 (see LICENSE file for details)


from Poll import Poll
from Components.Element import cached
from Components.Converter.Converter import Converter


class COCDiskSpaceInfo(Poll, Converter):
    SPACEINFO = 0

    def __init__(self, atype):
        Converter.__init__(self, atype)
        Poll.__init__(self)

        self.type = self.SPACEINFO
        self.poll_interval = 2500
        self.poll_enabled = True

    def doSuspend(self, suspended):
        if suspended:
            self.poll_enabled = False
        else:
            self.downstream_elements.changed((self.CHANGED_POLL,))
            self.poll_enabled = True

    @cached
    def getText(self):
        return self.source.space

    text = property(getText)
