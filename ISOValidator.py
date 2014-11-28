import time
import logging
from Config import *

LOGGER = logging.getLogger(APPNAME)

'''
These are a collection of validation functions for all ISO8583 bitmaps
No need to validate the size as its already done inside the ISO8583 class
'''
#Validation sub routines
#PAN
def validateBitMap2(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid Primary Account Number")
    return


#Processing code
def validateBitMap3(bitvalue):
    #hardcoded processing code
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid processing code")
    return


#Transaction Amount
def validateBitMap4(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid Transaction Amount")
    return


#We do not have to check these bitmap
def validateBitMap5(bitvalue):
    return


def validateBitMap6(bitvalue):
    return


#Transmission date and time
def validateBitMap7(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid transmission date and time")

    # will raise an exception if the format is not correct
    time.strptime(bitvalue,'%m%d%H%M%S')
    return


#oh wow we do not have to check these bitmap
def validateBitMap8(bitvalue):
    return


def validateBitMap9(bitvalue):
    return


def validateBitMap10(bitvalue):
    return


#System Trace number
def validateBitMap11(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid System Trace number")
    return


#Local Transaction time
def validateBitMap12(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid Local Transaction time")

    # will raise an exception if the data is not correct
    time.strptime(bitvalue,'%H%M%S')
    return


#Local Transaction Date
def validateBitMap13(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid Local transaction Date")

    # will raise an exception if the date is not correct
    time.strptime(bitvalue,'%m%d')
    return


#Card Expiry Date
def validateBitMap14(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid Expiry Date")

    # will raise an exception for invalid date
    time.strptime(bitvalue,'%y%m')
    return


# settlement date
def validateBitMap15(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid settlement date")

    # will raise an exception for invalid date
    time.strptime(bitvalue,'%m%d')
    return


def validateBitMap16(bitvalue):
    return


def validateBitMap17(bitvalue):
    return


#Merchant category code
def validateBitMap18(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid MCC")
    return


#Country Code
def validateBitMap19(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid Country code")
    return


def validateBitMap20(bitvalue):
    return


def validateBitMap21(bitvalue):
    return


#Point of Service Entry Mode
def validateBitMap22(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid POS Entry Mode")
    return


def validateBitMap23(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid POS Card sequence number")
    return


def validateBitMap24(bitvalue):
    return


#POS Condition code
def validateBitMap25(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid POS Condition code")
    return

# POS Pin capture code
def validateBitMap26(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid POS capture code")
    return


def validateBitMap27(bitvalue):
    return


def validateBitMap28(bitvalue):
    return


def validateBitMap29(bitvalue):
    return


def validateBitMap30(bitvalue):
    return


def validateBitMap31(bitvalue):
    return


#Bin number, Acquiring institution id code
def validateBitMap32(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid Bin Number")
    return


def validateBitMap33(bitvalue):
    return


def validateBitMap34(bitvalue):
    return


def validateBitMap35(bitvalue):
    return


def validateBitMap36(bitvalue):
    return


#Retreival reference number
def validateBitMap37(bitvalue):
    # should be alpha-numeric
    for c in str(bitvalue):
        if (c.isalnum() == False):
            raise TypeError("Invalid retrieval reference number")
    return


def validateBitMap38(bitvalue):
    # should be alpha-numeric
    for c in str(bitvalue):
        if (c.isalnum() == False):
            raise TypeError("Invalid Bitmap 38")
    return


def validateBitMap39(bitvalue):
    # should be alpha-numeric
    for c in str(bitvalue):
        if (c.isalnum() == False):
            raise TypeError("Invalid Bitmap_39")
    return


def validateBitMap40(bitvalue):
    return

# terminal ID
def validateBitMap41(bitvalue):
    # nothing to validate other than length
    return


#Merchant Number
def validateBitMap42(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid Merchant Number")
    return


#Card Acceptor Name and Location
def validateBitMap43(bitvalue):
    # should be alpha-numeric
    return

# additional response data
def validateBitMap44(bitvalue):
    return

# track 1 data
def validateBitMap45(bitvalue):
    return


def validateBitMap46(bitvalue):
    return


def validateBitMap47(bitvalue):
    return

#CVV2
def validateBitMap48(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isalnum() == False):
            if (c != ' '):
                raise TypeError("Invalid CVV2")
    return

# TXN currency code
def validateBitMap49(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid Txn Currency Code")
    return


def validateBitMap50(bitvalue):
    return


def validateBitMap51(bitvalue):
    return


def validateBitMap52(bitvalue):
    return


def validateBitMap53(bitvalue):
    return


def validateBitMap54(bitvalue):
    return


def validateBitMap55(bitvalue):
    return


def validateBitMap56(bitvalue):
    return


def validateBitMap57(bitvalue):
    return


def validateBitMap58(bitvalue):
    return


def validateBitMap59(bitvalue):
    return


#additional data
def validateBitMap60(bitvalue):
    return


def validateBitMap61(bitvalue):
    return


def validateBitMap62(bitvalue):
    return


def validateBitMap63(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid Reversal Reason Code")
    return


def validateBitMap64(bitvalue):
    return


def validateBitMap65(bitype, bitvalue):
    return


def validateBitMap66(bitvalue):
    return


def validateBitMap67(bitvalue):
    return


def validateBitMap68(bitvalue):
    return


def validateBitMap69(bitvalue):
    return


def validateBitMap90(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid Bitmap 90")
    return


def validateBitMap95(bitvalue):
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise TypeError("Invalid Bitmap 95")
    return

class validatorMap:
    def __init__(self):
        self.validatorFunc = {  "2":validateBitMap2,
                                "3":validateBitMap3,
                                "4":validateBitMap4,
                                "5":validateBitMap5,
                                "6":validateBitMap6,
                                "7":validateBitMap7,
                                "8":validateBitMap8,
                                "9":validateBitMap9,
                                "10":validateBitMap10,
                                "11":validateBitMap11,
                                "12":validateBitMap12,
                                "13":validateBitMap13,
                                "14":validateBitMap14,
                                "15":validateBitMap15,
                                "16":validateBitMap16,
                                "17":validateBitMap17,
                                "18":validateBitMap18,
                                "19":validateBitMap19,
                                "20":validateBitMap20,
                                "21":validateBitMap21,
                                "22":validateBitMap22,
                                "23":validateBitMap23,
                                "24":validateBitMap24,
                                "25":validateBitMap25,
                                "26":validateBitMap26,
                                "27":validateBitMap27,
                                "28":validateBitMap28,
                                "29":validateBitMap29,
                                "30":validateBitMap30,
                                "31":validateBitMap31,
                                "32":validateBitMap32,
                                "33":validateBitMap33,
                                "34":validateBitMap34,
                                "35":validateBitMap35,
                                "36":validateBitMap36,
                                "37":validateBitMap37,
                                "38":validateBitMap38,
                                "39":validateBitMap39,
                                "40":validateBitMap40,
                                "41":validateBitMap41,
                                "42":validateBitMap42,
                                "43":validateBitMap43,
                                "44":validateBitMap44,
                                "45":validateBitMap45,
                                "46":validateBitMap46,
                                "47":validateBitMap47,
                                "48":validateBitMap48,
                                "49":validateBitMap49,
                                "50":validateBitMap50,
                                "51":validateBitMap51,
                                "52":validateBitMap52,
                                "53":validateBitMap53,
                                "54":validateBitMap54,
                                "55":validateBitMap55,
                                "56":validateBitMap56,
                                "57":validateBitMap57,
                                "58":validateBitMap58,
                                "59":validateBitMap59,
                                "60":validateBitMap60,
                                "61":validateBitMap61,
                                "62":validateBitMap62,
                                "63":validateBitMap63,
                                "64":validateBitMap64,
                                "65":validateBitMap65,
                                "66":validateBitMap66,
                                "67":validateBitMap67,
                                "68":validateBitMap68,
                                "69":validateBitMap69,
                                "90":validateBitMap90,
                                "95":validateBitMap95
                                }


# function to check if the required list of bitmaps are correct in the ISO message
def validateBitMaps(isoMsg,bitmapList):
    map = validatorMap()
    if ( (isoMsg is None) or (bitmapList is None)):
        return False
    else:
        for bitmap in bitmapList:
            print "validating bitmap %d" % bitmap
            try:
                bitval = isoMsg.getBit(bitmap)
                if bitval is None:
                    print "Error in retrieving bitmap %d" % bitmap
                    return False
                map.validatorFunc[str(bitmap)](bitval)
                LOGGER.log(logging.DEBUG, "Validation of bitmap %d passed for value %s" % (bitmap, str(bitval)))
            except TypeError,e:
                LOGGER.log(logging.FATAL, "Validation failed for bitmap %d" % bitmap)
                print "Validate failed for Bitmap : %d - %s" % (bitmap,e)
                return False
            except:
                LOGGER.log(logging.FATAL, "Mandatory Bitmap %d not present in ISO message" % bitmap)
                print "Bitmap Not set for Bit : %d" % bitmap
                return False
    return True

