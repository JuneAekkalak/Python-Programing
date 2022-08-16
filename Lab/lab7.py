def rate_vat (money):
    ratevat = 0 
    if money >= 100000 :
        ratevat = money * 0.15
    elif money >= 30000 :
        ratevat = money * 0.10 
    elif money >= 10000 :
        ratevat = money * 0.05 
    else :
        ratevat = 0 
    return ratevat

def vat (money , ratevat) :
    money = money - ratevat
    return money 

def main() :
    money = int(input("Enter money => "))
    ratevat = rate_vat(money)
    summoney = vat(money , ratevat)
    print("tax = %.2f"%ratevat)
    print("Net income is %.2f"%summoney)
    
if __name__ == "__main__":
    main()