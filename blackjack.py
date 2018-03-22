import math
import random
print("Welcome to Las Portland")
while True:
    while True:

        print(" Pick a card amongst A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K ")
        card_1 = input( "card 1" ":" "").lower().strip()
        card_2 = input( "card 2" ":" "").lower().strip()
        card_3 = input( "card 3"":" "").lower().strip()
        card_dict= {'A':'1', '2':'2','3':'3','4':'4','5':'5', '6':'6', '7':'7', '8':'8','9':'9','J':'10','Q':'10','K':'10'}    
        if card_1 in card_dict.keys() and card_2 in card_dict.keys() and card_3 in card_dict.keys():
                    break


    # print(card_dict[card_1])
    tots= int(card_dict[card_1]) + int(card_dict[card_2]) + int(card_dict[card_3])
    def card(tots):
            if tots < 17:
                return "hit"
            elif 21 > tots <=17 :
                return "stay"
            elif tots==21:
                return "Blackjack!"
            elif tots > 21 :
                return "busted"
    print(card(tots))
    playag=input("Do you want to play again:")
    # if playag == "yes" or "y":
    if playag == "no":
            break
