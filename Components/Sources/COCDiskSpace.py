# coding=utf-8
# Copyright (C) 2018-2025 by dream-alpha
# License: GNU General Public License v3.0 (see LICENSE file for details)


from Components.Element import cached
from Components.Sources.Source import Source


class COCDiskSpace(Source):
    def __init__(self, player):
        Source.__init__(self)
        self.__player = player

    @cached
    def getDiskSpace(self):
        return self.__player.getBookmarksSpaceInfo()

    space = property(getDiskSpace)
