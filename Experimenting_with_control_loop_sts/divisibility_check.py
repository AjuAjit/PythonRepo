# checks if the number is divisible by 3, 5 or 3 and 5
def divisibility_check(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:   # divisible by 3 and 5
            print("BOOYAKA")
        elif i % 5 == 0:
            print("YAKA")
        elif i % 3 == 0:
            print("BOO")


n = int(input("Enter the numbers up to which divisibility should be checked:"))
divisibility_check(n)   # send the last term up to which divisibility should be checked as input
