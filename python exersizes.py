print("BILL")
print('......................................................................')
D=int(input('Enter price 1:'))
E=int(input('Enter price 2:'))
F=int(input('Enter price 3:'))
G=int(input('Enter price 4:'))
Bill=(D+E+F+G)
print("Total: "),Bill
Discount=Bill*10/100
Final_Amount= Bill-Discount
if(Bill>100):
    print ("Discounted_Amount: "),Final_Amount
else:
    print("Final_Amount: "),Bill


print ("bill lab tutorial")
print('......................................................................')
H=input("Cashier Name: ")
I=input("Customer: ")
J=int(input("Enter Bill Amount: "))
K=int(input("Discount percentage:"))
print("--------------------------------")
print("            INVOICE             ")
print("--------------------------------")
print("Customer:      "),I
print("Bill Amount:    RS"),J
print("Discount:      "),K,("%")
Total=J*80/100
print("Total:          RS"),Total
print("--------------------------------")
print("Cashier:       "),H
print("--------------------------------")




print("for loop ,")
print('......................................................................')

total = 0
for counter in range(0,101,2):
    total += counter
print ('Total = '), total 


total = 0
for counter in range(1,100,2):
    total += counter
print ('Total = '), total

print('......................................................................')

for i in range(0,51):
    if i==45:
        break
    print(i)
print('......................................................................')
#square
numbers=[1,2,4,6,11,20]
for i in numbers:
    print(i*i)

print('......................................................................')

#while loop
i=1
while i<=10:
    if i==5:
        print('maja 5')
        i=i+1
    else:
        print('maja')
        i=i+1



print("12 hour- 24 hour AM/PM")
print('......................................................................')
S=int(input("Enter Hour:"))
T=int(input("Enter minutes:"))
U=input("AM/PM: ")
if(U=="AM" and S==12):
            print("Time:"),00,":",T
elif(U=="PM" and S==12):
            print("Time:"),12,":",T 
elif(U=="AM"):
    print("Time:"),S,":",T
    
elif(U=="PM"):
    print("Time:"),S+12,":",T
else:
            print("fuck")







print("24 hour- 12 hour AM/PM")
print('......................................................................')
Q=int(input("Enter Hour:"))
R=int(input("Enter minutes:"))
if (Q==0):
            print("Time:"),12,":",R,"AM"
elif (Q<12):
            print("Time:"),Q,":",R,"AM"
elif(Q==12):
            print("Time:"),12,":",R,"PM"
elif(Q<=23):
            print("Time:"),Q-12,":",R,"PM"
else:
            print("not valid")




print("fall time from a height")
print('......................................................................')
N=int(input("Enter the height:"))
M=(2*N/9.8)
O=M**(0.5)
P=round(O,2)
print('Fall time:'),P,"S"





print("Temperature")
print('......................................................................')
L=int(input("Enter the celcious value:"))
M=L*9.0/5.0+32
print("Temperature in Farenheit:"),M,"F"











    
print("subject total ,if function")
print('......................................................................')
A= int(input ("enter Maths marks:"))
B= int(input ("enter Tamil marks:"))
C= int(input ("enter Arabic marks:"))
Total=(A+B+C)
Average=(A+B+C)/3
print("Total="),Total
print("Average="),Average
if (Total>=150):
    print('congatulation you got great passed')
elif (Total>=100):
    print('congatulation you got passed')
else:
    print ('sorry you are fail')
if (Average>50):
    print('great average')
elif (Average >30.33):
    print("nice average")
else:
    print("average should be improved")



