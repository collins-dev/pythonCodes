# create a list of ten numbers
numbers = [5, 2, 10, 3, 8, 1, 7, 6, 4, 9]

# initialize the minimum value to the first number in the list
minimum = numbers[0]

# iterate over the list to find the minimum value
for num in numbers:
    if num < minimum:
        minimum = num

# print the minimum value
print("The minimum value is:", minimum)
