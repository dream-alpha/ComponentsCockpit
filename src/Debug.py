# coding=utf-8
#
# Copyright (C) 2018-2025 by dream-alpha
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


import sys
import logging
from Components.config import config, ConfigSubsection, ConfigDirectory, ConfigSelection  # noqa: F401, pylint: disable=unused-import
from .Version import ID, PLUGIN


logger = None
streamer = None
format_string = ID + ": " + "%(levelname)s: %(filename)s: %(funcName)s: %(message)s"
log_levels = {"ERROR": logging.ERROR, "INFO": logging.INFO, "DEBUG": logging.DEBUG}
# Convert log_levels to list of tuples for ConfigSelection
log_level_choices = [(k, k) for k in log_levels]
plugin = PLUGIN.lower()
# Create dynamic config namespace using setattr instead of exec for better Python 3 compatibility
if not hasattr(config.plugins, plugin):
    setattr(config.plugins, plugin, ConfigSubsection())
plugin_config = getattr(config.plugins, plugin)
if not hasattr(plugin_config, 'debug_log_level'):
    plugin_config.debug_log_level = ConfigSelection(default='INFO', choices=log_level_choices)


def initLogging():
    global logger  # pylint: disable=global-statement
    global streamer  # pylint: disable=global-statement
    if not logger:
        logger = logging.getLogger(ID)
        formatter = logging.Formatter(format_string)
        streamer = logging.StreamHandler(sys.stdout)
        streamer.setFormatter(formatter)
        logger.addHandler(streamer)
        logger.propagate = False
        current_plugin_config = getattr(config.plugins, plugin)
        setLogLevel(log_levels[current_plugin_config.debug_log_level.value])


def setLogLevel(level):
    logger.setLevel(level)
    streamer.setLevel(level)
    logger.info("level: %s", level)
