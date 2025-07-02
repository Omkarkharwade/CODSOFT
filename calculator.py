print("SIMPLE CALCULATOR")
num1=float(input("enter the number 1 "))
num2=float(input("enter the number 2 "))

print(" press 1 for add\n press 2 for sub\n press 3 for multiply\n press 4 for division")
choice=int(input("enter the choice "))

if choice==1:
 print(num1+num2)
elif choice==2:
 print(num1-num2) 
elif choice==3:
 print(num1*num2) 
elif choice==4:
 print(float(num1/num2)) 
else :
 print("invalid number") 