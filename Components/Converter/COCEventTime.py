# coding=utf-8
# Copyright (C) 2018-2025 by dream-alpha
# License: GNU General Public License v3.0 (see LICENSE file for details)


from time import time
from Poll import Poll
from Components.Element import cached
from Components.Converter.Converter import Converter


class COCEventTime(Poll, Converter):
    POSITION = 1
    REMAINING = 2

    def __init__(self, atype):
        Converter.__init__(self, atype)
        Poll.__init__(self)
        self.poll_interval = 1000
        self.poll_enabled = True
        args = atype.split(",")
        atype = args.pop(0)
        self.negate = "Negate" in args
        if atype == "Position":
            self.type = self.POSITION
        elif atype == "Remaining":
            self.type = self.REMAINING

    @cached
    def getText(self):
        text = ""
        event = self.source.event
        if event:
            value = 0
            start_time = event.getBeginTime()
            duration = event.getDuration()
            now = int(time())
            if self.type == self.REMAINING:
                value = start_time + duration - now
            elif self.type == self.POSITION:
                value = now - start_time
            mins = value / 60
            secs = value % 60
            if self.negate:
                mins *= -1
            text = f"{mins:+d}:{secs:02d}"

        return text

    text = property(getText)
