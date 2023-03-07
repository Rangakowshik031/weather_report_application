import re
s=" into inevitable to onto hello award"
s1=r"\b[aeiou]+[\w]+[aeiou]\b"
l=re.findall(s1,s)
print(l)


