def no_c(my_string):
    new_string = []
    for n in my_string:
        if n != 'C' and n != 'c':
            new_string.append(n)

    return ''.join(new_string)
