import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/titanic_dataset.csv')
df.info()


sns.barplot(data=df,x='Survived',y='Sex',hue='Embarked')

sns.scatterplot(data=df,x='Age',y='Survived',hue='Embarked')


fig,ax=plt.subplots(3,3,figsize=(10,10))
sns.scatterplot(data=df,x='Age',y='Survived',hue='Embarked',ax=ax[0][0])
sns.scatterplot(data=df,x='Age',y='Survived',hue='Sex',ax=ax[0][1])
sns.scatterplot(data=df,x='Age',y='Survived',hue='Pclass',ax=ax[1][0])
sns.scatterplot(data=df,x='Age',y='Survived',hue='IsAlone',ax=ax[1][1])


sns.pairplot(df)



#data cleaning
df.drop(columns=['PassengerId','Name','Ticket','Fare','Cabin','Nationality','Occupation','Deck','Title','TravelPurpose','AgeGroup'],axis=1,inplace=True, errors='ignore')
df



#one hot encoding  pca=principle component analysis
#ordinal encoding  follow order or not
#label encoding  else label

#converting categorial data into numercal data
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for i in df.select_dtypes(include='object'):
  df[i]=le.fit_transform(df[i])
df


sns.heatmap(df.corr())