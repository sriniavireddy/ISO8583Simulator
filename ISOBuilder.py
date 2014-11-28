from Config import *
import logging
import sys
import utility

LOGGER = logging.getLogger(APPNAME)


class ErrorTypeToForce:
    NO_DATA = 1
    WRONG_DATA = 2
    FORCE_ERROR_CODE = 3  # used only for bitmap 39
    NO_ERROR = 4


def addBitMap(bitmap, isoRequestMsg, isoResponseMsg, forceValue, defaultValue):
    respVal = None
    if forceValue is not None:
        LOGGER.log(logging.INFO, "forcing value for bitmap %d " % bitmap)
        isoResponseMsg.setBit(bitmap, forceValue)
    elif isoRequestMsg is None:
        isoResponseMsg.setBit(bitmap, defaultValue)
    else:
        try:
            respValType = isoRequestMsg.getBitType(bitmap)
            respVal = isoRequestMsg.getBit(bitmap)
            if respValType == "LL":
                respVal = respVal[2:]
            elif respValType == "LLL":
                respVal = respVal[3:]
            else:
                pass

            isoResponseMsg.setBit(bitmap, respVal)
            LOGGER.log(logging.DEBUG, "Set the same value in req to resp for bitmap : %d " % bitmap)
        except:
            print str(sys.exc_info()) + str(respVal)
            LOGGER.log(logging.INFO, "No value is available in req for bitmap %d, setting default value" % bitmap)
            isoResponseMsg.setBit(bitmap, defaultValue)
    return isoResponseMsg


def getTypeofErrorToForce(amount):
    amount = int(amount)
    #if (amount >= 150000 and amount < 150200):
    if (amount >= 10000 and amount < 10200):
        # don't send bitmaps
        LOGGER.log(logging.INFO, "Forcing No data error")
        #return (ErrorTypeToForce.NO_DATA, (amount - 150000))
        return (ErrorTypeToForce.NO_DATA, (amount - 10000))
    elif (amount >= 150200 and amount < 150400):
        # send wrong data in the bitmap
        LOGGER.log(logging.INFO, "Forcing Wrong data error")
        return (ErrorTypeToForce.WRONG_DATA, (amount - 150200))
    elif (amount >= 150400 and amount < 150471):
        # force an error code in response code
        LOGGER.log(logging.INFO, "Forcing Error code")
        return (ErrorTypeToForce.FORCE_ERROR_CODE, (amount - 150400))
    else:
        # no need to do any error
        print "No error is forced"
        return (ErrorTypeToForce.NO_ERROR, 0)


# Add Primary Account Number to
def addBitMap2(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "123456A890B23456"
    return addBitMap(2, isoRequestMsg, isoResponseMsg, toForce, "1234567890123456")


# processing code
def addBitMap3(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "12345A"
    return addBitMap(3, isoRequestMsg, isoResponseMsg, toForce, "280000")


# transaction Amount
def addBitMap4(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "123456A890B2"
    return addBitMap(4, isoRequestMsg, isoResponseMsg, toForce, "000000001000")


# reconciliation amount - Current client cannot handle this
def addBitMap5(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "123456A890B2"
    return addBitMap(5, isoRequestMsg, isoResponseMsg, toForce, "000000001000")
    '''
    return isoResponseMsg


# cardholder billing amount
def addBitMap6(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "123456A890B2"
    return addBitMap(6, isoRequestMsg, isoResponseMsg, toForce, "000000001000")
    '''
    return isoResponseMsg


# Transmission date and time
def addBitMap7(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "123456A890"
    return addBitMap(7, isoRequestMsg, isoResponseMsg, toForce, "0625060000")


# cardholder billing fee
def addBitMap8(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "123456A8"
    return addBitMap(8, isoRequestMsg, isoResponseMsg, toForce, "00001000")
    '''
    return isoResponseMsg


# recon conversion rate
def addBitMap9(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "123456A8"
    return addBitMap(9, isoRequestMsg, isoResponseMsg, toForce, "00001000")
    '''
    return isoResponseMsg


# cardholder billing conversion rate
def addBitMap10(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "123456A8"
    return addBitMap(10, isoRequestMsg, isoResponseMsg, toForce, "00001000")
    '''
    return isoResponseMsg


# system trace number
def addBitMap11(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "A890B2"
    return addBitMap(11, isoRequestMsg, isoResponseMsg, toForce, "123456")


# local transaction time
def addBitMap12(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "A890B2"
    return addBitMap(12, isoRequestMsg, isoResponseMsg, toForce, "000100")


# local transaction Date
def addBitMap13(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "6A89"
    return addBitMap(13, isoRequestMsg, isoResponseMsg, toForce, "0625")


# card Expiration Date
def addBitMap14(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "6A89"
    return addBitMap(14, isoRequestMsg, isoResponseMsg, toForce, "1712")


# settlement date
def addBitMap15(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "6A89"
    return addBitMap(15, isoRequestMsg, isoResponseMsg, toForce, "0625")


# conversion Date
def addBitMap16(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "6A89"
    return addBitMap(16, isoRequestMsg, isoResponseMsg, toForce, "0625")
    '''
    return isoResponseMsg


# capture date
def addBitMap17(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "6A89"
    return addBitMap(17, isoRequestMsg, isoResponseMsg, toForce, "0625")
    '''
    return isoResponseMsg


# MCC Code
def addBitMap18(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "6A89"
    return addBitMap(18, isoRequestMsg, isoResponseMsg, toForce, "8999")


# Acquirer country code
def addBitMap19(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "6A8"
    return addBitMap(19, isoRequestMsg, isoResponseMsg, toForce, "840")

# country code PAN
def addBitMap20(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    defaultValue = "0625"
    return addBitMap(20,isoRequestMsg, isoResponseMsg, forceValue, defaultValue)
    '''
    return isoResponseMsg


def addBitMap21(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    defaultValue = "0625"
    return addBitMap(21,isoRequestMsg, isoResponseMsg, forceValue, defaultValue)
    '''
    return isoResponseMsg

# POS Entry mode --check
def addBitMap22(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "6A8"
    return addBitMap(22,isoRequestMsg, isoResponseMsg, toForce, "642")

# Card Sequence Number --check
def addBitMap23(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "6A8"
    return addBitMap(23,isoRequestMsg, isoResponseMsg, toForce, "642")


def addBitMap24(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    defaultValue = "0625"
    return addBitMap(24,isoRequestMsg, isoResponseMsg, forceValue, defaultValue)
    '''
    return isoResponseMsg

# POS Condition code --check
def addBitMap25(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "6A"
    return addBitMap(25,isoRequestMsg, isoResponseMsg, toForce, "25")

# POS - PIN capture code
def addBitMap26(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "6A"
    return addBitMap(26,isoRequestMsg, isoResponseMsg, toForce, "25")
    '''
    return isoResponseMsg


def addBitMap27(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, forceValue, defaultValue)
    '''
    return isoResponseMsg


def addBitMap28(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, forceValue, defaultValue)
    '''
    return isoResponseMsg


def addBitMap29(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, forceValue, defaultValue)
    '''
    return isoResponseMsg


def addBitMap30(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, forceValue, defaultValue)
    '''
    return isoResponseMsg


def addBitMap31(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, forceValue, defaultValue)
    '''
    return isoResponseMsg

# acquirer institution id
def addBitMap32(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "0000AB"
    return addBitMap(32, isoRequestMsg, isoResponseMsg, toForce, "000031")



def addBitMap33(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, forceValue, defaultValue)
    '''
    return isoResponseMsg


# Extended PAN, Use this with caution - required only for ELV Transactions
def addBitMap34(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    return addBitMap(34, isoRequestMsg, isoResponseMsg, None, "06250000")
    '''
    return isoResponseMsg


# track2 Data
def addBitMap35(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    return addBitMap(35, isoRequestMsg, isoResponseMsg, None, "track_2_buffer_for_test")
    '''
    return isoResponseMsg

# track3 data
def addBitMap36(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    return addBitMap(36, isoRequestMsg, isoResponseMsg, None, "track_3_buffer_for_test")
    '''
    return isoResponseMsg


# retrieval reference number --have to add
def addBitMap37(isoRequestMsg, isoResponseMsg, forceValue):
    # dont know the Default value or the error value --fixed
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "XXXX14000026"
    return addBitMap(37, isoRequestMsg, isoResponseMsg, toForce, "042514000026")


# Authorization code
def addBitMap38(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "      "
    return addBitMap(38, isoRequestMsg, isoResponseMsg, toForce, "000000")


# Response code
def addBitMap39(isoRequestMsg, isoResponseMsg, forceValue):
    ErrorCodeToForce = None
    if forceValue == ErrorTypeToForce.FORCE_ERROR_CODE:
        # force value needs to be changed in case of amount greater than 150300
        print "about to set error code"
        ErrorCodes = ["00", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "17", "19",
                      "20", "21", "22", "23", "24", "30", "34", "39", "41", "42", "43", "44", "51", "54", "55", "57",
                      "58", "59", "61", "62", "63", "65", "66", "67", "68", "75", "76", "77", "78", "79", "80", "81",
                      "82", "83", "84", "85", "86", "87", "88", "89", "91", "92", "93", "94", "95", "96", "97", "98",
                      "99", "N3", "N4", "N7", "R0", "R1", "R3"]
        try:
            amount = isoRequestMsg.getBit(4)
            amount = int(amount)
            print "Amount used for forcing error code : %d" % amount
            if amount >= 150400 and amount < 150471:
                ErrorCodeToForce = ErrorCodes[(amount - 150400)]
                print "Error code to force is %s" % ErrorCodeToForce
        except:
            # nothing to do, no transaction amount in request
            pass
    return addBitMap(39, isoRequestMsg, isoResponseMsg, ErrorCodeToForce, "00")


# service code
def addBitMap40(isoRequestMsg, isoResponseMsg, forceValue):
    '''
    # - Current Client cannot handle this
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "6A8"
    return addBitMap(40, isoRequestMsg, isoResponseMsg, toForce, "062")
    '''
    return isoResponseMsg


# terminal ID
def addBitMap41(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "XYZ3456A8"
    return addBitMap(41, isoRequestMsg, isoResponseMsg, toForce, "12345678")


# card acceptor identification code --check
def addBitMap42(isoRequestMsg, isoResponseMsg, forceValue):
    # dont know the default value or the error value
    return addBitMap(42, isoRequestMsg, isoResponseMsg, None, "ABCD1234EFG0625")


# card acceptor name/ location --check
def addBitMap43(isoRequestMsg, isoResponseMsg, forceValue):
    # dont know the default value or the error value
    return addBitMap(43, isoRequestMsg, isoResponseMsg, None, "Card Holder Name")


# additional response data
def addBitMap44(isoRequestMsg, isoResponseMsg, forceValue):
    # the default value or forced Value should depend on the card type
    '''
    Visa - stars with 4
    Master - 5
    current support is only for these two cards
    '''

    #get the card type
    cardType = None
    toForce = None
    defaultValue = None
    bitMap = 44
    try:
        cardNumber = isoRequestMsg.getBit(2)
        cardType = utility.findCardType(cardNumber[2:])
    except:
        # could not get a card type defaulting to Visa
        cardType = "V"

    # set the response based on the card type
    if cardType == "M":
        if forceValue == ErrorTypeToForce.WRONG_DATA:
            # 44.1 is set empty
            toForce = " MDC12345678912320145"
            isoResponseMsg.setBit(bitMap,toForce)
            LOGGER.log(logging.DEBUG, "Set the corrupt value in resp for bitmap : %d %s " %(bitMap,toForce))
        else:
            # 2 digit length (max 38)
            # subfield 44.1 fixed length 1 (CV2 value - either space or M etc)
            # subfield 44.2 fixed length 12 (banknet ref value)
            # subfield 44.3 variable length ..25 (additional data)
            respVal = "MMDC12345678912320145"
            isoResponseMsg.setBit(bitMap,respVal)
            LOGGER.log(logging.DEBUG, "Set the correct value in resp for bitmap : %d %s " %(bitMap,respVal))
    elif cardType == "V":
        if forceValue == ErrorTypeToForce.WRONG_DATA:
            # 44.1 is set empty
            toForce = " D        M   2"
            isoResponseMsg.setBit(bitMap,toForce)
            LOGGER.log(logging.DEBUG, "Set the corrupt value in resp for bitmap : %d %s " %(bitMap,toForce))
        else:
            respVal = "5D        M   2"
            isoResponseMsg.setBit(bitMap,respVal)
            LOGGER.log(logging.DEBUG, "Set the correct value in resp for bitmap : %d %s " %(bitMap,respVal))
    else:
        pass

    return isoResponseMsg


# track1 data
def addBitMap45(isoRequestMsg, isoResponseMsg, forceValue):
    return addBitMap(45, isoRequestMsg, isoResponseMsg, None, "track_1_test_data")


'''
def addBitMap46(isoRequestMsg, isoResponseMsg, forceValue):
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, "123456A890B23456" if forceValue == ErrorTypeToForce.WRONG_DATA else None, defaultValue)


def addBitMap47(isoRequestMsg, isoResponseMsg, forceValue):
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, "123456A890B23456" if forceValue == ErrorTypeToForce.WRONG_DATA else None, defaultValue)


def addBitMap48(isoRequestMsg, isoResponseMsg, forceValue):
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, "123456A890B23456" if forceValue == ErrorTypeToForce.WRONG_DATA else None, defaultValue)
'''

# txn currency code
def addBitMap49(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "56A"
    return addBitMap(49, isoRequestMsg, isoResponseMsg, toForce, "080")


'''
def addBitMap50(isoRequestMsg, isoResponseMsg, forceValue):
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, "123456A890B23456" if forceValue == ErrorTypeToForce.WRONG_DATA else None, defaultValue)


def addBitMap51(isoRequestMsg, isoResponseMsg, forceValue):
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, "123456A890B23456" if forceValue == ErrorTypeToForce.WRONG_DATA else None, defaultValue)


def addBitMap52(isoRequestMsg, isoResponseMsg, forceValue):
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, "123456A890B23456" if forceValue == ErrorTypeToForce.WRONG_DATA else None, defaultValue)
'''

# security control information --check
def addBitMap53(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "123456A890B23456"
    return addBitMap(53, isoRequestMsg, isoResponseMsg, toForce, 123456789012345678)


# additional Amounts --check
def addBitMap54(isoRequestMsg, isoResponseMsg, forceValue):
    return addBitMap(54, isoRequestMsg, isoResponseMsg, None, "Dummy Data for additional amounts")


# EMV Data
def addBitMap55(isoRequestMsg, isoResponseMsg, forceValue):
    # get a sample EMV data and then update the default value -- done
    toForce = None
    bitMap = 55
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "82023C008407A0000000031010950508000080009A031207189C01005F2A0208269F02060000000001009F03060000000000009F0902008C9F100D06120A03A400200541030000009F1A0208269F1E0830333030303030339F260826DE1C6576C79DEF9F2701809F3303E0B8C89F34034103029F3501229F360200FB9F3704B753FA56"
        isoResponseMsg.setBit(bitMap,toForce)
        LOGGER.log(logging.DEBUG, "Set the corrupt value in resp for bitmap : %d %s " %(bitMap,toForce))
    else:
        respVal = "82023C008407A0000000031010950508000080009A031207189C01005F2A0208269F02060000000001009F03060000000000009F0902008C9F100D06120A03A400200541030000009F1A0208269F1E0830333030303030339F260826DE1C6576C79DEF9F2701809F3303E0B8C89F34034103029F3501229F360200FB9F3704B753FA568A020000"
        isoResponseMsg.setBit(bitMap,respVal)
        LOGGER.log(logging.DEBUG, "Set the correct value in resp for bitmap : %d %s " %(bitMap,respVal))
    return isoResponseMsg


'''
def addBitMap56(isoRequestMsg, isoResponseMsg, forceValue):
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, "123456A890B23456" if forceValue == ErrorTypeToForce.WRONG_DATA else None, defaultValue)


def addBitMap57(isoRequestMsg, isoResponseMsg, forceValue):
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, "123456A890B23456" if forceValue == ErrorTypeToForce.WRONG_DATA else None, defaultValue)


def addBitMap58(isoRequestMsg, isoResponseMsg, forceValue):
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, "123456A890B23456" if forceValue == ErrorTypeToForce.WRONG_DATA else None, defaultValue)


def addBitMap59(isoRequestMsg, isoResponseMsg, forceValue):
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, "123456A890B23456" if forceValue == ErrorTypeToForce.WRONG_DATA else None, defaultValue)
'''

# additional data
def addBitMap60(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    bitMap = 60
    if forceValue == ErrorTypeToForce.WRONG_DATA:
	# This is to simulate AVS validation failure where CVV is present and AVS is missing
        toForce = "00432AB"
        isoResponseMsg.setBit(bitMap,toForce)
        LOGGER.log(logging.DEBUG, "Set the corrupt value in resp for bitmap : %d %s " %(bitMap,toForce))
    else:
        respVal = '00832AB5201'
        isoResponseMsg.setBit(bitMap,respVal)
        LOGGER.log(logging.DEBUG, "Set the correct value in resp for bitmap : %d %s " %(bitMap,respVal))
    return isoResponseMsg


# custom data --check
def addBitMap61(isoRequestMsg, isoResponseMsg, forceValue):
    return addBitMap(61, isoRequestMsg, isoResponseMsg, None, "custom data sent in iso message")


# custom payment service data (for Visa only)
def addBitMap62(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    bitMap = 62
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = ' 002221123454443     00'
        isoResponseMsg.setBit(bitMap,toForce)
        LOGGER.log(logging.DEBUG, "Set the corrupt value in resp for bitmap : %d %s " % bitMap,toForce)
    else:
        respVal = ' 002221123454443     00 H '
        isoResponseMsg.setBit(bitMap,respVal)
        LOGGER.log(logging.DEBUG, "Set the correct value in resp for bitmap : %d %s " %(bitMap,respVal))
    return isoResponseMsg


'''
def addBitMap63(isoRequestMsg, isoResponseMsg, forceValue):
    defaultValue = "0625"
    return addBitMap(2,isoRequestMsg, isoResponseMsg, "123456A890B23456" if forceValue == ErrorTypeToForce.WRONG_DATA else None, defaultValue)
'''


def addBitMap64(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "DUMMY_WRONGVALUE"
    return addBitMap(64, isoRequestMsg, isoResponseMsg, toForce, "1234567890123456")


def addBitMap102(isoRequestMsg, isoResponseMsg, forceValue):
    return addBitMap(102, isoRequestMsg, isoResponseMsg, None, "Dummy Data")


def addBitMap128(isoRequestMsg, isoResponseMsg, forceValue):
    toForce = None
    if forceValue == ErrorTypeToForce.WRONG_DATA:
        toForce = "DUMMY_WRONGVALUE"
    return addBitMap(128, isoRequestMsg, isoResponseMsg, toForce, "1234567890123456")


class RespGeneratorMap:
    def __init__(self):
        self.generatorMap = {"2": addBitMap2,
                             "3": addBitMap3,
                             "4": addBitMap4,
                             "5": addBitMap5,
                             "6": addBitMap6,
                             "7": addBitMap7,
                             "8": addBitMap8,
                             "9": addBitMap9,
                             "10": addBitMap10,
                             "11": addBitMap11,
                             "12": addBitMap12,
                             "13": addBitMap13,
                             "14": addBitMap14,
                             "15": addBitMap15,
                             "16": addBitMap16,
                             "17": addBitMap17,
                             "18": addBitMap18,
                             "19": addBitMap19,
                             "32": addBitMap32,
                             "34": addBitMap34,
                             "35": addBitMap35,
                             "36": addBitMap36,
                             "37": addBitMap37,
                             "38": addBitMap38,
                             "39": addBitMap39,
                             "40": addBitMap40,
                             "41": addBitMap41,
                             "42": addBitMap42,
                             "43": addBitMap43,
                             "44": addBitMap44,
                             "45": addBitMap45,
                             "49": addBitMap49,
                             "53": addBitMap53,
                             "54": addBitMap54,
                             "55": addBitMap55,
                             "60": addBitMap60,
                             "61": addBitMap61,
                             "62": addBitMap62,
                             "64": addBitMap64,
                             "102": addBitMap102,
                             "128": addBitMap128
        }


# function to build the response with requested bitmaps
def buildBitMaps(isoReqMsg, isoRespMsg, bitMapList, forceError):
    map = RespGeneratorMap()
    if ( isoReqMsg is None or bitMapList is None):
        return isoRespMsg
    else:
        # check the error type to force
        errorType, value = getTypeofErrorToForce(isoReqMsg.getBit(4))
        if errorType == ErrorTypeToForce.NO_DATA:
            LOGGER.log(logging.DEBUG, "Removing bitmap %d from the list of Bitmaps to be built" % value)
            if value in bitMapList:
                bitMapList.remove(value)
        elif errorType == ErrorTypeToForce.FORCE_ERROR_CODE:
            value = 39
            # removin field 07 to simulate missing field when field 39 is forced
            if FORCE_CORRUPT_VALUE_ON_SETTING_FIELD39 == True:
                bitMapList.remove(7)
        elif errorType == ErrorTypeToForce.NO_ERROR:
            value = -1

        for bitmap in bitMapList:
            LOGGER.log(logging.DEBUG, "building bit map %d " % bitmap)
            if bitmap == value:
                LOGGER.log(logging.INFO, "forcing error for bitmap %d" % bitmap)
                isoRespMsg = map.generatorMap[str(bitmap)](isoReqMsg, isoRespMsg, errorType)
            else:
                print bitmap
                isoRespMsg = map.generatorMap[str(bitmap)](isoReqMsg, isoRespMsg, None)

        if forceError is not None:
            LOGGER.log(logging.WARNING, "Forcing Error code to %s " % forceError)
            isoRespMsg.setBit(39, forceError)

    return isoRespMsg
