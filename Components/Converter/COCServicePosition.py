# encoding: utf-8
#
# Copyright (C) 2018-2023 dream-alpha
#
# In case of reuse of this source code please do not remove this copyright.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# For more information on the GNU General Public License see:
# <http://www.gnu.org/licenses/>.


import time
from Components.Converter.ServicePosition import ServicePosition
from Components.Element import cached


class COCServicePosition(ServicePosition):

    def __init__(self, atype):
        ServicePosition.__init__(self, atype)
        self.poll_interval = 1000

    @cached
    def getCutlist(self):
        cutlist = []
        if self.source.service is not None:
            cut = self.source.service.cutList()
            if cut:
                cutlist = cut.getCutList()
        return cutlist

    cutlist = property(getCutlist)

    @cached
    def getLength(self):
        return self.source.player.getLength()

    length = property(getLength)

    @cached
    def getPosition(self):
        return self.source.player.getPosition()

    position = property(getPosition)

    @cached
    def getTime(self):
        return self.getLength() / 90000

    time = property(getTime)

    @cached
    def getText(self):
        text = ""
        pos = 0
        seek = self.getSeek()
        if seek is not None:
            if self.type == self.TYPE_ENDTIME:
                pos = (self.length - self.position) / 90000
                t = time.localtime(time.time() + pos)
                text = f"{t.tm_hour:02d}:{t.tm_min:02d}"
                if not self.showNoSeconds:
                    text += f":{t.tm_sec:02d}"
                if pos >= 0:
                    text = ">" + text
                else:
                    text = text + "<"
            else:
                if self.type == self.TYPE_LENGTH:
                    pos = self.length
                elif self.type == self.TYPE_POSITION:
                    pos = self.position
                elif self.type == self.TYPE_REMAINING:
                    pos = self.length - self.position

                pos = -pos if self.negate else pos
                if self.type == self.TYPE_LENGTH:
                    sign = ""
                else:
                    sign = "-" if pos < 0 else "+"

                pos = abs(pos)
                milliseconds = (pos % 90000) / 90
                pos /= 90000
                if self.showHours:
                    text += sign + f"{pos // 3600:d}"  # hours
                    text += f":{pos % 3600 // 60:02d}"  # minutes
                else:
                    text += sign + f"{pos // 60:d}"  # minutes
                if not self.showNoSeconds:
                    text += f":{pos % 60:02d}"  # seconds
                    if self.detailed:
                        text += f":{milliseconds:03.0f}"  # milliseconds
        return text

    text = property(getText)
