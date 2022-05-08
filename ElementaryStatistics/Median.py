
even_n = [1,3,6,7,8,9]
odd_n = [1,4,6,8,8]

# Step 1, order the dataset.

def InsertionSort(dataset):
    # Traverse through the dataset except index 0
    for i in range(1, len(dataset)):
            # Key is the value at index i.
            key = dataset[i]
            # The index next to the current index (to the left)
            j = i - 1 
            # stop iterating when we reach 0 on our j because that is the bounds of our list
            # also stop when our key is bigger than our j. That part is then already sorted.
            while j >= 0 and key < dataset[j]:
                dataset[j+1] = dataset[j]
                j -= 1
            dataset[j+1] = key
    return dataset

def Median(dataset):
    dataset = InsertionSort(dataset)
    counter = 0 
    for i in dataset:
        counter += 1 

    if (counter % 2) == 0:
        middle_1 = int((counter / 2)-1)
        middle_2 = int(middle_1 + 1)
        median_even = (dataset[middle_1] + dataset[middle_2]) / 2
        return median_even
    
    else:
        counter = counter + 1
        counter = counter - 1 # To deal with index starting at zero.
        index = int(counter / 2)
        return dataset[index]
answer = Median(even_n)
answer_2 = Median(odd_n)
print("Median is {0}".format(answer))
print("Median is {0}".format(answer_2))

