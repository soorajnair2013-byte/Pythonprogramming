import pandas as pd
import matplotlib.pyplot as plt

year=[2000,2001,2002,2003,2004,2005]
sales=[10000,20000,40000,60000,80000,90000]
plt.plot(year,sales)
plt.xlabel('sales')
plt.ylabel('year')
plt.title('sales per year: sales trend analysis')
plt.ylim(0,100000)
plt.grid()
plt.show()




from matplotlib import lines

year=[2000,2001,2002,2003,2004,2005]
sales_Q1=[10000,20000,40000,60000,80000,90000]
sales_Q2=[12000,22000,42000,62000,82000,92000]
plt.plot(year,sales_Q1,label='Q1',linestyle='--',marker='*',color='r')
plt.plot(year,sales_Q2,label='Q2',linestyle='--',marker='.',color='g')
plt.axhline(50000,linestyle='--',color='b')
plt.xlabel('sales')
plt.ylabel('year')
plt.grid()
plt.show()




plt.boxplot([sales_Q1])
plt.xlabel('year')
plt.ylabel('sales')

plt.show()



import numpy as np
data=[(1,3,5,7,9,10,15,1000,2000,5000,-85)]
plt.boxplot(data)
plt.show()


#pie plot
plt.figure(figsize=(7,7))
plt.pie(x=sales_Q1,labels=year,autopct='%0.2f%%')
plt.title('Sales distribution wrt year')
plt.show()

plt.bar(year,sales_Q1,color=['green','yellow','cyan','pink','blue','red'],width=0.7,edgecolor='black')
plt.plot(year,sales_Q1,color='r',linestyle='--')
plt.show()



plt.scatter(sales_Q1,sales_Q2)
plt.xlabel('sales_Q1')
plt.ylabel('sales_Q2')
plt.title('Scatter plot')
plt.show()


