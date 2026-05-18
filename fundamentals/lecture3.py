i=1
while i == 1:
   print(i)
   i=i+1



# i=10
# for(i=1, i<=10, i++):
#  print(i)

for i in range(1,10):
 print(i)


 #for odd number

for i in range(0,21):
 if i% 2==1:
  print(i)



#for even number

for i in range(0,21):
 if i% 2==0:
  print(i)



# string data types along with list

str= ["hello","world","python programming"]
for i in str:
    print (i)


name ='India'
print(type(name))


'''
when any function defined inside a class it is called method of respective class
'''

#methods odf strings 

print(name.capitalize())
print(name.casefold())
print(name.lower())



names=['chandan','suresh','ramesh']
for index, name in enumerate (names):
 print(f"index: {index}, name:{name}")





