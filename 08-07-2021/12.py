import re
pat="TS[0-9]{2}[A-Z]{2}[0-9]{4}"
s="TS08EM3444"
#re.search(pat,s)
if(re.search(pat,s)):
    print("matched")
else:
    print("non match")
