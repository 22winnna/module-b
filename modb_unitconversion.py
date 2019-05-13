def main():
    print("This program converts Kilograms to Pounds.")
   

    for i in range(11): 
        print("---------------------------------------------") 
        k = i * 10
        p = round(k * 2.2)
        print(str(k) + " Kilograms is: " + str(p) + " Pounds")
    for i in range (2):
        choice = input("Press the <K> key for Kilometers or Press the <P> key for Pounds:")
        if choice == "k":     
            k = 0 
            k = eval(input("What is the amount in Kilograms? "))
            p = round(k * 2.2)
            print(str(k) + " Kilograms is: " + str(p) + " Pounds ")
            print("---------------------------------------------") 
        elif choice == "p":
            p = 0
            p = eval(input("What is the amount in Pounds? ")) 
            k = round(p / 2.2)
            print(str(p) + " Pounds is: " + str(k) + " Kilograms")

    input("Press the <Enter> key to quit.")
    
main ()