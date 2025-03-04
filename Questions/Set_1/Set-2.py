#write a program to check if the number is positive
num=int(input("Enter number here:"))
print("Number is Positive") if (num>=0) else print("Number is negative")

#write a program to check number is even or odd
num=int(input("Enter number here:"))
print("number is  even") if (num%2 ==0) else print("Number is Odd")

#Write a program to calculate area of rectangle.
length=int(input("Enter length here:"))
breadth=int(input("Enter breadth here:"))
area=length*breadth
print(area)

#chec k weather the alphabet is vowel or not
word=input("enter word:")
if (word in "aeiou") or (word in "AEIOU"):
    print("its a vowel")
else:
    print("Its not a vowel")

#weite a program to check if the number is single digit, two  digit and so on upto 5 digit
num= int(input("enter number upto 5 digit:"))

if 9>= num >=0:
    print("Single digit")

elif 99>= num >=10:
    print("Double digit")

elif 999>= num >=100:
    print("Triple digit")

elif 9999 >= num >= 1000:
    print("Four digit")

elif 99990 >= num >= 10000:
    print("Five digit")

else:
    print("Value exceeds!")


