import requests

url="https://example.com"

response=requests.get(url)

print(type(response))
print(response.status_code)
print(response.text)



import requests

url="https://www.aajtak.in/"

response=requests.get(url)

print(type(response))
print(response.status_code)
print(response.text)





from  bs4 import BeautifulSoup

html="""
<h1> product name</h1>
<p class="price">999
"""

soup=BeautifulSoup(html)
price=soup.find('p')

print(price.text)



import requests

from bs4 import BeautifulSoup

page=requests.get("https://www.aajtak.in/")
soup=BeautifulSoup(page.text)

print(soup)

