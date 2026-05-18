i=0
while i<4:
  print(i)
  i=i+1


i=0
while i<4:
  print(i)
  if(i==1):
    print("hello")
  i=i+1


  i=0
while i<=5:
  if i==1:
    print("hello")
    if i==2:
      print("world")

      i=i+2
print(i) 


i = 0
while i==0 and i<5:  
  print(i)
  if i==2:
    print("you win")
    i +=1
  i=i+1
  print(i)  


  num =100
num1=20

print(num+num1)
print(num-num1)
print(num*num1)

#calculator program

name=input("enter the name:")

password=input("enter the passowrd: ")

if name.lower() =="harsh" and password=="1234" :
    num1=float(input("enter the first number :"))
    num2=float(input("enter the second number :"))

    operation= input("enter the operation to be performed: ")

    if operation =='+':
      print(num1+num2)

    elif operation == '-':
      print(num1+num2)

    elif operation == '*':
      print(num1+num2)

    elif operation == '/':
      print(num1+num2)  

    elif operation == '**':
      print(num1+num2)

    else:
      print("enter a valid input..")      


