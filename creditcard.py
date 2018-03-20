import random
import math
creditcardnumber=input("Enter credit card number:")
print (creditcardnumber)
def credit_card_validation(cardnumber):
    cardnumber=cardnumber.split()
    for i in range(len(cardnumber)):
        cardnumber[i]=int(cardnumber[i])
    print(cardnumber)
    check_digit=cardnumber.pop()
    print(check_digit)
    cardnumber.reverse()
    print(cardnumber)
    for i in range(0,len(cardnumber),2):
        cardnumber[i] =2 * cardnumber[i]
    print(cardnumber)
    for i in range(len(cardnumber)):
        if cardnumber[i]> 9:
            cardnumber[i]-=9
    print(cardnumber)

    total=sum(cardnumber)
    print(total)
    total=int(list(str(total))[1])
    print(total)

    validation=total
    if check_digit == validation :
        print ("credit card is valid")
    else:
        print("credit card is invalid")
credit_card_validation(creditcardnumber)

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
