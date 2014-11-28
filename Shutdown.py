__author__ = 'kakarthikeyan'


import os
import socket
import sys
from Config import *

try:
    print "IP is %s, and Port is %s" % (HOSTNAME,PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOSTNAME, int(PORT)))
    if s is None:
        print "socket is not open"
    s.send("SHUT")
    print "Sent shutdown message"
    s.close()
except:
    print "Error in sending shutdown message, please kill the process manually" + str(sys.exc_info())



