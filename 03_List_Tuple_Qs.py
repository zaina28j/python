"""
# LIST
# Basic Level 
# 1. Write a Python program to create a list of integers and print its elements. 
lst = [1, 2, 3, 4, 5]
for n in lst:
    print(n)

# 2. Write a program to find the sum and average of all elements in a list. 
lst = [1, 2, 3, 4, 5]
print("Sum:", sum(lst))
print("Avg:", sum(lst)/ len(lst))

# 3. Write a program to find the largest and smallest element in a list. 
lst = [1, 2, 3, 4, 5]
print('Smallest:', min(lst))
print("largest:", max(lst))

# 4. Write a Python program to count the number of elements in a list without using len(). 
lst = [1, 2, 3, 4, 5]

count = 0
for i in lst:
    count += 1

print(f"Elements in lis is: {count} ")

# 5. Write a program to reverse a list without using built-in functions. 
lst = [1, 2, 3, 4, 5]
lst.reverse()
print(lst)

# 6. Write a program to check if an element exists in a list. 
lst = [1, 2, 3, 4, 5] 
n = int(input("Enter a number: "))
found = False

for i in lst:
    if i == n:
        found = True
        break
if found:
    print("Number Exist")
else:
    print("Not Exist")

# 7. Write a Python program to remove duplicate elements from a list. 
lst = [5, 1, 2, 4, 3, 4, 2, 5, 1, 3] 

lst = list(set(lst))
print(lst)

# 8. Write a program to sort a list in ascending and descending order. 
lst = [1, 3, 2, 5, 4]

lst.sort()
print(f"Ascending list: {lst}")

lst.sort(reverse = True)
print(f"Descending list: {lst}")

# Intermediate Level 
# 9. Write a program to merge two lists and remove duplicates. 

l1 = [1, 2, 3, 4, 5, 6]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

l3 = list(set(l1 + l2))
print(l3)

# 10. Write a program to find common elements between two lists. 
l1 = [87, 32, 56, 34, 90]
l2 = [34, 92, 22, 42, 87]

com = []
for i in l1:
    if i in l2:
        com.append(i)
print(com)

# 11. Write a program to split a list into even and odd numbers. 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []
odd = []

for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even List:-", even ,"\nOdd List:-", odd)

# 12. Write a program to rotate a list by n positions. 
lst = [1, 2, 3, 4, 5]
r = int(input("Enter how many rotations: "))

for i in range(r):
    first = lst.pop(0)
    lst.append(first)
print(lst)


# 13. Write a Python program to find the second largest number in a list.
lst = [10, 32, 5, 88, 60]

largest = lst[0]
second = lst[0]

for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print(f"Second Lagest is {second}")

# 14. Write a program to flatten a nested list. 
lst = [1, [2, 3], [4, 5], 6]

flat = []

for i in lst:
    if type(i) == list:
        for j in i:
            flat.append(j)
    else:
        flat.append(i)
print(flat)

# 15. Write a program to count frequency of each element in a list. 
lst = [4, 1, 3, 6, 9, 5, 7, 2, 5, 8, 9, 1, 2, 4, 5, 6, 7, 1]

freq = {}

for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

# 16. Write a program to replace all negative numbers with zero in a list. 
lst = [2, -4, 5, -6, 3, -2, 1, -9]

for i in range (len(lst)):
    if lst[i] < 0:
        lst[i] = 0
print(lst)
    
# Advanced Level 
# 17. Write a program to remove all occurrences of a given element from a list. 
lst = ['Apple', 'Banana', 'Orange', 'Mango', 'papaya']
o = str(input("enter your occurrence: "))

nlst = []

for i in lst:
    if i != o:
        nlst.append(i)
print(nlst)

# TUPLE 
# Basic Level 
# 23. Write a Python program to create a tuple and print its elements. 
tpl = (1, 2, 3, 4, 5)

for i in tpl:
    print(i)

# 24. Write a program to find the length of a tuple. 
tpl = (1, 2, 3, 4, 5)

# len = 0

# for i in tpl:
#     len += 1
print(len(tpl))

# 25. Write a program to find the maximum and minimum element in a tuple. 
tpl = (1, 2, 3, 4, 5)
print(max(tpl))
print(min(tpl))

# 26. Write a program to convert a tuple into a list. 
tpl = (1, 2, 3, 4, 5)

print(list(tpl))

# 27. Write a program to check if an element exists in a tuple.
n = int(input('enter a number: ')) 
tpl = (1, 2, 3, 4, 5)

found = False

for i in tpl:
    if i == n:
        found = True
        break
   
if found == True:
    print("Number Exists")
else:
    print("Not exists")

# 28. Write a program to count occurrences of an element in a tuple. 
tpl = (1, 2, 3, 4, 5)

o = {}

for i in tpl:
    if i in o:
        o[i] += 1
    else:
        o[i] = 1
print(o)

# 29. Write a program to slice a tuple and display the result.
S = int(input("Enter a Start index: ")) 
E = int(input("Enter a End index: ")) 
tpl = (1, 2, 3, 4, 5)

result = tpl[S:E]

print(result)

# 30. Write a program to find repeated elements in a tuple. 
tpl = (1, 2, 3, 4, 2, 4, 5, 6, 1, 8, 3)

r = []

for i in tpl:
    if tpl.count(i) > 1 and i not in r:
        r.append(i)
print(r)
    
# 31. Write a program to merge two tuples. 
t1 = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)

t3 = t1 + t2
print(t3)

# 32. Write a program to unpack elements of a tuple into variables. 
tpl = (10,20,30,40)

a, b, *c = tpl

print(a)
print(b)
print(c)

# 33. Write a Python program to sort a tuple. 
tpl = (20, 40, 10, 50, 30)

lst = list(tpl)
lst.sort()

tpl = tuple(lst)
print(tpl)

# 34. Write a program to convert a list of tuples into a dictionary. 
lst = [(1,'a'), (2,'b'), (3,'c')]

d = {}

for i in lst:
    d[i[0]] = i[1]

print(d)
"""

# Advanced Level 
# 35. Write a program to find the index of an element in a tuple.




