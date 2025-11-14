# Date: 14-11-2025
# Author: Ella Zhang
# YR10 DGT 
# Version 3.13.7
#Calculates the area and perimeter for a shape 

#Loop
'''def num_check():
    keep_looping =""
    while keep_looping =="":
        #Main error msg
        error = "please enter a number more than 0. \n" 
        #Error msg for when the user inputs something that is not a valid number
        error2 = "Please enter a number."
       
        #Asks the user for width
        while True:
            try:
                width = float(input("Enter your width: "))
                #Error checking for width
                if width > 0:
                    print(f"Your width is {width}")
                    break
                else:
                    print(error)
            except ValueError:
                    print(error2)

        #Asks user for height          
        while True:
            try:  
                height = float(input("Enter your height: ")) 
                #Error checking for height
                if height > 0:
                    print(f"Your height is {height}")
                    break
                else:
                    print(error)
            except ValueError:
                print(error2)
                           
            #Formulas to calculate the perimeter and area
            perimeter = 2*(width + height)
            area = width*height
                    
            #print answer
            print()
            print(f"perimeter: {perimeter} units; area: {area} square units. \n")
            #Ask user if they want to run the program again 
            loop = input("Press <ENTER> to continue, or any other key to quit.")
            loop2 = loop
            #Error checking
                

num_check()'''

#Error checking
def valid_num(question, low):
    while True:
        try:
            response = float(input(question))
            if response > low:
                return response
            else: #Error message when user inputs something other than a valid number
                print("Please enter a number more than 0.\n")
        except ValueError:
            #Error msg for when the user inputs a number less than or equal to 0
            print("Please enter a valid number.\n")

# Main program
while True:
    #Ask for width + print output
    width = valid_num("Enter your width: ", 0)
    print(f"Your width is {width}.\n")
    #Ask for height + print output
    height = valid_num("Enter your height: ", 0)
    print(f"Your height is {height}.\n")
    #Formulas for area and perimeter
    area = width * height
    perimeter = 2 * (width + height)
    #Print perimeter and area
    print(f"Perimeter: {perimeter} units; Area: {area} square units.\n")
    #Asks the user if they want to rerun the program
    loop = input("Press <ENTER> to continue, or any other key to quit.")
    #Breaks the loop if the user presses a key other than <ENTER>
    if loop != "":
        break
    else:
        print("Program loops")


