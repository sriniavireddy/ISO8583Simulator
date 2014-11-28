"""

(C) Copyright 2009 Debanjan Basu(debanjan.basu@gmail.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

# Administer logging
import logging
import time

logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)


def entry_log(message):
    logger.info(message)
    return


def exit_log(message):
    logger.info(message)
    return


import socket, subprocess, re
#Utility subroutines
def get_ipv4_address():
    """
    Returns IP address(es) of current machine.
    :return:
    """
    #p = subprocess.Popen(["/sbin/ifconfig"], stdout=subprocess.PIPE)
    #ifc_resp = p.communicate()
    #patt = re.compile(r'inet\s*\w*\S*:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    #resp = patt.findall(ifc_resp[0])
    #print resp
    #info = "The ip used is : " + str(resp[0])
    #logger.info(info)
    #return resp[0]
    return "127.0.0.1"


#Validation sub routines
def validate_BM_1(bitype, bitvalue):
    entry_log(validate_BM_1.__name__)
    info = "The bitype is " + str(bitype) + "The bitvalue : " + str(bitvalue)
    raise InvalidIso8583, "Invalid Bitmap"
    exit_log(validate_BM_1.__name__)
    return


#PAN
def validate_BM_2(bitype, bitvalue):
    entry_log(validate_BM_2.__name__)
    info = "The Account number is" + str(bitvalue)
    logger.info(info)
    if (bitype != '2'):
        logger.info("Invalid bitype")
        raise InvalidIso8583, "Invalid Bitmap_2"
    #check length
    if (len(str(bitvalue)) > 19 or len(str(bitvalue)) == 0 ):
        raise InvalidIso8583, "Invalid Bitmap_2"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_2"
    exit_log(validate_BM_2.__name__)
    return


#Processing code
def validate_BM_3(bitype, bitvalue):
    #hardcoded processing code
    if (str(bitvalue) != "280000"):
        raise InvalidIso8583, "Invalid Bitmap_3"
    return


#Transaction Amount
def validate_BM_4(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) != 12):
        raise InvalidIso8583, "Invalid Bitmap_4"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_4"

    # to pause the thread for 20 seconds if BM 4 is 000000009999
    #if pack.getBit(4) == '000000001000':
        #time.sleep(20)
    return


#We do not have to check these bitmap
def validate_BM_5(bitype, bitvalue):
    return


def validate_BM_6(bitype, bitvalue):
    return


#Transmission date and time
def validate_BM_7(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) != 10):
        raise InvalidIso8583, "Invalid Bitmap_7"
    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_7"
    return


#oh wow we do not have to check these bitmap
def validate_BM_8(bitype, bitvalue):
    return


def validate_BM_9(bitype, bitvalue):
    return


def validate_BM_10(bitype, bitvalue):
    return


#System Trace number
def validate_BM_11(bitype, bitvalue):
    entry_log(validate_BM_11.__name__)
    info = "The trace number" + str(bitvalue)
    #check length
    if (len(str(bitvalue)) != 6):
        raise InvalidIso8583, "Invalid Bitmap_11"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_11"
    exit_log(validate_BM_11.__name__)
    return


#Local Transaction time
def validate_BM_12(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) != 6):
        raise InvalidIso8583, "Invalid Bitmap_12"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_12"
    return


#Local Transaction Date
def validate_BM_13(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) != 4):
        raise InvalidIso8583, "Invalid Bitmap_13"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_13"
    return


#Card Expiry Date
def validate_BM_14(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) != 4):
        raise InvalidIso8583, "Invalid Bitmap_14"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_14"
    return


def validate_BM_15(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) != 4):
        raise InvalidIso8583, "Invalid Bitmap_15"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_15"
    return


def validate_BM_16(bitype, bitvalue):
    return


def validate_BM_17(bitype, bitvalue):
    return


#Merchant category code
def validate_BM_18(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) != 4):
        raise InvalidIso8583, "Invalid Bitmap_18"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_18"
    return


#Country Code
def validate_BM_19(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) != 3):
        raise InvalidIso8583, "Invalid Bitmap_19"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_19"
    return


def validate_BM_20(bitype, bitvalue):
    return


def validate_BM_21(bitype, bitvalue):
    return


#Point of Service Entry Mode
def validate_BM_22(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) != 3):
        raise InvalidIso8583, "Invalid Bitmap_22"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_22"
    return


def validate_BM_23(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) != 3):
        raise InvalidIso8583, "Invalid Bitmap_23"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_23"
    return


def validate_BM_24(bitype, bitvalue):
    return


#POS Condition code
def validate_BM_25(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) != 2):
        raise InvalidIso8583, "Invalid Bitmap_25"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_25"
    return


def validate_BM_26(bitype, bitvalue):
    return


def validate_BM_27(bitype, bitvalue):
    return


def validate_BM_28(bitype, bitvalue):
    return


def validate_BM_29(bitype, bitvalue):
    return


def validate_BM_30(bitype, bitvalue):
    return


def validate_BM_31(bitype, bitvalue):
    return


#Bin number, Acquiring institution id code
def validate_BM_32(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) <= 0 or len(str(bitvalue)) > 10):
        raise InvalidIso8583, "Invalid Bitmap_32"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_32"
    return


def validate_BM_33(bitype, bitvalue):
    return


def validate_BM_34(bitype, bitvalue):
    return


def validate_BM_35(bitype, bitvalue):
    return


def validate_BM_36(bitype, bitvalue):
    return


#Retreival reference number
def validate_BM_37(bitype, bitvalue):
    if (len(str(bitvalue)) != 12):
        raise InvalidIso8583, "Invalid Bitmap_37"
    # should be alpha-numeric
    for c in str(bitvalue):
        if (c.isalnum() == False):
            raise InvalidIso8583, "Invalid Bitmap_37"
    return


def validate_BM_38(bitype, bitvalue):
    if (len(str(bitvalue)) != 6):
        raise InvalidIso8583, "Invalid Bitmap_38"
    # should be alpha-numeric
    for c in str(bitvalue):
        if (c.isalnum() == False):
            raise InvalidIso8583, "Invalid Bitmap_38"
    return


def validate_BM_39(bitype, bitvalue):
    if (len(str(bitvalue)) != 2):
        raise InvalidIso8583, "Invalid Bitmap_39"
    # should be alpha-numeric
    for c in str(bitvalue):
        if (c.isalnum() == False):
            raise InvalidIso8583, "Invalid Bitmap_39"
    return


def validate_BM_40(bitype, bitvalue):
    return


def validate_BM_41(bitype, bitvalue):
    if (str(bitvalue) != "00000001"):
        raise InvalidIso8583, "Invalid Bitmap_41"
    return


#Merchant Number
def validate_BM_42(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) != 15):
        raise InvalidIso8583, "Invalid Bitmap_42"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_42"
    return


#Card Acceptor Name and Location
def validate_BM_43(bitype, bitvalue):
    if (len(str(bitvalue)) > 40 or len(str(bitvalue)) == 0):
        raise InvalidIso8583, "Invalid Bitmap_43"
    # should be alpha-numeric
    for c in str(bitvalue):
        if (c.isalnum() == False):
            if (c != ' '):
                raise InvalidIso8583, "Invalid Bitmap_43"
    return


def validate_BM_44(bitype, bitvalue):
    return


def validate_BM_45(bitype, bitvalue):
    return


def validate_BM_46(bitype, bitvalue):
    return


def validate_BM_47(bitype, bitvalue):
    return


def validate_BM_48(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) <= 0 or len(str(bitvalue)) > 999):
        raise InvalidIso8583, "Invalid Bitmap_48"

    # should be numeric
    for c in str(bitvalue):
        if (c.isalnum() == False):
            if (c != ' '):
                raise InvalidIso8583, "Invalid Bitmap_48"
    return


def validate_BM_49(bitype, bitvalue):
    if (len(str(bitvalue)) != 3):
        raise InvalidIso8583, "Invalid Bitmap_49"
    # should be alpha-numeric
    for c in str(bitvalue):
        if (c.isalpha() == True):
            raise InvalidIso8583, "Invalid Bitmap_49"
    return


def validate_BM_50(bitype, bitvalue):
    return


def validate_BM_51(bitype, bitvalue):
    return


def validate_BM_52(bitype, bitvalue):
    return


def validate_BM_53(bitype, bitvalue):
    return


def validate_BM_54(bitype, bitvalue):
    return


def validate_BM_55(bitype, bitvalue):
    return


def validate_BM_56(bitype, bitvalue):
    return


def validate_BM_57(bitype, bitvalue):
    return


def validate_BM_58(bitype, bitvalue):
    return


def validate_BM_59(bitype, bitvalue):
    return


#additional data
def validate_BM_60(bitype, bitvalue):
    return


def validate_BM_61(bitype, bitvalue):
    return


def validate_BM_62(bitype, bitvalue):
    return


def validate_BM_63(bitype, bitvalue):
    if (str(bitvalue) != "068"):
        raise InvalidIso8583, "Invalid Bitmap_63"
    return


def validate_BM_64(bitype, bitvalue):
    return


def validate_BM_65(bitype, bitvalue):
    return


def validate_BM_66(bitype, bitvalue):
    return


def validate_BM_67(bitype, bitvalue):
    return


def validate_BM_68(bitype, bitvalue):
    return


def validate_BM_69(bitype, bitvalue):
    return


def validate_BM_90(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) <= 0 or len(str(bitvalue)) > 42):
        raise InvalidIso8583, "Invalid Bitmap_90"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_90"
    return


def validate_BM_95(bitype, bitvalue):
    #check length
    if (len(str(bitvalue)) <= 0 or len(str(bitvalue)) > 12):
        raise InvalidIso8583, "Invalid Bitmap_95"

    # should be numeric
    for c in str(bitvalue):
        if (c.isdigit() == False):
            raise InvalidIso8583, "Invalid Bitmap_95"
    return


def validate_ISO8583_0200(bitmap, bitype, bitvalue):
    print "The bitmap is ", str(bitmap)
    print "The bit-type is ", str(bitype)
    print "The bitvalue is ", str(bitvalue)

    if (str(bitmap) == '2'):
        validate_BM_2(bitmap, bitvalue)
        return
    elif (str(bitmap) == '3'):
        validate_BM_3(bitmap, bitvalue)
        return
    elif (str(bitmap) == '4'):
        validate_BM_4(bitmap, bitvalue)
        return
    elif (str(bitmap) == '7'):
        validate_BM_7(bitmap, bitvalue)
        return
    elif (str(bitmap) == '11'):
        validate_BM_11(bitmap, bitvalue)
        return
    elif (str(bitmap) == '12'):
        validate_BM_12(bitmap, bitvalue)
        return
    elif (str(bitmap) == '13'):
        validate_BM_13(bitmap, bitvalue)
        return
    elif (str(bitmap) == '14'):
        validate_BM_14(bitmap, bitvalue)
        return
    elif (str(bitmap) == '18'):
        validate_BM_18(bitmap, bitvalue)
        return
    elif (str(bitmap) == '19'):
        validate_BM_19(bitmap, bitvalue)
        return
    elif (str(bitmap) == '22'):
        validate_BM_22(bitmap, bitvalue)
        return
    elif (str(bitmap) == '25'):
        validate_BM_25(bitmap, bitvalue)
        return
    elif (str(bitmap) == '32'):
        validate_BM_32(bitmap, bitvalue)
        return
    elif (str(bitmap) == '37'):
        validate_BM_37(bitmap, bitvalue)
        return
    elif (str(bitmap) == '41'):
        validate_BM_41(bitmap, bitvalue)
        return
    elif (str(bitmap) == '42'):
        validate_BM_42(bitmap, bitvalue)
        return
    elif (str(bitmap) == '43'):
        validate_BM_43(bitmap, bitvalue)
        return
    elif (str(bitmap) == '48'):
        validate_BM_48(bitmap, bitvalue)
        return
    elif (str(bitmap) == '49'):
        validate_BM_49(bitmap, bitvalue)
        return
    elif (str(bitmap) == '60'):
        validate_BM_60(bitmap, bitvalue)
        return
    elif (str(bitmap) == '61'):
        validate_BM_61(bitmap, bitvalue)
        return
    elif (str(bitmap) == '62'):
        validate_BM_62(bitmap, bitvalue)
        return
    return


def validate_ISO8583_0400(bitmap, bitype, bitvalue):
    print "The bitmap is ", str(bitmap)
    print "The bit-type is ", str(bitype)
    print "The bitvalue is ", str(bitvalue)

    if (str(bitmap) == '2'):
        validate_BM_2(bitmap, bitvalue)
        return
    elif (str(bitmap) == '3'):
        validate_BM_3(bitmap, bitvalue)
        return
    elif (str(bitmap) == '4'):
        validate_BM_4(bitmap, bitvalue)
        return
    elif (str(bitmap) == '7'):
        validate_BM_7(bitmap, bitvalue)
        return
    elif (str(bitmap) == '11'):
        validate_BM_11(bitmap, bitvalue)
        return
    elif (str(bitmap) == '12'):
        validate_BM_12(bitmap, bitvalue)
        return
    elif (str(bitmap) == '13'):
        validate_BM_13(bitmap, bitvalue)
        return
    elif (str(bitmap) == '14'):
        validate_BM_14(bitmap, bitvalue)
        return
    elif (str(bitmap) == '18'):
        validate_BM_18(bitmap, bitvalue)
        return
    elif (str(bitmap) == '19'):
        validate_BM_19(bitmap, bitvalue)
        return
    elif (str(bitmap) == '22'):
        validate_BM_22(bitmap, bitvalue)
        return
    elif (str(bitmap) == '23'):
        validate_BM_23(bitmap, bitvalue)
        return
    elif (str(bitmap) == '25'):
        validate_BM_25(bitmap, bitvalue)
        return
    elif (str(bitmap) == '32'):
        validate_BM_32(bitmap, bitvalue)
        return
    elif (str(bitmap) == '37'):
        validate_BM_37(bitmap, bitvalue)
        return
    elif (str(bitmap) == '38'):
        validate_BM_38(bitmap, bitvalue)
        return
    elif (str(bitmap) == '39'):
        validate_BM_39(bitmap, bitvalue)
        return
    elif (str(bitmap) == '41'):
        validate_BM_41(bitmap, bitvalue)
        return
    elif (str(bitmap) == '42'):
        validate_BM_42(bitmap, bitvalue)
        return
    elif (str(bitmap) == '43'):
        validate_BM_43(bitmap, bitvalue)
        return
    elif (str(bitmap) == '49'):
        validate_BM_49(bitmap, bitvalue)
        return
    elif (str(bitmap) == '60'):
        validate_BM_60(bitmap, bitvalue)
        return
    elif (str(bitmap) == '61'):
        validate_BM_61(bitmap, bitvalue)
        return
    elif (str(bitmap) == '62'):
        validate_BM_62(bitmap, bitvalue)
        return
    elif (str(bitmap) == '63'):
        validate_BM_63(bitmap, bitvalue)
        return
    elif (str(bitmap) == '90'):
        validate_BM_90(bitmap, bitvalue)
        return
    elif (str(bitmap) == '95'):
        validate_BM_95(bitmap, bitvalue)
        return
    return


def prepare_answer(mti, auth_code, response_code, in_pack, out_pack):
    out_pack.setMTI(mti)
    #echoed from request
    out_pack.setBit(2, pack.getBit(2))
    out_pack.setBit(3, pack.getBit(3))
    out_pack.setBit(4, pack.getBit(4))

    out_pack.setBit(7, pack.getBit(7))
    out_pack.setBit(11, pack.getBit(11))
    out_pack.setBit(12, pack.getBit(12))
    out_pack.setBit(13, pack.getBit(13))
    #out_pack.setBit(15, pack.getBit(15))
    out_pack.setBit(18, pack.getBit(18))
    out_pack.setBit(19, pack.getBit(19))
    out_pack.setBit(32, pack.getBit(32))
    out_pack.setBit(37, pack.getBit(37))

    #6 alpha numeric characters, fixed lentgh
    #Conditional  only present if the transaction is approved.
    #If issuing bank does not approve the authorization, this field will not be present.
    out_pack.setBit(38, auth_code);
    out_pack.setBit(39, response_code);
    out_pack.setBit(49, pack.getBit(49));
    return


from ISO8583.ISO8583 import ISO8583
from ISO8583.ISOErrors import *
from socket import *

# Configure the server
#serverIP = "10.57.210.23" 
serverIP = get_ipv4_address()
serverPort = 8583
maxConn = 5
bigEndian = True
#bigEndian = False


# Create a TCP socket
s = socket(AF_INET, SOCK_STREAM)
# bind it to the server port
s.bind((serverIP, serverPort))
# Configure it to accept up to N simultaneous Clients waiting...
s.listen(maxConn)

auth_code = '00000'
response_code = '00'

# Run forever
while 1:
    #wait new Client Connection
    connection, address = s.accept()
    while 1:
        # receive message
        length = connection.recv(4)
        if length:
            print "received length %s " % length
            isoStr = connection.recv(int(length))
            if isoStr:
                isoStr = length + isoStr
                print ("\nInput ASCII |%s|" % isoStr)
                pack = ISO8583()
                #change the protocol
                pack.redefineBit(18, '18', 'Merchant Category Code', 'N', 4, 'n')
                pack.redefineBit(60, '60', 'Additional Data', 'LLL', 999, 'ans')
                pack.redefineBit(62, '62', 'Custom Data', 'AN', 26, 'ans')
                #parse the iso
                try:
                    if bigEndian:
                        pack.setNetworkISO(isoStr)
                    else:
                        pack.setNetworkISO(isoStr, False)

                    v1 = pack.getBitsAndValues()
                    for v in v1:
                        print ('Bit %s of type %s with value = %s' % (v['bit'], v['type'], v['value']))
                        bitmap = str(v['bit'])
                        bittype = str(v['type'])
                        bitvalue = str(v['value'])
                        #print "The bit " , bitmap
                        if pack.getMTI() == '0200':
                            validate_ISO8583_0200(bitmap, bittype, bitvalue)
                        elif pack.getMTI() == '0400':
                            validate_ISO8583_0400(bitmap, bittype, bitvalue)

                    if pack.getMTI() == '0200':
                        print ("\tThat's great !!! The client send a correct message !!!")
                    elif pack.getMTI() == '0420':
                        print ("\tThat's great !!! The client send a correct message !!!")
                    elif pack.getMTI() == '0100':
                        auth_code = '000003'
                        response_code = '02'
                        print ("The client dosen't send the correct message!")
                        break


                #consume all exceptions and just log the information, server should not die unless its
                #killed explicitly
                #send answer
                except InvalidIso8583, ii:
                    auth_code = '000003'
                    response_code = '02'
                    print ii
                #catch all exception(s) here
                except:
                    auth_code = '000003'
                    response_code = '02'
                    print ('Something happened!!!!')

                response = ISO8583()

                if pack.getMTI() == '0420':
                    mti = '0430'
                if pack.getMTI() == '0200':
                    mti = '0210'
                try:
                    prepare_answer(mti, auth_code, response_code, pack, response)
                except:
                    print ('Something happened!!!!')

                if bigEndian:
                    ans = response.getNetworkISO()
                else:
                    ans = response.getNetworkISO(False)

                print ('Sending answer %s' % ans)
                connection.send(ans)

            else:
                break
    # close socket
    connection.close()
    print ("Closed...")
