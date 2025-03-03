"""
Arithmetic operators
+ addition        %modulus ( tells remiander)
- subtraction     / division
* multiplication  ** exponentiation (2 to  the power 10 -- 2**10)
// floor division
"""
#----------------------Arth. Operators-------------------------------
print(2+2)
print(2-2)
print(2*2)
print(34%3)
print(10/2)
print(2**10)
print (9//2)
#-------------------COMPARISON OPERATORS---------------
"""
< lesser than   <= less than equal to
> greater than  >= greater than equal to
!= not equal    == equal to
"""
print(3>2)
print(3>=2)
print(3<2)
print(3<=2)
print(2==2)
print(4!=4)
#---------------------LOGICAL OPERATORS-----------------------------
a=(4==4 and 3>1)
print(a)

b=(4!=4 or 3>1)
print(b)

c=not(4==4 and 3>1)
print(c)
#---------------------ASSIGNMENT OPERATORS----------------------------
score = 1
print(score)
score += 1
print(score)
score *=5
print(score)
score-=2
print(score)
#-----------------------IDENTITY OPERATORS-----------------------------

a=123
b="1234"
print(a is b)
c=123
d=123
print(c is d)

#----------------------BITWISE OPERATORS-----------------------------
a=10
b=15
print (a&b)
print(a|b)
print (a^b)
print(10>>2)
print(10<<2)
#------------------------MEMBERSHIP OPERATORS--------------------------
a = "hello"
print("p" in a)
print("p" not in a)
print("L" in a)
print("l" in a)
