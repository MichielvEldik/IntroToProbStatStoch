
# Index function
def Indexer(dataset, value):
    for i in range(0, len(dataset)):
            if value == dataset[i]:
                return i

# Largest function
def largest(arr, n):
    maxie = arr[0]
    for i in range(1, n):
        if arr[i] > maxie:
            maxie = arr[i]
    return maxie

# Get dictionary key with max value
def keyWithMaxValue(dictionary):
    the_keys = list(try_dict.keys())
    the_values = list(try_dict.values())
    max_value = largest(the_values, len(the_values))
    return the_keys[Indexer(the_values, max_value)]

# Max dictionary
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr,n)

print(Ans)

try_dict = {1:10, 2:2, 3:30, 4:15}

print(try_dict.keys())
print(try_dict.values())


the_keys = list(try_dict.keys())
the_values = list(try_dict.values())

max_value = largest(the_values, len(the_values))

print("HOI")
print(max_value)
print("HIHIHI")

# this gets me the max dictionary value, yay! 
print(the_keys[Indexer(the_values, max_value)])




def keyWithMaxValue(dictionary):
    the_keys = list(try_dict.keys())
    the_values = list(try_dict.values())
    max_value = largest(the_values, len(the_values))
    return the_keys[Indexer(the_values, max_value)]


print("TRY FUNCTION")

print(keyWithMaxValue(try_dict))

nautilus = [1, 5, 6, 2]

print(Indexer(nautilus, 5))



print("---")

print(Indexer(the_keys, 4))


# List function 


