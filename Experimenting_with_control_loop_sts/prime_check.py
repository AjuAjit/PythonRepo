# prints the prime numbers between 1 and 100
def prime_numbers():
    lists = []
    for i in range(2, 101):     # range started from 2 since 1 is not a prime number
        flag = 0
        for j in range(2, i//2):    # i//2 is used as end value for better loop efficiency
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            lists.append(i)
    print("Prime numbers from 1 to 100 are {}".format(lists))


prime_numbers()
