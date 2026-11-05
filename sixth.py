#find the number of digits in a given number

# num = int(input("enter the number:"))
# count = 0
# while num > 0:
#      i = num % 10
#      count = count + 1
#      num =num // 10

# print("no of digits =",count)

# for loop

#for i in range(start,stop,step)

# for i in range(1,11,1):
#      print(i)

# for i in range(1,11):
#     print(i)

# for i in range(11):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

#find sum of first 10 numbers

# sum = 0
# for i in range(1,11,1):
#     sum = sum + i
# print(sum)

#find factorial of a given number

# n = int(input("enter a num:-"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

#find the sum and average of given number 

# count = int(input("enter the count of numbers to find:"))
# sum = 0
# for i in range(1,count + 1):
#     num = int(input("enter a num:"))
#     sum = sum + num

# avg = sum / count
# print("sum",sum)
# print("avg",avg)

#chech if the given number is amstrong or not

num = int(input("Enter the number:"))
orgnum = num
n = num
sum = 0
count = 0
while n != 0:
    count = count + 1
    n = n // 10
print(count)
while orgnum != 0:
    b = orgnum % 10
 
    sum = sum + b ** count
    orgnum = orgnum // 10
print(sum)
print(num)

if num == sum:
    print("Given number is amstrong")
else:
    print("Given number is not amstrong")