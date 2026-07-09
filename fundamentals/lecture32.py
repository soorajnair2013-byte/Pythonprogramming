# import data manipulation library
import pandas as pd
import numpy as np

# import data visualization library
import matplotlib.pyplot as plt
import seaborn as sns
df =pd.read_csv('/content/titanic_dataset.csv')
df.head()

plt.bar(df['Embarked'],df['Pclass'],color='grey')
plt.title("Barplot")

plt.xlabel("Embarked")
plt.ylabel("class")
plt.show()








sns.barplot(data=df,x='Embarked',y='Pclass',color='grey')
plt.title("Barplot")

plt.xlabel("Embarked")







year=[2000,2001,2002,2003,2004,2005]
sales_Q1=[10000,20000,40000,60000,80000,90000]
sales_Q2=[12000,22000,42000,62000,82000,92000]



#plotting boxplot using seaborn
a
sns.boxplot(data='sales_Q1')
#sns.boxnplot(data='sales_Q2')
plt.title("Boxplot")
plt.show()


sns.violinplot(data=sales_Q1,color='cyan')
plt.title("Violinplot")
plt.show()


sns.lineplot(x=sales_Q1,y=sales_Q2)
plt.xlabel("sales_Q1")
plt.ylabel("sales_Q2")
plt.title("Lineplot")
plt.show()





sns.scatterplot(x=sales_Q1,y=sales_Q2)
plt.xlabel("sales_Q1")
plt.ylabel("sales_Q2")
plt.title("Scatterplot")
plt.show()
#


sns.regplot(x=sales_Q1,y=sales_Q2)



sns.jointplot(x=sales_Q1,y=sales_Q2)

plt.subplots(2,2)
plt.subplot(2,2,1)
plt.plot(year,sales_Q1)
plt.subplot(2,2,2)
plt.plot(year,sales_Q2)
plt.show()
plt.subplot(2,2,3)
sns.boxplot(data=sales_Q1)
plt.subplot(2,2,4)
plt.plot(data=sales_Q2)
plt.show()