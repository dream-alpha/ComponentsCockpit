# coding=utf-8
# Copyright (C) 2018-2025 by dream-alpha
# License: GNU General Public License v3.0 (see LICENSE file for details)


from enigma import iServiceInformation
from ServiceReference import ServiceReference
from Components.Element import cached, ElementError
from Components.Converter.Converter import Converter


class COCMovieInfo(Converter):
    # meta description when available.. when not .eit short description
    MOVIE_SHORT_DESCRIPTION = 0
    MOVIE_META_DESCRIPTION = 1  # just meta description when available
    MOVIE_REC_SERVICE_NAME = 2  # name of recording service
    MOVIE_REC_FILESIZE = 3  # filesize of recording
    MOVIE_EVENT_DURATION = 4  # duration of recorded event

    def __init__(self, atype):
        if atype == "ShortDescription":
            self.type = self.MOVIE_SHORT_DESCRIPTION
        elif atype == "MetaDescription":
            self.type = self.MOVIE_META_DESCRIPTION
        elif atype == "RecordServiceName":
            self.type = self.MOVIE_REC_SERVICE_NAME
        elif atype == "FileSize":
            self.type = self.MOVIE_REC_FILESIZE
        elif atype == "MovieDuration":
            self.type = self.MOVIE_EVENT_DURATION
        else:
            raise ElementError(
                f"'{atype}' is not <ShortDescription|MetaDescription|RecordServiceName|FileSize|MovieDuration> for MovieInfo converter")
        Converter.__init__(self, atype)

    @cached
    def getText(self):
        text = ""
        service = self.source.service
        info = self.source.info
        if info and service:
            if self.type == self.MOVIE_EVENT_DURATION:
                event = self.source.event
                if event:
                    text = str(event.getDuration())
            if self.type == self.MOVIE_SHORT_DESCRIPTION:
                event = self.source.event
                if event:
                    text = info.getInfoString(
                        service, iServiceInformation.sDescription)
                    if text == "":
                        text = event.getShortDescription()
            elif self.type == self.MOVIE_META_DESCRIPTION:
                text = info.getInfoString(
                    service, iServiceInformation.sDescription)
            elif self.type == self.MOVIE_REC_SERVICE_NAME:
                rec_ref_str = info.getInfoString(
                    service, iServiceInformation.sServiceref)
                text = ServiceReference(rec_ref_str).getServiceName()
            elif self.type == self.MOVIE_REC_FILESIZE:
                filesize = info.getInfoObject(
                    service, iServiceInformation.sFileSize)
                if filesize is not None:
                    filesize /= 1024 * 1024
                    if filesize > 0:
                        if filesize < 1000:
                            text = f"{filesize:d} MB"
                        else:
                            text = f"{filesize // 1024:d} GB"
        return text

    text = property(getText)

    @cached
    def getTime(self):
        duration = 0
        event = self.source.event
        if event:
            duration = event.getDuration()
        return duration

    time = property(getTime)
