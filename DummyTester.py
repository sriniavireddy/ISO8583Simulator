import MessageFactories as f
from ISO8583.ISO8583 import ISO8583
__author__ = 'kakarthikeyan'

# create a Message factory

msgType1 = "0420"
msgType2 = "0400"

iso = ISO8583()
#Modifications for our protocol
iso.redefineBit(18, '18', 'Merchant Category Code', 'N', 4, 'n')
iso.redefineBit(60, '60', 'Additional Data', 'LLL', 999, 'ans')
iso.redefineBit(62, '62', 'Additional Data', 'N', 26, 'ans')

isoMessage = '0420723C648108E0801C1640320370945546112800000000000010000228121605917114041605022818126051826812800600003140581291711400000001000980020002997PAYPAL Lewinsky Gus      4029357733   LU0360670033000513174261    63428                                   004400716601410405812917114    018114032037094554611                  01812Gus Lewinsky    0201363428 Broad Street                 01014Clovelly                 00416JO 00418AAY000000000000000     00   '
#isoMessage = '0100723C64810800801C1640320070945546112800000000000010000228121605917114041605022818126051826812800600003140581291711400000001000980020002997PAYPAL Lewinsky Gus      4029357733   LU0360670033000513174261    63428                                   004400716601410405812917114    018114032037094554611                  01812Gus Lewinsky    0201363428 Broad Street                 01014Clovelly                 00416JO 00418AAY000000000000000     00   '

iso.setIsoContent(isoMessage)
fullstr = iso.getNetworkISO()

iso.setNetworkISO(fullstr)

# call validate on msgtype1
print f.MessageFactory().getFactory(msgType1)
print f.MessageFactory().getFactory(msgType1).getRequestValidator()
f.MessageFactory().getFactory(msgType1).getRequestValidator().validateMessage(iso)
f.MessageFactory().getFactory(msgType1).getResponseGenerator().generateResponse(iso,"30")



