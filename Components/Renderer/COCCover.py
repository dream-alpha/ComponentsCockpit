# coding=utf-8
# Copyright (C) 2018-2025 by dream-alpha
# License: GNU General Public License v3.0 (see LICENSE file for details)


from enigma import ePixmap, gPixmapPtr, ePicLoad
from Components.Renderer.Renderer import Renderer
from Components.AVSwitch import AVSwitch


class COCCover(Renderer):
    GUI_WIDGET = ePixmap

    def __init__(self):
        self.skinAttributes = None
        Renderer.__init__(self)

    def destroy(self):
        Renderer.destroy(self)

    def applySkin(self, desktop, parent):
        attribs = self.skinAttributes
        for (attrib, value) in self.skinAttributes:
            if attrib == "type":
                self.type = value
                attribs.remove((attrib, value))
        self.skinAttributes = attribs
        return Renderer.applySkin(self, desktop, parent)

    def changed(self, what):
        if self.instance is not None:
            if what[0] != self.CHANGED_CLEAR:
                if self.source.cover:
                    scale = AVSwitch().getFramebufferScale()
                    size = self.instance.size()
                    self.picload = ePicLoad()
                    self.picload.PictureData.append(self.displayPixmapCallback)
                    self.picload.setPara(
                        (size.width(), size.height(), scale[0], scale[1], False, 1, "#ff000000"))
                    self.picload.startDecodeBuffer(
                        bytearray(self.source.cover), len(self.source.cover), False)
                else:
                    self.instance.setPixmap(gPixmapPtr())
            else:
                self.instance.setPixmap(gPixmapPtr())

    def displayPixmapCallback(self, picinfo=None):
        if self.picload and picinfo:
            self.instance.setPixmap(self.picload.getData())
