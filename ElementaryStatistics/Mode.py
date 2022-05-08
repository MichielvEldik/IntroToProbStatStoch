# What's next?
# Implement the keyWithMaxValue function!


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


dataset = [1, 4, 5, 7, 7, 8, 1, 2, 3, 3, 3, 9, 9, 9, 9, 9]


arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr,n)

print(Ans)

# What if there are no repeats?
# Step 1, inventory of all unique values.
# Step 2, check if length of that list equals
unique_set = []
for i in range(0, len(dataset)):
    if dataset[i] not in unique_set:
        unique_set.append(dataset[i])

print(unique_set)

if len(unique_set) == len(dataset):
    print("Hi")
else:
    print("Hoi")

frequencies = {}
frequencies[1] = 2


print(frequencies)

for i in unique_set:
    freq = 0
    for b in dataset:
        if i == b:
            freq = freq + 1
    frequencies[i] = freq
print(frequencies)

print(frequencies[1])
print(max(frequencies, key = frequencies.get))



# Get max

print("---")


def keywithmaxval(d):
    v = list(d.values())
    k = list(d.kays())
    return k[v.index(max))]



