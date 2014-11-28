__author__ = 'kakarthikeyan'

import ISOValidator
import ISOBuilder
from ISO8583.ISO8583 import ISO8583
import utility
'''
This class the abstract factory class which will produce the request validator and
response generator
'''
class MessageFactory:
    #function to generate a concrete factory based on message type
    def __init__(self):
        self.Message100Factory = MessageFactory0100()
        self.Message200Factory = MessageFactory0200()
        self.Message400Factory = MessageFactory0400()
        self.Message420Factory = MessageFactory0420()

    def getFactory(self, messageType):
        if messageType is None:
            raise "Invalid Message Type"
        elif messageType == "0100":
            return self.Message100Factory
        elif messageType == "0200":
            return self.Message200Factory
        elif messageType == "0400":
            return self.Message400Factory
        elif messageType == "0420":
            return self.Message420Factory
        else:
            raise NotImplementedError("Unimplemented Message Type")

    # interface definitions
    def getRequestValidator(self):
        raise NotImplementedError("Call to Abstract Base class")

    def getResponseGenerator(self):
        raise NotImplementedError("Call to Abstract Base class")

'''
This class produces and stores factory class which will return objects for 0100 message
'''
class MessageFactory0100(MessageFactory):
    def __init__(self):
        self.validator = RequestValidatorFactory().createValidator("0100")
        self.responseGenerator = ResponseGeneratorFactory().createResponseGenerator("0100")
    #overloaded function
    def getRequestValidator(self):
        return self.validator

    def getResponseGenerator(self):
        return self.responseGenerator

'''
This class produces and stores factory class which will return objects for 0200 message
'''
class MessageFactory0200(MessageFactory):
    def __init__(self):
        self.validator = RequestValidatorFactory().createValidator("0200")
        self.responseGenerator = ResponseGeneratorFactory().createResponseGenerator("0200")
    #overloaded function
    def getRequestValidator(self):
        return self.validator

    def getResponseGenerator(self):
        return self.responseGenerator

'''
This class produces and stores factory class which will return objects for 0400 message
'''
class MessageFactory0400(MessageFactory):
    def __init__(self):
        self.validator = RequestValidatorFactory().createValidator("0400")
        self.responseGenerator = ResponseGeneratorFactory().createResponseGenerator("0400")

    #overloaded function
    def getRequestValidator(self):
        return self.validator

    def getResponseGenerator(self):
        return self.responseGenerator

'''
This class produces and stores factory class which will return objects for 0420 message
'''
class MessageFactory0420(MessageFactory):
    def __init__(self):
        self.validator = RequestValidatorFactory().createValidator("0420")
        self.responseGenerator = ResponseGeneratorFactory().createResponseGenerator("0420")

    #overloaded function
    def getRequestValidator(self):
        return self.validator

    def getResponseGenerator(self):
        return self.responseGenerator

'''
This class is the Abstract class for Request Validators
'''

class RequestValidatorFactory:
    # function to create a concrete request Validator
    def createValidator(self,messageType):
        if messageType is None:
            raise "Invalid message type"
        elif messageType == "0100":
            return RequestValidator0100()
        elif messageType == "0200":
            return RequestValidator0200()
        elif messageType == "0400":
            return RequestValidator0400()
        elif messageType == "0420":
            return RequestValidator0420()
        else:
            raise NotImplementedError("Unimplemented request validator")

    # interface definitions
    def validateMessage(self,requestMessage):
        raise NotImplementedError("Call to Abstract base class")

'''
concrete class implementation for 0100 message
'''
class RequestValidator0100(RequestValidatorFactory):

    def __init__(self):
        #mandatory fields shd be present
        self.FieldsToValidate = [2,3,4,7,11,12,13,18,19,22,25,32,37,41,42,43,49]

    #overloaded function
    def validateMessage(self,requestMessage):
        if not isinstance(requestMessage, ISO8583):
            print "Tried to validate a request which is not of ISO8583 type"
            return False
        print "0100 message : " + requestMessage.getNetworkISO()
        return ISOValidator.validateBitMaps(requestMessage,self.FieldsToValidate)


'''
concrete class implementation for 0200 message
'''
class RequestValidator0200(RequestValidatorFactory):

    def __init__(self):
        #mandatory fields shd be present
        self.FieldsToValidate = [2,3,4,7,11,12,13,18,19,22,25,32,37,41,42,43,49]

    #overloaded function
    def validateMessage(self,requestMessage):
        if not isinstance(requestMessage, ISO8583):
            print "Tried to validate a request which is not of ISO8583 type"
            return False
        print "0200 message : " + requestMessage.getNetworkISO()
        return ISOValidator.validateBitMaps(requestMessage,self.FieldsToValidate)


'''
concrete class implementation for 0400 message
'''
class RequestValidator0400(RequestValidatorFactory):

    def __init__(self):
        #mandatory fields shd be present
        self.FieldsToValidate = [2,3,4,7,11,12,13,18,19,22,25,32,37,41,42,43,49,63,90]

    #overloaded function
    def validateMessage(self,requestMessage):
        if not isinstance(requestMessage, ISO8583):
            print "Tried to validate a request which is not of ISO8583 type"
            return False
        print "0400 message : " + requestMessage.getNetworkISO()
        return ISOValidator.validateBitMaps(requestMessage,self.FieldsToValidate)

'''
concrete class implementation for 0420 message
'''
class RequestValidator0420(RequestValidatorFactory):

    def __init__(self):
        #mandatory fields shd be present
        self.FieldsToValidate = [2,3,4,7,11,12,13,18,19,22,25,32,37,41,42,43,49,63,90]

    #overloaded function
    def validateMessage(self,requestMessage):
        if not isinstance(requestMessage, ISO8583):
            print "Tried to validate a request which is not of ISO8583 type"
            return False
        print "0420 message : " + requestMessage.getNetworkISO()
        return ISOValidator.validateBitMaps(requestMessage,self.FieldsToValidate)


'''
This class is the abstract class for response generators
'''
class ResponseGeneratorFactory:
    # function to create a concrete response generator
    def createResponseGenerator(self, messageType):
        if messageType is None:
            raise "Message type should be passed"
        elif messageType == "0100":
            return ResponseGenerator0100()
        elif messageType == "0200":
            return ResponseGenerator0200()
        elif messageType == "0400":
            return ResponseGenerator0400()
        elif messageType == "0420":
            return ResponseGenerator0420()
        else:
            raise NotImplementedError("Other response generators are not implemented")

    # interfaces
    def generateResponse(self, request, forceError = None):
        raise NotImplementedError("Call to Abstract Base class")

'''
concrete class implementation for 0100 response
'''
class ResponseGenerator0100(ResponseGeneratorFactory):
    def __init__(self):
        #mandatory fields to build
        self.FieldsToBuild = [2,3,4,7,11,12,13,14,15,18,19,32,37,38,39,49,60]

    def getCustomISOObject(self):
        temp = ISO8583()
        # change the protocol - this is for customization
        temp.redefineBit(18, '18', 'Merchant Category Code', 'N', 4, 'n')
        temp.redefineBit(53,'53','Security related control information','LL',76,'n')
        temp.redefineBit(60, '60', 'Additional Data', 'LLL', 999, 'ans')
        temp.redefineBit(62, '62', 'Custom Data', 'ANS', 26, 'ans')
        return temp

    #overloaded function
    def generateResponse(self, request, forceError = None):
        if not isinstance(request,ISO8583):
            request = self.getCustomISOObject()

        tempList = list(self.FieldsToBuild)
        # create a dummy response now
        response = self.getCustomISOObject()
        response.setMTI("0110")

        # adding fields based on card
        cardNumber = request.getBit(2)
        cardType = utility.findCardType(cardNumber[2:])
        if cardType == "V":
            tempList.extend([44,62])
        elif cardType == "M":
            tempList.extend([44])
        else:
            pass

        # adding EMV field only if it is set in field 55

        try:
            emvData = request.getBit(55)
            if emvData:
                tempList.append(55)
        except:
            pass

        response = ISOBuilder.buildBitMaps(request,response,tempList,forceError)
        print "110 message response : " + response.getNetworkISO()
        return response


'''
concrete class implementation for 0200 response
'''
class ResponseGenerator0200(ResponseGeneratorFactory):
    def __init__(self):
        #mandatory fields to build
        self.FieldsToBuild = [2,3,4,7,11,12,13,14,15,18,19,32,37,38,39,49,60]

    def getCustomISOObject(self):
        temp = ISO8583()
        # change the protocol - this is for customization
        temp.redefineBit(18, '18', 'Merchant Category Code', 'N', 4, 'n')
        temp.redefineBit(53,'53','Security related control information','LL',76,'n')
        temp.redefineBit(60, '60', 'Additional Data', 'LLL', 999, 'ans')
        temp.redefineBit(62, '62', 'Custom Data', 'ANS', 26, 'ans')
        return temp

    #overloaded function
    def generateResponse(self, request, forceError = None):
        if not isinstance(request,ISO8583):
            request = self.getCustomISOObject()

        tempList = list(self.FieldsToBuild)
        # create a dummy response now
        response = self.getCustomISOObject()
        response.setMTI("0210")

        # adding fields based on card
        cardNumber = request.getBit(2)
        cardType = utility.findCardType(cardNumber[2:])
        if cardType == "V":
            #tempList.extend([44,62])
            tempList.extend([44])
        elif cardType == "M":
            tempList.extend([44])
        else:
            pass

        response = ISOBuilder.buildBitMaps(request,response,tempList,forceError)
        print "210 message response : " + response.getNetworkISO()
        return response

'''
concrete class implementation for 0400 response
'''
class ResponseGenerator0400(ResponseGeneratorFactory):
    def __init__(self):
        #mandatory fields to build
        self.FieldsToBuild = [2,3,4,7,11,12,13,14,15,18,19,32,37,38,39,41,49]

    def getCustomISOObject(self):
        temp = ISO8583()
        # change the protocol - this is for customization
        temp.redefineBit(18, '18', 'Merchant Category Code', 'N', 4, 'n')
        temp.redefineBit(53,'53','Security related control information','LL',76,'n')
        temp.redefineBit(60, '60', 'Additional Data', 'LLL', 999, 'ans')
        temp.redefineBit(62, '62', 'Custom Data', 'ANS', 26, 'ans')
        return temp

    #overloaded function
    def generateResponse(self, request, forceError = None):
        if not isinstance(request,ISO8583):
            request = self.getCustomISOObject()

        tempList = list(self.FieldsToBuild)
        # create a dummy response now
        response = self.getCustomISOObject()
        response.setMTI("0410")

        # adding fields based on card
        cardNumber = request.getBit(2)
        cardType = utility.findCardType(cardNumber[2:])
        if cardType == "V":
            tempList.extend([44,62])
        else:
            pass

        # adding EMV field only if it is set in field 55

        try:
            emvData = request.getBit(55)
            if emvData:
                tempList.append(55)
        except:
            pass

        response = ISOBuilder.buildBitMaps(request,response,tempList,forceError)
        print "410 message response : " + response.getNetworkISO()
        return response



'''
concrete class implementation for 0420 response
'''
class ResponseGenerator0420(ResponseGeneratorFactory):
    def __init__(self):
        #mandatory fields to build
        self.FieldsToBuild = [2,3,4,7,11,12,13,14,15,18,19,32,37,38,39,41,49,60]

    def getCustomISOObject(self):
        temp = ISO8583()
        # change the protocol - this is for customization
        temp.redefineBit(18, '18', 'Merchant Category Code', 'N', 4, 'n')
        temp.redefineBit(53,'53','Security related control information','LL',76,'n')
        temp.redefineBit(60, '60', 'Additional Data', 'LLL', 999, 'ans')
        temp.redefineBit(62, '62', 'Custom Data', 'ANS', 26, 'ans')
        return temp

    #overloaded function
    def generateResponse(self, request, forceError = None):
        if not isinstance(request,ISO8583):
            request = self.getCustomISOObject()

        tempList = list(self.FieldsToBuild)
        # create a dummy response now
        response = self.getCustomISOObject()
        response.setMTI("0430")

        # adding fields based on card
        cardNumber = request.getBit(2)
        cardType = utility.findCardType(cardNumber[2:])
        if cardType == "V":
            tempList.extend([44,62])
        else:
            pass

        # adding EMV field only if it is set in field 55

        try:
            emvData = request.getBit(55)
            if emvData:
                tempList.append(55)
        except:
            pass

        response = ISOBuilder.buildBitMaps(request,response,tempList,forceError)
        print "430 message response : " + response.getNetworkISO()
        return response







