def findCardType(cardNumber):
    try:
        if cardNumber[:1] == '4':
            return 'V' #Visa card
        else:
            return 'M' #Master card
    except:
        return 'V' # defaulting it to Visa Card

