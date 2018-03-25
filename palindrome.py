import string
import math


def check_palindrome():
    word_to_check = input("Enter a word:")
    word_to_check=list(word_to_check)

    if word_to_check == list(reversed(word_to_check)):
        print(str(word_to_check)+"is a palindrome")
    else:
        print(str(word_to_check) + "is not a palindrome")


check_palindrome()


def check_anagram():
    print("This function is to check for anagrams. anagrams are words that can be arranged to fit each other")
    word1 = input("Enter first word:").lower().replace(' ','')
    word2 = input("Enter second word:").lower().replace(' ','')
    word1=list(word1).sort()
    word2=list(word2).sort()
    # word2=word2.
    if word1==word2:
        print ("This word is an anagram")
    else:
        print("this word is not an anagram")
check_anagram()
