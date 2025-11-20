# coding=utf-8
# Copyright (C) 2018-2025 by dream-alpha
# License: GNU General Public License v3.0 (see LICENSE file for details)


from Components.Element import cached
from Components.Sources.CurrentService import CurrentService
from Components.Sources.Event import Event


class COCCurrentService(CurrentService, Event):
    def __init__(self, navcore, player):
        CurrentService.__init__(self, navcore)
        Event.__init__(self)
        self.__player = player

    def cueSheet(self):
        return self.__player

    @cached
    def getInfo(self):
        return self.service and self.__player.getInfo()

    info = property(getInfo)

    @cached
    def getEvent(self):
        return self.service and self.__player.getEvent()

    event = property(getEvent)

    @cached
    def getCurrentService(self):
        service = self.navcore.getCurrentService()
        if service is not None:
            service.cutList = self.cueSheet
        return service

    service = property(getCurrentService)

    @cached
    def getCurrentPlayer(self):
        return self.__player

    player = property(getCurrentPlayer)
