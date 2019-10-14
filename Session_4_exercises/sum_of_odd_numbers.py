# sums the odd numbers less than 100
def sum_of_odd_numbers():
    total = 0   # initializing the total variable
    for i in range(100):
        if i % 2 == 1:  # odd number check
            total = total + i
    return total


odd_number_sum = sum_of_odd_numbers()
print("Sum of odd numbers less than 100 = {}".format(odd_number_sum))
