import numpy as np
import pandas as pd

df=pd.read_csv('/content/titanic_dataset.csv')
df

south_hampton=df[df['Embarked']=='S']
south_hampton['Survived'].value_counts()
south_hampton['Pclass'].value_counts()


cat=south_hampton['Pclass'].value_counts().plot(
    kind='pie',
    autopct='%0.2f',
    explode=[0.01, 0.01,0.01]
)
print('cat')


south_hampton_survived=south_hampton[(south_hampton['Pclass'])&(south_hampton['Survived']==1)]
south_hampton_survived['Sex'].value_counts()



south_hampton_dead=south_hampton[(south_hampton['Pclass'])&(south_hampton['Survived']==0)]
south_hampton_dead['Sex'].value_counts()



quinstorm=df[df['Embarked']=='Q']
quinstorm_survived=quinstorm[(quinstorm['Pclass'])&(quinstorm['Survived']==0)]
quinstorm['Sex'].value_counts()



pd.crosstab(index=df['Sex'],columns=df['Survived'],margins=True)




pd.crosstab(index=df['Sex'],columns=df['Survived']).plot(kind='bar')


pd.crosstab(index=df['Sex'],columns=df['Survived']).plot(kind='bar')







#import data manipulation library

import numpy as np
import pandas as pd
#import data visualization library
import matplotlib.pyplot as plt
import seaborn as sns
#import warnings
# import warnings
# warnings.filterwarnings('ignore')


#step1: data ingestion
def data_ingestion(data):
  df=pd.read_csv(data)
  return df



#step2: descriptive stats
def descriptive_stats(df):
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
  return report
    


def dataset_information(df):
  info=df.info()
  duplicated_values=df.duplicated().sum()
  null_values=df.isnull().sum()
  return info,duplicated_values,null_values


#crosstab function

def crosstb(row,col):
 crs=pd.crosstab(index=row,columns=col)
 x=crs.plot(kind='bar',figsize=(15,15) )
 plt.show()
 return x


#define entry point
def main():
  filepath='/content/titanic_dataset.csv'
  df=data_ingestion(filepath)
  # df=descriptive_stats(df)
  # info,duplicated_values,null_values=dataset_information(df)
  crs=crosstb(df['Sex'],df['Survived'])
  print(crs)
  

main()


