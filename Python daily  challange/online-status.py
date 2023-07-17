#function named online_count that takes one parameter.
#The parameter is a dictionary that maps from strings of names to the string "online" or "offline"
#function should return the number of people who are online.
def online_count(dictionary):
    count = 0
    for i in dictionary.values():
        if i == "online":
            count +=1
    return count
        
dictionary = {
    "Alice":"online",
    "bob":"offline",
    "collins":"online",
    "mum":"online"
}
result = online_count(dictionary)
print(result)
