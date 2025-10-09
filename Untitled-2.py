# Date: 08-10-2025
# Author: Ella Zhang
# YR10 DGT 
# Version 3.13.7

# Different types of variables
# Store a string
greeting = "Hello World!"
print(greeting)

# Store a number
my_number = 80 # assigned 80 to the variable called my_number 
print(my_number)
my_number2 = 7
print(my_number2)

# Assign the value of one variable to another
my_number = greeting
print(my_number) # Don't assign values to numbers that don't make sense
'''67'''
# creating new variable 
num_1 = 6
num_2 = 7
sum1 = 6 +7 # Ts is not good practise !!!!
print(sum1)

# Do ts instead ;
sum1 = num_1 + num_2
print(sum1)
sum_string1 = "66"
sum_string2 = "77"

# Adding two strings tgthr, ts is called concatenation 
sum = sum_string1 + sum_string2
print(sum)
# Print formatting, f stands for 'format' and insert the value of variables 
print(f"my calculation for adding {num_1} and {num_2} together is {sum1}.")
