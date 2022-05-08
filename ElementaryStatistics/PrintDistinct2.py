# --------------------------
# SOLUTION 2: Using sorting
# -------------------------

# Using sorting, the problem becomes O(nlogn)
# First sort the array
# Traverse the list

# Python program to print all distinct
# elements in a given array


def printDistinct(arr, n):
    arr.sort()

    for i in range(n):
        if(i < n-1 and arr[i] == arr[i+1]):
            while (i < n-1 and (arr[i] == arr[i+1])):
                i+=1
        else:
            print(arr[i], end=" ")

# 
