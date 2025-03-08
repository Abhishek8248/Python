#find sum of even numbers upto 50
add = 0
for i in range (1,51):
    if i % 2 == 0:
        add+=i
        print(add)
#first 20 number and their square
for i in range(1, 21):
    print(i, i * i)

#sum of first 10 odd numbers using while loop
add = 0
n = 0
while n <=20:
    if n %2 != 0:
        add += n
    n +=1
    print(add)

#create billing system at supermarket

while True:
    name = input("Enter customer name")
    total = 0
    while True:
        print("Enter amount and Quantity")
        amount = float(input("Enter amount:"))
        quantity = int(input("Enter number of items"))
        total += amount*quantity
        repeat =input("Do you want to add more items? (yes/no)")
        if repeat == "no" or repeat == "No":
            break
    print("-"*40)
    print("Name", name)
    print("Amount to be paid:", total)
    print("-"*40)
    print("*****happy shopping*****")

    repeat1 = input("Do you want to move to next customer? (yes/no):")
    if repeat1 =="no" or repeat1=="No":
        break
