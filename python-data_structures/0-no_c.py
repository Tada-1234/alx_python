def no_c(my_string):
    lists = [w for w in my_string]
    index = 0
    for n in lists:
        temp = lists[index]
        if temp == 'C' or temp == 'c':
            del lists[index]
            index = index + 1
        else:
            index = index + 1
    new_string = ''.join([str(item) for item in lists])
    return new_string
