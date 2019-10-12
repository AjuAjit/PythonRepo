# divides the list by 2 and stores it in a new list
def divide_list_by_constant(n):
    numbers = []    # given list
    results = []    # output list
    for i in range(1, n+1):
        numbers.append(int(input()))
        results.append((numbers[i-1])/2)
    print(results)


no_of_terms = int(input("Enter the number of terms in the list: "))
divide_list_by_constant(no_of_terms)    # pass the number of terms in the list as input
