import numpy as np
array=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]).reshape(4,5)
array


array[1:3,-2:]


from typing import dataclass_transform
#stats:

'''
1.descriptive:min,max,kurtosis,skewness.std dev., variance,etc.
2.inferential:hypothesis testing, confidence interval
'''

'''
statistics mainly consists of following steps:
collect data
organise the data
summarize data
interpret data/inferential stats
'''

a=[1,4,5,7,4]
a.sort()
a

'''
Central tendency refers to the numerical value that represents the center or typical observation within a dataset.

they are of 3 types:
mean:average value
median:central value
mode: most frequent occuring value


a. mean and median generally used for numerical columns
b.mode generally used for categorical columns

'''


'''for outliers use z test,
'''
'''
when mean=median then such distribution is called norammly distributed dataclass_transformthis distribution is also called symmetric distribution 
'''
'''
note2: mean>median then such distribution is called positively skewed data

note2: mean<median then such distribution is called negatively skewed data

'''
array =np.array([1,2,3,4,5,6,7,8,9,10])
mean=np.mean(array)
print(f'the mean value of array is',mean)
median=np.median(array)
print(f'the median value of array is',median)

#positive skewed data
array1=np.array([100,400,700,300,200,100,800,900])
array1.sort()
array1
mean1=np.mean(array1)
print(f'the mean value of array is',mean1)

median=np.median(array1)
print(f'the median value of array is',median)

'''
trim :directly cut the outliers
cap: cap the value with central tendency mean median or mode
'''



#measurew of dispersion

array1=np.array([100,400,700,300,200,100,800,900])
max_value=np.max(array1)
min_value=np.min(array1)

range=max_value-min_value
print(f'the range of array is',range)



variance=np.var(array1)
print(f'the variance of array is',variance)

std=np.sqrt(variance)
print(std)

std1=np.std(array1)
print(std1)



#calculation for iqr
print(array1)
q1=np.percentile(array1,25)
q3=np.percentile(array1,75)
iqr=q3-q1
print("iqr for array1: ",iqr)