# import data manipulation library
import numpy as numpy
import pandas as pd


df=pd.read_csv('/content/titanic_dataset.csv')

df


#checking dataset info
df.info()

#checking duplicate
df.duplicated().sum()


from collections import OrderedDict

stats=[]

for i in df.select_dtypes(exclude='object'):
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
   


   #descriptive method for ctaegory

# df.describe(include='object)


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


#calculate the percwentage of people who started the jounery from southhamptopn
import matplotlib.pyplot as plt
df['Embarked'].value_counts().plot(
    kind='pie',
    autopct='%0.2f',
    explode=[0.01, 0.01, 0.01]
)


df['Survived'].value_counts().plot(kind='pie', autopct='%0.2f%%', explode=[0.01, 0.01])


south_hampton=df[df['Embarked']=='S']
south_hampton
#south_hampton.to_csv('south_hampton.csv')


south_hampton['Survived'].value_counts()
south_hampton['Pclass'].value_counts()



south_hampton=df[df['Embarked']=='S']

cat=south_hampton['Sex'].value_counts().plot(
    kind='pie',
    autopct='%0.2f',
    explode=[0.01, 0.01,]
)
print('cat')

quint=df[df['Embarked']=='Q']

cat1=quint['Sex'].value_counts().plot(
    kind='pie',
    autopct='%0.2f',
    explode=[0.01, 0.01,]
)

print('cat1')
