# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    record info, debug, error, fatial information
    refer to ZhiShu system gps data

demo:
    info_msg = "XXXX occur exception"
    debug_msg = "XXXX occur exception"
    error_msg = "XXXX occur exception"
    fatal_msg = "XXXX occur exception"

    log.info(info_msg)
    log.debug(debug_msg)
    log.error(error_msg)
    log.fatal(fatal_msg)
------------------------------------------------
"""

import inspect
import logging
import os
import sys
from logging.handlers import RotatingFileHandler

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/12/07"

# log config
_MAX_SIZE = 10 * 1024 * 1024
_BACKUP_COUNT = 8
_FORMAT = "%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s"
_LOG_LEVEL = 0
_LOG_DELAY = 2


# get current log.py folder, solve is or not frozen of the script
def _get_cur_folder():
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(__file__))
    else:
        cur_folder = os.path.dirname(inspect.getfile(inspect.currentframe()))
        return os.path.abspath(cur_folder)


_cur_folder = _get_cur_folder()
_log_folder = os.path.abspath(os.path.join(_get_cur_folder(), "../log"))
if not os.path.exists(_log_folder):
    try:
        os.makedirs(_log_folder)
    except Exception as e:
        msg = "create log folder is failure: %s" % e.message
        raise Exception(msg)

_log_file = os.path.abspath(os.path.join(_log_folder, "gps_logs.log"))
_formatter = logging.Formatter(_FORMAT)
# file log
_file_handle = RotatingFileHandler(filename=_log_file,
                                   mode='a',
                                   maxBytes=_MAX_SIZE,
                                   backupCount=_BACKUP_COUNT,
                                   encoding=None,
                                   delay=_LOG_DELAY)

_file_handle.setFormatter(_formatter)
_file_handle.setLevel(_LOG_LEVEL)

# print log
_strout_handle = logging.StreamHandler(sys.stdout)
_strout_handle.setFormatter(_formatter)
_strout_handle.setLevel(_LOG_LEVEL)

# log object
log = logging.getLogger()
log.setLevel(_LOG_LEVEL)
log.addHandler(_file_handle)
log.addHandler(_strout_handle)
