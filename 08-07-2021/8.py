import re
pat=r"\b[789]{1}[0-9]{9}\b"
s="8074311341 1236582555 987987987987 8555846885"
l=re.findall(pat,s)
print(l)
