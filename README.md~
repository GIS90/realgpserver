# SocketServer
gps in read time socket server
## 简介
程序采用Python语言进行编写开发，用来接收GPS原始数据，并进行解析入库Mysql。主要用到SocketServer，log，command，dbhandler，config几个模块。

间隔：1S，实时接收

## 包
import threading 
import inspect 
import logging 
import os 
import sys 
import mysql.connector
import yaml
import platform
import subprocess
from SocketServer import BaseRequestHandler
from datetime import datetime
from logging.handlers import RotatingFileHandler

## 流程图

        +------------+
        | Run Server |
        +------------+
              |
              v
        +------------+
        | Recive GPS | --<--
        +------------+      ^
              |             |
              v             |
        +------------+      ^
        |Analyse GPS |      |
        +------------+      |
              |             ^
              v             |
        +------------+      |
        | Import GPS | -->--
        +------------+

## 运行
- 1.安装python运行环境，安装百度即可。
 - 2.安装程序所用的三方包，详细包见上面功能包。
- 3.修改config文件夹下面的config.yaml配置文件，包括Server的Ip，Port，以及数据库的账号，密码等连接信息。
- 4.运行gps_server.py文件。
- 5.检查配置文件的mysql数据库是否有gps原始数据。
