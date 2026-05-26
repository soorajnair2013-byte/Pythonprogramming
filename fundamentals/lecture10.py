# wap to count vowels present inside a string

s=input("enter the string")
vowels='aeiouAEIOU'

def count_vowels():
  count=0
  for i in s:
    if i in vowels:
      count=count+1
  print(count)


count_vowels()


s=input("enter the string")
vowels='aeiouAEIOU'

def count_vowels():
  count=0
  for i in s:
    if i in vowels:
      count=count+1
  print(count)


c=count_vowels()





def sum(): # return value  the values are global
  num1=100
  num2=200
  num3=num1+num2

  return num3
ans=sum()
ans







num1=int(input("enter  the number1"))
num2=int(input("enter  the number2"))

def sum():
  num3=num1+num2

  return num3

def min():
  num3=num1-num2
  return num3

add=sum()
sub=min()


print(add)
print(sub)





a=int(input("enter  the number1"))
b=int(input("enter  the number2"))
c=int(input("enter  the number3"))

def sum(num1,num2):
  num3=num1+num2

  return num3

def min(num1,num2):
  num3=num1-num2
  return num3

add=sum(a,b)
sub=min(b,c)


print(add)
print(sub)





#fibonacci series


number=int(input("enter the number"))

def fib(n):
  a,b=0,1
  while a<n:
    print(a,end='')
    a,b=b, a+b
  print()

ans=fib(number) 




