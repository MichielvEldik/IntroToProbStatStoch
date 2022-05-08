S = [1,2,3,4,5,6]
A = [1,2]
B = [2,4,5]
C = [1,5,6]

# A UNION B

both_A_and_B = []

for i in A:
    if i not in both_A_and_B:
        both_A_and_B.append(i)

for i in B:
    if i not in both_A_and_B:
        both_A_and_B.append(i)

print("A UNION B is")
print(both_A_and_B)

# A Intersect B
intersect = []

for i in both_A_and_B:
    if i in A and B:
        intersect.append(i)
print("Intersect..")
print(intersect)

# Complement
complement_A = []
for i in S:
    if i not in A:
        complement_A.append(i)
complement_B = []
for i in S:
    if i not in B:
        complement_B.append(i)


print(complement_A)
print(complement_B)


# Check De morgan's law by (A UNION B)^c and A^c INTERSECT B^c
a_union_b = []
a_union_b_complement = []
a_complement = []
b_complement = []


# Part 1:
# (A UNION B)^c = A^c intersect B^c
# S not in A or B is the same as not A and not B

# Find (A UNION B)^c
for i in S:
    if i in A or i in B:
        a_union_b.append(i)
print(a_union_b)

for i in S:
    if i not in a_union_b:
        a_union_b_complement.append(i)

print(a_union_b_complement)



# Find not A and not B
for i in S:
    if i not in A:
        a_complement.append(i)

for i in S:
    if i not in B:
        b_complement.append(i)
print(a_complement)
print(b_complement)

