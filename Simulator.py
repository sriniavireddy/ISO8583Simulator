__author__ = 'kakarthikeyan'

from RequestHandler import *
from socket import *
import os


def setupLogger():
        logger = logging.getLogger(APPNAME)
        handler = logging.FileHandler(LOGFILE)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(LOGLEVEL)

class Server:
    def __init__(self):
        setupLogger()
        # Create a TCP socket
        self.s = socket(AF_INET, SOCK_STREAM)
        # bind it to the server port
        self.s.bind((HOSTNAME, int(PORT)))
        # Configure it to accept up to N simultaneous Clients waiting...
        self.s.listen(MAXCONN)
        self.handler = RequestHandler()
        self.handler.initialize()

    def run(self):
        # wait for a connection
        waitForRequest = True
        while waitForRequest:
            try:
                print "Starting to receive"
                (clientSocket, address) = self.s.accept()
                # as soon as we receive a connection from a client, ask a request handler to handle the request
                print "Received request"
                self.handler.handleRequest(clientSocket)
                print "Finished the request Handling"
            except KeyboardInterrupt,e:
                print "Received shutdown command - shutting down"
                break
        print "Simulator going down"


if __name__ == "__main__":
    # run the server
    Server().run()
