import math

operation_num= input("What is the operation you'd like to perform?" ":" "(" " + " "," "-" "," "*" "," "/" ")" ":")
num_one = input("What is the first number?" ":") #first value entered by customer,
num_two =input("What is the second number?" ":") #second value entered by customer
num_one=int(num_one)
num_two=int(num_two)
if operation_num == "+":
    print(num_one + num_two)
elif operation_num == "*":
    print(num_one * num_two)
elif operation_num == "-":
    print(num_one - num_two)
elif operation_num == "/":
    print(num_one / num_two)
