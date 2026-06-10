# step1: data loading/data ingestion

# step2: data exploration: eda / exploratory data analysis

# step3: data cleaning / data preprocessing

# step4: data transformation 

# step5: data modeling

# step6: Results/model deployment

import pandas as pd 

def data_ingestion(data):
  # df = pd.read_csv('data.csv')
  return df

def data_exploration():
  pass

def data_cleaning():
  pass

def data_transformation():
  pass

def data_modeling():
  pass

def model_deployment():
  pass

# define entry point

def main():
  df = data_ingestion('data.csv')
  data_exploration(df)
  data_cleaning(df)
  data_transformation(df)
  data_modeling(df)
  model_deployment(df)

main()



import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://www.aajtak.in/&quot";

# Get HTML content
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

news = []

for link in soup.find_all("a"):
    title = link.text.strip()
    href = link.get("href")

    # Store only valid data
    if title and href:
        news.append([title, href])

df = pd.DataFrame(news, columns=["Title", "URL"])

df = df.drop_duplicates()

df.to_csv("aajtak_news.csv", index=False)

print("CSV file created successfully!")





# numpy
# nupmy is vectorized form of an array
# it is faster in computations
#  vectorized form of an array is N dimensional array

import numpy as np

a=np.array([2])
print(type(a))
print(a.ndim)





import numpy as np

a=np.array([[2,4,6]])
print(type(a))
print(a.ndim)

