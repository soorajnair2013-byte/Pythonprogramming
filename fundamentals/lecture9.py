e={}  # if no value it is considered as ditionary  treted as none
s={1,2,3}  #if there are value then it is set
print(type(e))
print(type(s))

#dictionary
from builtins import print # Re-import the built-in print function
d1={'india':1000,'usa':3000,'uk':4000}
print(d1.keys())

d1={'india':1000,'india':3000,'uk':4000}
print(d1.keys())

d1.values()

d1.items()

d1.pop('uk')

d2={'name':'india',
    'age':23,
    'gender':'male'}

d2.popitem()
d2

d2.get('name')

d2.update({'name':'Manoj','age':32}) #case sentitive 
d2

d2['age']=42
d2

c=tuple(i for i in range(1,10))
print(c)

