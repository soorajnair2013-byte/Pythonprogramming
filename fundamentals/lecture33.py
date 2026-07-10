import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging #----loging is a libray
#feacture means columns
#higher feacture less prediction score


logging.basicConfig(level=logging.INFO, #----record hoga whatever we write
                    filemode='w',#---overwrite
                    filename='Model.log',#---file createed
                    format='%(asctime)s  - %(message)s',
                    force=True)

# df.sample(frac=1)

logging.info('EDA process started')




#checking dataset info
df=pd.read_csv('/content/titanic_dataset.csv')
df.info()


#missing value info using graplical method
df.isnull().sum().plot(kind='barh',color='lightgray')
plt.ylabel('datacolumns')
plt.xlabel('Data values')
plt.title('missing value info')
plt.show()



#checking duplicate record in dataset
df.duplicated().sum()

#segregate categorical and numerical
cat_col=df.select_dtypes(include='object').columns
num_col=df.select_dtypes(exclude='object')

print(cat_col)
print(num_col)




#observations:
# 1.the dataset contains 10000 rows and 20 colums
# 2.out of 20 columns 9 best features selected based on domain knowledge
# sex,embarked,pclass,age,siblingsp,parch,family size,isalone and survived
# 3.considering sex and embarked both are nominal data so we can encode with
#  label encoding ie converting categorical data into numerical
#  checking descriptive statistics using orderdict function
# 4.based on numerical descriptive stats it was observed that all numerical columns are non normal distribution

from collections import OrderedDict
stats=[]
for i in df.select_dtypes(exclude='object'):
  print(i)
  num_col=OrderedDict({
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
  stats.append(num_col)
  report=pd.DataFrame(stats)
report







scat_col=[]
for i in df.select_dtypes(include='object'):
  cat_num=OrderedDict({
    'Feature':i,
    'Count':df[i].count(),
    'Mode':df[i].mode()[0],
    'Null val Count':df[i].isnull().sum()
    

  })
  scat_col.append(cat_num)
  cat_report=pd.DataFrame(scat_col)

cat_report



#using group by function 
df.groupby('Sex')['Fare'].mean()


df.groupby('Sex')['Age'].mean()

pd.crosstab(index=[df['Sex'],df['Survived']], columns=[df['Pclass'], df['Embarked']], margins=True)


pd.crosstab(index=[df['Sex'],df['Survived']], columns=[df['Pclass'], df['Embarked']], margins=True).plot(kind='bar', stacked=True, figsize=(20,5))

