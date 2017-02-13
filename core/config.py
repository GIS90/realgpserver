# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    get config.yaml file informations about server host, server port,
    database host, database port, database user, database password, database default,
    gps folder
    database gps table
    it need run this process to modify config file information only

demo:

    server informations:
        host, port = get_server_config()
    database informations:
        host, port, user, password, database = get_db_config()
    gps folder informations:
        gps_folder = get_gps_folder_config()
------------------------------------------------
"""
import yaml
import os
import sys
import inspect


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/12/9"


# get current folder, solve is or not frozen of the script
def _get_cur_folder():
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(__file__))
    else:
        cur_folder = os.path.dirname(inspect.getfile(inspect.currentframe()))
        return os.path.abspath(cur_folder)


_cur_folder = _get_cur_folder()
_config_folder = os.path.abspath(os.path.join(_get_cur_folder(), "../config"))
_config_file = os.path.abspath(os.path.join(_config_folder, "config.yaml"))

_config_info = yaml.load(file(_config_file))


def get_db_config():
    """
    get database config informations
    :return: database host, database port, database user,
    database password, database default
    """
    host = _config_info["Database"]["host"]
    port = _config_info["Database"]["port"]
    user = _config_info["Database"]["user"]
    password = _config_info["Database"]["password"]
    database = _config_info["Database"]["database"]

    if isinstance(port, basestring):
        port = int(port)
    if isinstance(password, int):
        password = str(password)
    return host, port, user, password, database


def get_server_config():
    """
    get server config information
    :return: server host, server port
    """
    host = _config_info["Server"]["host"]
    port = _config_info["Server"]["port"]
    if isinstance(port, basestring):
        port = int(port)
    return host, port


def get_gps_folder_config():
    """
    get gps stored folder
    :return: gps folder
    """
    return _config_info["GPSFolder"]


def get_gps_table_config():
    """
    get database gps table
    :return: gps table
    """
    return _config_info["GPSTable"]
