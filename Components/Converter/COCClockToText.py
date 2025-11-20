# coding=utf-8
# Copyright (C) 2018-2025 by dream-alpha
# License: GNU General Public License v3.0 (see LICENSE file for details)


from time import localtime, strftime, gmtime
from Plugins.SystemPlugins.ComponentsCockpit.__init__ import _
from Components.Converter.ClockToText import ClockToText
from Components.Element import cached
from Components.config import config


class COCClockToText(ClockToText):

    def __init__(self, atype):
        ClockToText.__init__(self, atype)

    @cached
    def getText(self):
        text = ""
        time = self.source.time
        if time is not None:
            if self.type == self.IN_MINUTES:
                text = ""
                if time > -1:
                    mins = time / 60
                    if time % 60 >= 30:
                        mins += 1
                    text = f"{mins} " + _("min")
            elif self.type == self.AS_LENGTH:
                text = f"{time // 60}:{time % 60:02d}"
            elif self.type == self.TIMESTAMP:
                text = str(time)
            else:
                if time > (31 * 24 * 60 * 60):
                    # No Recording should be longer than 1 month
                    t = localtime(time)
                else:
                    t = gmtime(time)

                if self.type == self.WITH_SECONDS:
                    text = f"{t.tm_hour:2d}:{t.tm_min:02d}:{t.tm_sec:02d}"
                elif self.type == self.DEFAULT:
                    text = f"{t.tm_hour:02d}:{t.tm_min:02d}"
                elif self.type == self.DATE:
                    if config.osd.language.value == "de_DE":
                        text = strftime("%A, %d. %B %Y", t)
                    else:
                        text = strftime("%A %B %d, %Y", t)
                elif self.type == self.FORMAT:
                    spos = self.fmt_string.find("%")
                    if spos > -1:
                        s1 = self.fmt_string[:spos]
                        s2 = strftime(self.fmt_string[spos:], t)
                        text = str(s1 + s2)
                    else:
                        text = strftime(self.fmt_string, t)
        return text

    text = property(getText)
