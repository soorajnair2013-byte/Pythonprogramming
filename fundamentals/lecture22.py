import numpy as np
array1=np.array([100,400,700,300,200,100,800,900])
q1=np.percentile(array1,25)
q3=np.percentile(array1,75)


iqr=q3-q1
print('iqr of array1 : ',iqr)

lowerwhisker=(q1-1.5*iqr)
upperwhisker=(q3+1.5*iqr)
print('lower whisker : ',lowerwhisker)
print('upper whisker : ',upperwhisker)





'''
the methods used for evaluation of outliers are as follows:
1.iqr method
2.z-test


note:
1.if the dataset contains outliers check the number of outliers present in the given dataset(95% - measure of disbursion)
2.if the outliers are less tan 5% then we can use capping method
3.if the outliers are more than 5% then we can use iqr method
4.if the outliers are more than 10% then we can use z-test (zscore >=3 or zscore <=3)
5.some people also use winsorization technique to handle outlier
6. as far as possible avoid trimming technique
7. if the dataset is non normal distributed or skewed then better to use iqr method rather than winsorization technique.
8. if dataset is highly skewed then use box-cox technique or yeo jhonson method in order to convert high skewed data into normal distribution.
then only think of outlier treatment decision.
9. u may use shapiro test to check whether dataset is normal distributed or not.


note
zscore can be evaluated as 
z=(x-u)s
u- mean
s-standard devaition


calculate the outliers using z test using scipy module
'''

print(array1)
mean=np.mean(array1)
standard_deviation=np.std(array1)
z_score=(array1-mean)/standard_deviation
print(z_score)




array3=np.array([[1,2,3,4,5,6,7,8,9,10,11,12]])

array3=array3.ravel()
df=array3
q1=np.percentile(df,25)
q3=np.percentile(df,75)

iqr=q3-q1
lowerwhisker=q1-1.5*iqr
upperwhisker=q3+1.5*iqr
print(lowerwhisker)
print(upperwhisker)
array3











import pandas as pd
import scipy as sp
from scipy.stats import zscore
data=[5,2,4.5,4,3,2,6,20,9,2.5,3.5,4.75,6.5,2.5,8,1]

df = pd.DataFrame(data)
df['z_score']=zscore(data)
print(df)