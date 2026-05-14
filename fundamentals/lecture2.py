# conecpt of f string

name="sachin"
age=30
salary=50000

print(f"my name is {name}, my age is {age}, my salary is {salary}")

print("my name is {}, my age is {}, my salary is {}".format(name,age,salary))




# concept of list

lst1=[]
lst2=[1,2,3,4,5.76,"sachin",True,False,[1,2,3],(1,2,3),{"name":"sachin","age":30}]



# control flow

name=(input("enter your name:"))
if name=="sachin":
    print(f"welcome {name}") 


coin_side=input("enter the coin side:")
if coin_side.lower()=="head":
    print("you win")
elif coin_side.lower()=="tail":
    print("i win ")
else:
    print("invalid input")     

#conecpt of indexing and slicing

str="welcome to the world of python programming"
print(str[4])
print(str[-5])
print(str[:])
print(str[3:-1])


'''
ask user to enter a string 
reverse the string 
compare the original string with reversed string
if both are same theen it is palindraome otherwise it is not a palindrome
'''

string=input("enter a string:")
reverse_string=string[::-1] 
if string==reverse_string:
    print(f"{string} is a palindrome")  
else:
    print(f"{string} is not a palindrome")  

