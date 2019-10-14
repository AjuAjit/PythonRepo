# finds the factorial of the given number
def factorial_of_a_number(number):
    if number == 1:
        return 1
    else:
        return number * factorial_of_a_number(number-1)     # recursive function is used


n = int(input("Enter the number for which factorial has to be found: "))
fact = factorial_of_a_number(n)
print("{}! = {}".format(n, fact))   # n! = __
