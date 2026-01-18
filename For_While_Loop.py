"""
# FOR Loop 

# Q1. Write a program to print numbers from 1 to 100.
for i in range(1,101):
    print(i)

# Q2. Write a program to print all even numbers between 1 and 50.
for i in range (1, 51):
    if i%2 == 0:
        print(i)

# Q3. Write a program to print the sum of first n natural numbers.
n = int(input("Enter a number: "))

sum = 0
for i in range(1, n+1):
    sum = sum + i
print("Sum =", sum)

# Q4. Write a program to print the multiplication table of a given number.
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")

# Q8. Write a program to print all prime numbers between 1 and 100.
for n in range(2, 101):
    for i in range (2, n):
        if n % i == 0:
            break
    else:
        print(n)

# Q9. Write a program to calculate the factorial of a number using a for loop.
n = int(input("Enter a number: "))

fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)
    
# Q10. Write a program to print the reverse of a string using a for loop.   
s = (input("Enter a string: "))

rev= ""
for i in s:
    rev = i + rev
print(rev)

# WHILE Loop 
# Q11. Write a program to print numbers from 1 to 50 using a while loop.
a = 1
while a <= 50:
    print(a)
    a += 1

# Q12. Write a program to print all odd numbers between 1 and 50. 
a = 1
while a <= 50:
    if a%2 != 0:
        print(a)
    a += 1

# Q13. Write a program to calculate the sum of digits of a number.
n = int(input("Enter a number:  "))
a = 1
sum = 0

while a<=n:
    rem = n%10 
    sum = sum+rem
    n = n//10
print(f"sum of digit: {sum}")

# Q14. Write a program to reverse a number using a while loop. 
n = int(input("Enter a number"))
a = 1
add = 0

while a<=n:
    rem = n%10
    add = add*10+rem
    n = n//10
print(add)

# 15. Write a program to find the factorial of a number using a while loop. 
n = int(input("Enter a number: "))
a = 1
fact = 1

while a <= n:
    fact = fact * a
    a += 1
print(fact)


# 16. Write a program to keep taking input from the user until the user enters 0.
n = int(input("Enter a number: "))

while n != 0:
    n = int(input("Enter a number: "))

# 17. Write a program to find the largest digit in a number.
n = int(input("Enter a number: "))
copy = n
largest = 0

while n>0:
    rem = n % 10
    if rem > largest:
        largest = rem
    n = n // 10
print(f"Largest number of {copy} is {largest}")

# 18. Write a program to check whether a number is a palindrome.
n = int(input("Enter a number: "))
copy = n 
add = 0
a = 1

while a<=n:
    rem = n % 10
    add = add*10+rem
    n = n//10
print(f"reverse number {add}")
if copy == add:
    print("It,s Palindrome ")
else:
    print("It,s not palindrome")
"""

