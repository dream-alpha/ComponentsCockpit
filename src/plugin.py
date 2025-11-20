# coding=utf-8
# Copyright (C) 2018-2025 by dream-alpha
# License: GNU General Public License v3.0 (see LICENSE file for details)


from .Debug import logger
from .Version import VERSION


def Plugins(**__):
    logger.info("  +++ Version: %s starts...", VERSION)
    return []
