import re
pat=r"[1-9]{2}-[1-12]{2}-[0-9]{4}"
s="my date of joining id 18-11-2021"
l=re.findall(pat,s)
print(l)
