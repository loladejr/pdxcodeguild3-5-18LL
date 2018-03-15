import random
import math
while True:

    counter = 0
    old_delta=0
    comp_guess = random.randint(1,10)
    while counter < 10:
        
        while True:
            try:
                guess_num =int(input('Enter a number between 1 and 10'))
                if 0 < guess_num <=10:
                    break
            except:
                print("please enter a valid input")
        delta = math.fabs(guess_num - comp_guess)
        if guess_num == comp_guess :
            print("You are right!")
            break
        elif guess_num < comp_guess:
            print("you are too low")
            if old_delta < delta:
                print(guess_num,  'closer')
        elif guess_num > comp_guess:
            print("you are too high")
            if old_delta > delta:
                print(guess_num, 'closer')

            print("You lose")
        old_delta = delta
        counter = counter + 1
        print("you have guessed" + str(counter))

    play_again=input("do you want to play again" ":").lower()
    if (play_again == 'no'):
        break
#     if old_delta > delta:
# ...             print(num1, num2, 'closer')
# ...     elif old_delta < delta:
# ...             print(num1, num2, 'further')
# ...     else:
# ...             print(num1, num2, 'same')
# ...     old_delta = delta
