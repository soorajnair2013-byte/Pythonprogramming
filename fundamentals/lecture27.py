import numpy as np
import pandas as pd
#create 1d array using series function
a=pd.Series([1,2,3,4])
a


#create 2d array using dataframe
a=pd.Series([1,2,3,4],index=['a','b','c','d'])
a

a=pd.DataFrame([1,2,3,4,5],columns=['Value'],index=['a','b','c','d','e'])
a


data=pd.DataFrame({'India':[10,20,30],
                  'USA':[40,50,60],
                  'UK':[70,80,90]})
data



data['India'].sum(),data['India'].mean(),data["India"].median()


q1=data['India'].quantile(0.25)
q3=data['India'].quantile(0.75)

iqr=q3-q1

uw=q3+1.5*iqr
lw=q1-1.5*iqr

print(q1,q3,iqr,uw,lw)



#calculate skewness and curtosis
skewness_india=data['India'].skew()
skewness_india #--- symmetric dist  data is normally distributed




kurtosis_india=data['India'].kurt()
kurtosis_india



import matplotlib.pyplot as plt
data['India'].plot(kind='kde')
plt.axvline(25,color='red', linestyle='--')
plt.axvline(32.5,color='g', linestyle='--')
plt.axvline(17.5,color='g', linestyle='--')
plt.axvline(0.005,color='b', linestyle='--')
plt.show()



data.head(2)


data.tail(2)


data.sample(frac=1)


# checking dataset information and description stats
data.info()



data.describe()  #checking descriptive stats


#checking null values in dataset using stats graphical method

data.isnull().sum().plot(kind='bar')
plt.title('Null Values')
plt.show()


data.iloc[0,2]


df=pd.DataFrame({'Gender':['Male','Female','Male','Female'],
                 'Station':['Thane','Klayan','Bhandup','Diva'], 
                 'Age':[50,70,90,45],
                 'Salary':[1000,3000,5000,7000]})
df



male_data=df[df['Gender']=='Male']
male_data


female_data=df[df['Gender']=='Female']
female_data

male_data=df[df['Gender']=='Male']
male_data


female_data=df[df['Gender']=='Female']
female_data


df['Gender'].value_counts().plot(kind='pie',autopct='%0.3f',explode=[0.01,0.01])


