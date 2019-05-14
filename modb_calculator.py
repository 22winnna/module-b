def main():

    # These are options for the user to choose from
    print("This program is a calculator.")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    # This is so the user can make 100 different equations
    for i in range (100):
        if (choice>=1 and choice<=4): # These nubers are based off of the optione above
            print("Enter two numbers:")
            num1 = int(input()) # Allows the user to enter two numbers of their choice
            num2 = int(input())
            if choice==1: # Choice 1
                res = num1 + num2 # Adds user's chosen numbers
                print("Result = ", res) # Prints result
                
            elif choice == 2: # Choice 2
                res = num1 - num2 # Subtracts the user's chosen numbers
                print("Result = ", res) # Prints result

            elif choice == 3: # Choice 3
                res = num1 * num2 
                print("Result = ", res)

            else: # Choice 4
    	        res = num1 / num2 # Divides the user's chosen numbers
    	        print("Result = ", res) # Prints result

        elif choice == 5: # Choice 5
            exit() # Allows user to exit
            input("Press the <Enter> key to quit.")   

        else:
            print("Wrong input..!!") # If anything else is entered prints wrong input.
            
main ()