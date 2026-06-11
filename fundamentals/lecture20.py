#array.shape  it shows elements arranged in numpy array
import numpy as np
array1=np.array([[1,2,3],[4,5,6]])
array1.shape




array1=np.array([[1,2,3],[4,5,6],[7,8,9]])
array1.shape



#transpose of matrix

array1.T


array1.flatten()   #this will convert multi dimensional into 1-d


array1.sum(axis=1)  # row wise 

array1.sum(axis=0)  # column wise


import numpy as np
array1=np.array([[1,2,3],[4,5,6],[7,8,9]])
array1.shape


array1.max(),array1.min(),array1.mean()


np.eye(5)


np.zeros(3)


np.ones(3)


array2=np.array([[1,2,3],[4,5,6],[7,8,9],[3,6,9]])

array2.reshape(3,4)



a=np.array([[1,2,3],[4,5,6],[7,8,9],[3,6,9]])
b=np.array([[1,2,3],[4,5,6],[7,8,9],[3,6,9]])

c=a+b
print(c)
c*20
c>1


#variance--spread of data
#std deviation-- under root of variance
# deviation of each and every  data points wrt mean

np.array([[1,2,3,4,5,6,7,8,9]]).reshape(3,3)


d=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]).reshape(7,5)
d


d=np.arange(1,36).reshape(7,5)
d

d=np.arange(0,36,2).reshape(3,6)
d


d=np.linspace(0,100,5,dtype='int')
d

# generating random numbers

np.random.seed(0)
np.random.rand(3,3)


f=np.random.randint(low=0,high=2,size=(3,3))
f


f.ravel() 
# perform same task as flatten


# when mean =median the distribution is symmetric also called as noramlly distributed/no skew
# when mean>median the distribution is positively skewed
# when mean<median the distribution is negatively skewed

np.median(f),np.mean(f),np.std(f),np.var(f),np.min(f),np.max(f)











