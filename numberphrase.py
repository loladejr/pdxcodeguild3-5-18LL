import math
user_input = int(input("Enter the number you want in words:"))

tens_digit = user_input//10

one_digit = user_input % 10

number_tens_dict= {'1':'one','2':'twenty', '3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty', '9':'ninety'}
number_one_dict= {'0':' ' ,'1':'one','2':'two', '3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight', '9':'nine'}

print (str(number_tens_dict[str(tens_digit)]) + (str(number_one_dict[str(one_digit)])))
