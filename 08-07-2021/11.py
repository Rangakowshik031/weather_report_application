import re
pat="[A-Z]+[\w]{1,}"
s="There are 5 types of Inheritance"
s1=re.findall(pat,s)
print(s1)
