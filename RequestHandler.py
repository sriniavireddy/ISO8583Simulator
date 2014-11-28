from Config import *
import logging
from MessageFactories import *
import sys

LOGGER = logging.getLogger(APPNAME)

# factory method to determine the message type this simulator will handle
def getRequestHandler():
    if (MSGTYPE == "ISO8583"):
        return ISO8583RequestHandler()
    else:
        raise NotImplementedError("Message types other than ISO8583 cannot be handled by this Simulator")


'''
this class is the base class for handling simulator requests.
Specialized functionality can be overridden in derived classes
'''


class RequestHandler:
    def __init__(self):
        self.msgFactory = MessageFactory()
        self.handler = None

    def initialize(self):
        self.handler = getRequestHandler()

    # interface Definition
    def handle(self, clientSocket):
        raise NotImplementedError("Handle request of the base class called")

    def handleRequest(self, clientSocket):
        self.handler.handle(clientSocket)


class ISO8583RequestHandler(RequestHandler):
    def getCustomISOObject(self):
        temp = ISO8583()
        # change the protocol - this is for customization
        temp.redefineBit(18, '18', 'Merchant Category Code', 'N', 4, 'n')
        temp.redefineBit(53, '53','Security related control information','LL',76,'n')
        temp.redefineBit(60, '60', 'Additional Data', 'LLL', 999, 'ans')
        temp.redefineBit(62, '62', 'Custom Data', 'AN', 26, 'ans')
        return temp

    # overridden function
    def handle(self, clientSocket):
        # receive message
        print "Receiving length"
        length = clientSocket.recv(4)
        if length == "SHUT":
            raise KeyboardInterrupt
        if length:
            LOGGER.log(logging.INFO, "received length %s " % length)
            #isoStr = clientSocket.recv(int(length))
	    isoStr = clientSocket.recv(2048)
            if isoStr:
                isoStr = length + isoStr
                LOGGER.log(logging.INFO, "Input ASCII |%s|" % isoStr)
                msg = self.getCustomISOObject()
                #parse the iso
                try:
                    if BIGENDIAN:
                        msg.setNetworkISO(isoStr)
                    else:
                        msg.setNetworkISO(isoStr, False)

		    # print values in input
		    v1 = msg.getBitsAndValues()
		    for v in v1 :
                        print ('Bit %s of type %s with value = %s' % (v['bit'], v['type'], v['value']))
                    msgType = msg.getMTI()
                    validMsg = self.msgFactory.getFactory(msgType).getRequestValidator().validateMessage(msg)
                    # generate a response
                    errorToForce = "30"
                    if validMsg == True:
                        errorToForce = None
                    resp = self.msgFactory.getFactory(msgType).getResponseGenerator().generateResponse(msg,errorToForce)

                    # send the response back
                    rawResponse = ""
                    if BIGENDIAN:
                        rawResponse = resp.getNetworkISO()
                    else:
                        rawResponse = resp.getNetworkISO(False)

		    # print Bits in Response
		    v1 = resp.getBitsAndValues()
		    for v in v1:
                        print ('Bit %s of type %s with value = %s' % (v['bit'], v['type'], v['value']))

                    # log before sending the response
                    LOGGER.log(logging.INFO, "Output ASCII |%s|" % rawResponse)
		    print rawResponse
                    clientSocket.send(rawResponse)

                except:
                    LOGGER.log(logging.CRITICAL, "Exception happened while processing request" + str(sys.exc_info()))
        else:
            LOGGER.log(logging.CRITICAL, "Wrong input")

        # close socket
        clientSocket.close()
        LOGGER.log(logging.INFO, "---------------------------------------------------------------------------------")
