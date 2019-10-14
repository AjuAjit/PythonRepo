# prints the type of different values
def printing_types_of_values():
    lists = [3.1112, complex('3+2j'), 'c', "bollywood", """tollywood""", r"kollywood",
             [1, 2, 3, 4, 5], range(1, 10), False,
             11*3, 12/2, 11//3]   # the values are stored in a list
    for i in range(len(lists)):     # range starts from 0
        print("Type of {} is {}".format(lists[i], type(lists[i])))


printing_types_of_values()
