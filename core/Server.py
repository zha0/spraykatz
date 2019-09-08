# coding: utf-8

# Author:	Lyderic LEFEBVRE
# Twitter:	@lydericlefebvre
# Mail:		lylefebvre.infosec@gmail.com
# LinkedIn:	https://www.linkedin.com/in/lydericlefebvre


# Imports
import os, logging, pexpect
from core.Colors import *
from core.Paths import *
from core.SmbServer import *


def launchServer(q, local_ip, alea, verbosity, server):
    if server == "smb":
        launchSmbServer(q, local_ip, alea, verbosity)