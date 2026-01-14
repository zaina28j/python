
# Q1. Write a Python program to check if a number is positive.
n = int(input("Enter a number: "))
if n>0:
    print(f"{n} is POSITIVE NUMBER")

# Q2. Print "Eligible to vote" if age is 18 or above.
n = int(input("Enter your age: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not Eligible")

# Q3. Check if a number is divisible by 7. 
n = int(input("Enter a number: "))
if n%7==0:
    print(f"{n} is divisible by 7")
else:
    print(f"{n} is NOT divisible by 7")

# Q4. Print "Pass" if marks are greater than 40.
n = int(input("Enter your marks: "))
if marks>40:
    print("Pass")
else:
    print("Fail")

# Q5. Check if a number is greater than 100.
n = int(input("Enter a number: "))
if n>100:
    print(f"{n} is greater then 100")
else:
    print(f"{n} is not greater then 100")

# Q6. Display a message if temperature exceeds 45°C.
n = float(input("Enter temperature: "))
if n > 45:
    print("Alert! Temperature is above 45°C")
else:
    print("Temperature is normal")

# Q7. Check if a string length is more than 8 characters.
text = input("Enter text: ")
if len(text) > 8:
    print("String length is greater than 8")

# Q8. Print "Logged In" if password matches "admin123".
p = input("Enter password: ")
if p == "admin123":
    print("Logged In")
else:
    print("Incorrect Password")

# Q9. Check if a number is a multiple of 10.
n = int(input("Enter a number: "))
if n % 10 == 0:
    print("Number is divisible by 10")
else:
    print("Number is not divisible by 10")

# Q10. Print a warning if balance is below minimum limit.
balance = int(input("Enter your balance: "))
min_limit = 1000

if balance < min_limit:
    print("Warning! Balance is below minimum limit")

# Q11. Check whether a number is even or odd.
n = int(input("Enter a number: "))
if n % 2 == 0:
    print(f"{n} is Even number")
else:
    print(f"{n} is Odd number")

# Q12. Find the largest of two numbers.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a>b:
    print("Largest is", a)
else:
    print("Largest is", b)

# Q13. Check whether a person is eligible for driving license.
age = int(input("Enter  your age: "))

if age>=18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")

# Q14. Print "Pass" or "Fail" based on marks.
m = int(input("Enter marks: "))

if m >= 30:
    print("Pass")
else:
    print("Fail")

# Q15. Check whether a number is positive or negative.
num = float(input("Enter a number: "))

if num >= 0:
    print("Positive")
else:
    print("Negative")

# Q16. Check whether a character is a vowel or consonant.
c = input("Enter a character: ")

if c in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

# Q17. Check if a year is leap or not.
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a Leap Year")
else:
    print("It's not a Leap Year")

# Q18. Print "Valid Password" or "Invalid Password".
p = input("Enter password: ")

if len(p) >= 8:
    print("Valid Password")
else:
    print("Invalid Password")

# Q19. Determine whether salary is taxable or not.
salary = float(input("Enter a salary: "))

if salary>250000:
    print("Taxable")
else:
    print("Not Taxable")

# Question 20. Check whether a number is greater than 50 or not.
num = float(input("Enter a number: "))

if num > 50:
    print("Greater than 50")
else:
    print("Less then 50")
# Q21. Find the largest of three numbers. 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b:
    if a > c:
        print("Largest number is", a)
    else:
        print("Largest number is", c)
else:
    if b > c:
        print("Largect number is", b)
    else:
        print("Largect number is", c)

# 22. Check whether a number is positive, negative, or zero.
n = int(input("Enter a number: "))

if n>0:
    print(f"{n} This number is Positive")
else:
    if n<0:
        print(f"{n} This number is Negative")
    else:
        print(f"{n} This number is Zero")


# Q23. Assign grades: ● A → marks ≥ 90  ● B → marks ≥ 75  ● C → marks ≥ 60  ● Fail → below 60 
if marks >= 90:
    print("A")
else:
    if marks >= 75:
        print("B")
    else:
        if marks >= 60:
            print("C")
        else:
            print("Fail")
