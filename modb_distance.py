def main():
    print("This program converts Kilometers to Miles.")
   

    for i in range(11): 
        print("---------------------------------------------") 
        k = i * 10
        m = (k / 8 * 5)
        print(str(k) + " Kilometers is: " + str(m) + " Miles")
    for i in range (2):
        choice = input("Press the <K> key for Kilometers or Press the <M> key for Miles:")
        if choice == "k":     
            k = 0 
            k = eval(input("What is the distance in Kilometers? "))
            m = (k / 8 * 5)
            print(str(k) + " Kilometers is: " + str(m) + " Miles ")
            print("---------------------------------------------") 
        elif choice == "m":
            m = 0
            m = eval(input("What is the distance in Miles? ")) 
            k = (m / 5 * 8)
            print(str(m) + " Miles is: " + str(k) + " Kilometers")

    input("Press the <Enter> key to quit.")
    
main ()