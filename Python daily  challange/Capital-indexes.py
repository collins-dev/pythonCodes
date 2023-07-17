#The function takes a single parameter, which is a string. 
#The function returns a list of all the indexes in the string that have capital letters.
def capital_indexes(name):
    index_list = []
    for i in range(len(name)):
        if name[i].isupper():
            index_list.append(i)
    return index_list


print(capital_indexes("TEsT"))
print(capital_indexes("HeLlO"))

    
