# bool operator 

#camparison operator  (==,!=,>,<,<= or >=)

# ==

# a = 2
# b = 5
# print(a == b)

# a = 5
# b = 5
# print(a == b)

# !=

# a = 6
# b = 5
# print(a != b)

# a = 6
# b = 6
# print(a != b)

# >

# a = 9
# b = 8
# print(a > b)

# a = 9
# b = 9
# print(a > b)

# <

# a = 6
# b = 7
# print(a < b)

# a = 6
# b = 6
# print(a < b)

# <=

# a = 9
# b = 9
# print(a <= b)


# >=

# a = 3
# b = 3
# print(a >= b)


# conditional   (if , if else or if elif)


# age = int(input("entre you age:-"))

# if age >= 18:
#     print("eligible to vote...")

# else:
#     print("not eligible")

#largest of two numbers

# a = int(input("enter a num:"))
# b = int(input("enter a num:"))

# if a > b:
#     print("a greater")

# else:
#     print("a not greater")

# check if a number is positive or negative

# num = int(input("enter a number:"))

# if num >0:
#     print("positive")
# else:
#     print("negative")

# check if a number is odd or even

# num = int(input("enter a number:"))

# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# if elif

#check the grade according to the marks

# mark = 90

# if mark >= 90:
#     print("A")
# elif mark >= 80:
#     print("B+")
# elif mark >= 70:
#     print("B")
# elif mark >= 60:
#     print("C+")
# elif mark >= 50:
#     print("C")
# elif mark >= 40:
#     print("D")
# else:
#     print("Fail")


#chech if a numbe is positive,negative or zero

# num = int(input("enter a num:-"))

# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")

# logical operators ( and , or , not )

# and

# a = 2
# if a > 1 and a < 3 and a == 2:
#     print("yes")

# a = 3
# if a > 1 and a < 4 and a == 2:
#     print("yes")

# or

# a = 7
# if a > 6 or a < 8 or a == 7:
#     print("yes")

# a = 6
# if a > 6 or a < 8 or a == 7:
#     print("yes")

# not

# name = ("mohan")
# if name == ("mohan"):
#     print("its mohan")

# name = ("mohan")
# if not name == ("mohan"):
#     print("its mohan")

#find num greater than 3 numbers

num1 =int(input("enter a num:"))
num2 =int(input("enter a num:"))
num3 =int(input("enter a num:"))

if num1 > num2 and num1 > num3:
    print("num1 is greater")
elif num2 > num1 and num2 > num3:
    print("num2 is greater")
else:
    print("num3 is greater")