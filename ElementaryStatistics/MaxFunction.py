#Program to find the largest element in an Array.

# Linear traversal
# Time complexity O(N)
def largest(arr, n):
    maxie = arr[0]
    for i in range(1, n):
        if arr[i] > maxie:
            maxie = arr[i]
    return maxie


arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr,n)

print(Ans)


