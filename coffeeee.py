# Date: 10-10-2025
# Author: Ella Zhang
# YR10 DGT 
# Version 3.13.7

# Coffee
# Some people dislike coffee
# Solution
# Person should be convinced to drink coffee
# Components    
    # - Input
      # - Record answers
    # - Question
    # - Response
# Error checking

# TO-DO: Ask the user if they like coffee
       #Record the answer
       #Give an answer back
# Ask the user whether they like coffee or not
'''like_coffee = input ("Do you like coffee? ")
print(f'Your answer was "{like_coffee}".')

if like_coffee == "Yes" or "y" or "YES" or "Y" or "yh" or "sure" or "Yep" or "probably" or "yes" or "67": 
    print("That is great! c:")

else:
    print("I agree, water is superior") '''

# Version 2 
# While loop
loop = ""
while True:
    if loop == "":
        like_coffee = input("Do you like coffee? ")

        if like_coffee.lower() in ["yes", "y", "yh", "sure", "yep", "probably", "67"]:
            print("That is great! c:")
        elif like_coffee.lower() in ["no", "n", "nope"]:
            print("I agree, water is superior")
        else:
            print("what")

