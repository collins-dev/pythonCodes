def only_ints(num_1, num_2):

    if type(num_1) == int and type(num_2) == int:
        return True
    else: 
        return False

print(only_ints(1, 2))
