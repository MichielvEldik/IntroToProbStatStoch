

dataset = [1, 4, 3, 6, 88, 20, 3]

def FindMean(dataset):
    total = 0
    cardinal = 0
    for i in dataset:
        total = total + i
        cardinal = cardinal + 1
    mean = total / cardinal
    return mean


mean = FindMean(dataset)

print("We work with the following dataset...")
for i in dataset:
    print(i)
print("The mean of this dataset is {0}".format(mean))

