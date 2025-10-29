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

# Version 3
# Making the program more pythonic.
    # Convert answer to lower case using .lower()
count =int.len(loop="")
while True:
    like_coffee = input("Do you like coffee? \n").lower()

    if like_coffee in ["yes", "y", "yh", "sure", "yep", "probably", "67"]:
        print("That is great! c:")
    elif like_coffee in ["no", "n", "nope"]:
        print("I agree, water is superior")

    like_tea = input("Do you like tea instead? \n").lower()
    if like_tea in ["yes", "y", "yh", "sure", "yep", "probably", "67"]:
        print("Ok that's cool ig.")
    elif like_tea in ["no", "n", "nope"]:
        print("yh sybau ts pmo you monkey.")
    
    else: # Error msg.
        print("Girl what.")

    loop = input("Press <ENTER> to continue, or any other key to quit.")
    if loop.strip() != "":
        break
    print(count)



          