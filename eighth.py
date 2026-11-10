# list

# is a collection of Data respresented between []

# students = ["mohan", "sree","suja"]
# print(students)
# print(type(students))

# properties

# can be of any elements at any size
# a = [1,1.1,True,"mohan",[1,2,3,4],1,2,3,4]
# print(a)

# lists are ordered
# a = [1,2,3,4]
# b = [4,3,2,1]
# print(a == b)

#lists are indexed
# starts at zero
# 
# a = [11,12,13,14]
# print (a[0]) 

# name = "mohandas"
# print(name[2])

#also has negative index

# name = "mohandas"
# print(name[-2])

# a = [1,2,3]
# print(a[-2])

#[startindex:stopindex:step]

# b =[1,2,3,4,5,6,7]
# print(b[1:5:1])

# b =[1,2,3,4,5,6,7]
# print(b[:7:])

# b =[1,2,3,4,5,6,7]
# print(b[::])

# b =[1,2,3,4,5,6,7]
# print(b[::-1])

# name = "mohandas"
# print(name[1:5:1])

# name = "mohandas"
# print(name[:5:])

# name = "mohandas"
# print(name[::])

# name = "mohandas"
# print(name[::-1])

# list can be nested

# a = [11,12,13,[100,200,300,["mohan",["hari"],"das"],400]]
# print(a[3])

# a = [11,12,13,[100,200,300,["mohan",["hari"],"das"],400]]
# print(a[3][3])

# a = [11,12,13,[100,200,300,["mohan",["hari"],"das"],400]]
# print(a[3][3][1])

# a = [11,12,13,[100,200,300,["mohan",["hari"],"das"],400]]
# print(a[3][3][1][0])

# lists are mutable

# s = [11,12,13,14,15]
# s[0] = "mohan"
# print(s)

#lists are dynamic

#LIST INBUILD METHODS

#to add we use (append,extend,insert)

# append(item)
# adds item to the end of the list

# a =[11,12,13,14,15,16]
# a.append("mohan")
# print(a)

# a =[11,12,13,14,15,16]
# a.append("100")
# print(a)

#extend
# adds an item to the list

# a =[11,12,13,14,15,16]
# a.extend([17,18,19,20])
# print(a)

# a =[11,12,13,14,15,16]
# a.extend("mohan")
# print(a)

#insert(index[item])

# a =[11,12,13,14,15,16]
# a.insert(0,[2,5,7,8])
# print(a)

# a =[11,12,13,14,15,16]
# a.insert(0,"mohan")
# print(a)

#delete

# remove(item)

# a =[11,12,13,14,15,16,16]

# pop() removes the item at the end or given item

# pop(index) removes the item from the given index


#tuple
#is immutable

#collection of data

#data = (3,4,5,6,"mohan",3,4)

#cannot do like below 
#data =[0]="das"
# print(data)
# print(data[0])
# print(type(data))