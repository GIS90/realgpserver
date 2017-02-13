# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    command tool be used to execute command of Win or Linux system.
    subprocess is beat command module,
    this intends to replace other module about command function, older modules and functions,
    such as: os.system、os.spawn*、os.popen*、popen2.*、commands.*

demo:
command = "netstat -ano | findstr 80"
retcode = COMMAND.execute(command, is_repipe=False)
------------------------------------------------
"""
import platform
import subprocess

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/12/8"
__method__ = ["execute"]


class System_Type(object):
    win = "Windows"
    linux = "Linux"
    other = "Other System"


class COMMAND(object):
    def __init__(self):
        self._local_system = _get_system()

    def _get_system(self):
        if hasattr(platform, "system"):
            return platform.system()
        else:
            if os.name == "nt":
                return System_Type.win
            elif os.name == "posix":
                return System_Type.linux
            else:
                return System_Type.other

    @classmethod
    def execute(cls, command, is_repipe=False):
        """
        this fun is execute command of Win or Linux system,
        if you want to interact command line also you will be used to subprecess.communcate
        such as:
            import subprocess
            child = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
            child.communicate("vamei")
        :param command: system command
        :param is_repipe: is or not redirect PIPE
            if is_repipe is true, subprocess.call is redirect PIPE
            else, subprocess.call is not redirect PIPE
        :return:
            if command execute success, return 0
            else command execute failure, return -1
        """
        assert isinstance(command, basestring)
        assert isinstance(is_repipe, bool)
        try:
            if not is_repipe:
                return_code = subprocess.call(command,
                                              shell=True)
            else:
                return_code = subprocess.call(command,
                                              stdin=None,
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE,
                                              shell=True)
            return 0 if return_code >= 0 else -1
        except subprocess.CalledProcessError as e:
            emsg = "COMMAND execute is CalledProcessError: %s" % e.message
            raise Exception(emsg)
        except OSError as e:
            emsg = "COMMAND execute is OSError: %s" % e.message
            raise Exception(emsg)
        except Exception as e:
            emsg = "COMMAND execute is error: %s" % e.message
            raise Exception(emsg)
