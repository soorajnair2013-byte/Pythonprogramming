import re
import numpy as np
import pandas as pd

# escape characters in python
# \t :tab
# \n :new line


sentence= "\t\t\t\t Hello world.."
print(sentence)


sentence1= "\n\t\t\n\t hello world"
print(sentence1)



import re
text_to_search="""Regular expressions are extremely useful"""

pattern =re.compile(r'e')
matches=pattern.finditer(text_to_search)
for match in matches:
  print(match)




#for numbers 
import re
text_to_search="""Regular expressions 2009 are extremely useful 2009"""

pattern =re.compile(r'2009')
matches=pattern.finditer(text_to_search)
for match in matches:
  print(match)



import re

text="""
customer name: rahul sharma
im 25 years old
the phone number is 7977507987
order id: ord36515
delivery expected in 3 days
"""
result=re.findall("[0-9]",text)
a=set(result)
print(a)


import re

text="""
Customer name: Rahul Sharma
im 25 years old
the Phone Number is 7977507987
order id: Ord36515
Delivery expected in 3 days
"""
result=re.findall("[A-Z]",text)

pattern =re.compile(r's')
matches=pattern.finditer(text_to_search)
for match in matches:

 print(matches)  




