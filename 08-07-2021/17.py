import re
pat=r"\b[0-9]+[\s]+[\w]"
s="1 234uyrhkv"
if(re.search(pat,s)):
    print("matched")
else:
    print("non match")
