import numpy as np
import pandas as pd

df = pd.DataFrame({
    'Name':['A','B','C','D','E','F'],
    'Department':['HR','IT','SALES','HR','IT','SALES'],
    'Age':[42,46,56,50,27,39],
    'Salary':[1000,4000,6000,8000,3000,9000],
    'Experience':[2,4,6,3,5,7]
})

df




from collections import OrderedDict

stats=[]
for i in df.select_dtypes(exclude='object'):
  print(i)

  numerical_stats=OrderedDict({
      'Feature':i,
      'count':df[i].count(),
      'min':df[i].min(),
      'max':df[i].max(),
      'mean':df[i].mean(),
      'median':df[i].median(),
      'Q1':df[i].quantile(0.25),
      'Q3':df[i].quantile(0.75),
      'IQR':df[i].quantile(0.75)-df[i].quantile(0.25),
      'var':df[i].var(),
      'UW':df[i].quantile(0.25)-1.5*(df[i].quantile(0.75)-df[i].quantile(0.25)),
      'LW':df[i].quantile(0.75)+1.5*(df[i].quantile(0.75)-df[i].quantile(0.25)),
      'std':df[i].std(),
      'skew':df[i].skew(),
      'kurtosis':df[i].kurtosis()
  })
  stats.append(numerical_stats)
  report=pd.DataFrame(stats)


report





df = pd.DataFrame({
    'Name':['A','B','C',np.nan,'E',np.nan],
    'Department':['HR','IT','SALES','HR',np.nan,np.nan],
    'Age':[42,46,56,50,np.nan,np.nan],
    'Salary':[1000,4000,6000,8000,np.nan,np.nan],
    'Experience':[2,4,6,3,5,7]
})

import matplotlib.pyplot as plt
df.isnull().sum().plot(kind='bar')
plt.title('Missing Values')
plt.show()





#imputing null values using fillna

df['Salary']=df['Salary'].fillna(df['Salary'].median())
df['Age']=df['Age'].fillna(df['Age'].median())
df['Name']=df['Name'].fillna('x')
df['Department']=df['Department'].fillna(df['Department'].mode()[0])

df


import pandas as pd
import numpy as np


employee_data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Karan', 'Neha', 'Vijay', 'Pooja', 'Rohit', 'Anjali'],
    'Age': [25, 30, np.nan, 28, 35, np.nan, 40, 29, 31, 27],
    'Department': ['HR', 'IT', 'Finance', np.nan, 'IT', 'HR', 'Finance', 'Marketing', np.nan, 'IT'],
    'Salary': [45000, 60000, 55000, np.nan, 70000, 48000, np.nan, 52000, 61000, 58000],
    'Experience': [2, 5, 4, 3, np.nan, 2, 10, 4, 6, np.nan],
    'Performance_Rating': [4.5, 4.8, np.nan, 4.2, 4.9, 4.1, 5.0, np.nan, 4.6, 4.3]
}


df = pd.DataFrame(employee_data)

df



#checking info abot dataset

from collections import OrderedDict

stats=[]
for i in df.select_dtypes(exclude='object'):
  print(i)
  numerical_stats=OrderedDict({
      'Feature':i,
      'count':df[i].count(),
      'min':df[i].min(),
      'max':df[i].max(),
      'mean':df[i].mean(),
      'median':df[i].median(),
      'Q1':df[i].quantile(0.25),
      'Q3':df[i].quantile(0.75),
      'IQR':df[i].quantile(0.75)-df[i].quantile(0.25),
      'var':df[i].var(),
      'UW':df[i].quantile(0.25)-1.5*(df[i].quantile(0.75)-df[i].quantile(0.25)),
      'LW':df[i].quantile(0.75)+1.5*(df[i].quantile(0.75)-df[i].quantile(0.25)),
      'std':df[i].std(),
      'skew':df[i].skew(),
      'kurtosis':df[i].kurtosis()
  })
  stats.append(numerical_stats)
  report=pd.DataFrame(stats)
report

stats_cat=[]
for i in df.select_dtypes(include='object'):
  categorical_stat=OrderedDict({
    'Feature':i,
    'Count':df[i].count(),
    'Mode':df[i].mode()[0],
    'Null val Count':df[i].isnull().sum()
    

  })
  stats_cat.append(categorical_stat)
  cat_report=pd.DataFrame(stats_cat)

cat_report