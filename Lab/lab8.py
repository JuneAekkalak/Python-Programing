def sumdigit(n):
    sum = 0
    while n != 0 :
        digit = n % 10 
        n = n // 10
        sum = sum + digit 
    return sum
def main():
    n = int(input("Enter your integer is : "))
    result = sumdigit(n)
    print("output is %d"%result)
if __name__ == "__main__":
    main()