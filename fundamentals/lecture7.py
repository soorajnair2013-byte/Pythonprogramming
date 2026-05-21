even=[]
for i in range(0,11):
  if i % 2==0:
    even.append(i)
print(even)

even1=[i for i in range(0,11) if i%2==0]
print(even1)

odd=[i for i in range(0,11) if i%2!=0]
print(odd)

#square
a=[a**2 for a in range(0,9) if a%2==0]
print(a)


# to upper case
names=["harsh","Devesh","Suraj","Mayur"]
a=[i.upper() for i in names]
a


#Tuple
# tuple is immutable, we cannot add the elemnet nor remove it
# hence the methods of tuple are as follows: index and count
tup=(1,2,3,4,5,6,[1,(2,(3,(4,5,6),7),8),9])

tup[6][1][1][1]
tup[-1][2][-2][-2]


tup=(1,2,3,4,5,6,7)
tup.index(1)
tup.count(1)

#type casting to list
a=tuple([i for i in range(0,21) if i%2==0])
a

num=[1,2,3,4,5,6]
num.sort()

num
num.reverse()
num




