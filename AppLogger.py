__author__ = 'kakarthikeyan'

import logging
from Config import *

class AppLogger:
    def __init__(self):
        print "Creating logger"
        self.logger = logging.getLogger(__name__)
        handler = logging.FileHandler(LOGFILE)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(LOGLEVEL)

    def log(self, level, message):
        print "Called log"
        self.logger.log(level, message)
