lst=[]
lst1=[1,2,3,'India',456.464]
lst2=[123,[1234,4343,43432]]
lst3=[10.20,(10,20,30),{1,2,3},{"a":[839849]}]

lst.append(10)
lst.append([20,30])
lst.insert(0,2)
a=lst.copy()
lst.extend([40,50,60])
lst.index([20,30])
lst.pop()
lst.remove(40)
print(lst)
lst.count(10)





lst4=[1,2,3,43,2]
lst4.remove(2)
print(lst4)
lst4.pop()

lst.clear()
print(lst)


even=[]
odd=[]
for i in range(0,21):
  if i%2==0:
    even.append(i)
  else:
      odd.append(i)
print(even)
print(odd) 


lst=[1,2,3,4,[4,[5,6,7[100,20[40,50,60],90],900],9000,(10,20),1000],1]
# 40 
# 90
# 50 60