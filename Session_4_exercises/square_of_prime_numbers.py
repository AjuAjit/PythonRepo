# prints the squares of prime numbers less than 100
def square_of_prime_numbers():
    lists = []
    for i in range(2, 100):     # starting from 2 since 1 is neither prime nor composite
        flag = 0
        for j in range(2, i//2+1):     # checking only till i//2+1 for better efficiency
            if (i % j ==0):
                flag = 1
        if flag == 0:
            lists.append(i*i)   # square of the number is stored in a list
    return lists


squares_of_prime_numbers = square_of_prime_numbers()
print("Squares of prime number less than 100 are {}".format(squares_of_prime_numbers))
