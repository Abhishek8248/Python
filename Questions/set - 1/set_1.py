
#Write a program to display name age and address in 3 different lines.

name="avi"
age = 23
address = "Gurugram"

print(name)
print(age)
print(address)

#swap two variables
#MEATHOD-1
x = 12
y = 13
temp=x
x=y
y=temp
print(x,y)
#MEATHOD-2
a=20
b=30
a,b=b,a
print("value of a",a, "value of b:",b)

#write a program to convert float to integer.

length = 2.45
print(type(length))

length=int(length)
print(type(length))
print(length)

#take data from student for ID cards and print on diffrent line
name=input("Your Name:")
age=int(input("your age is:"))
address=input("write your address:")
course = input("Enter your course:")

print("Student ID card")
print("name:",name)
print("age:",age)
print("address:",address)
print("course:",course)

#take user inout as integer and convert it to float.

a=float(input("Enter your number:"))
print("before converting to int:",a)

a=int(a)
print("after converting it to int:",a)
