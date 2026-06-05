#file handling

df=open('data.txt')
print(df.read())



df=open('data.txt')   
print(df.readline())
print(df.readline())
print(df.readline())




with open('data.txt', mode ='r') as mydata:
    print(mydata.read())



with open('data.txt', mode='r') as mydata:
  print(mydata.read())


with open('data.txt', mode='w') as mydata:
  print(mydata.writelines('i am happy2.....'))


with open('data.txt', mode='a') as mydata:
  print(mydata.writelines('i am happy3.....'))



# ask user for input

num1=int(input('enter first number'))
num2=int(input('enter second number'))

try:
  ans=num1/num2
  print(ans)

except Exception as e:
  print(e)



acct1=(input('enter account number'))
mpin=int(input('enter mpin number'))

try:
  if acct1.lower()=="tjsb1234" and mpin=="1234":
   print("successful login")

except Exception as e:
  print("please enter correct details")

pin=int(input("enter the pin"))
if pin==5525:
        print("correct pin")
else:
        print("incorrect pin")         

bal=10000

withdraw=int(input("enter amount to withdraw")) 
try:
    bal=bal-withdraw
    print(bal)


except Exception as e:
     print("insufficient balance")


 

    




