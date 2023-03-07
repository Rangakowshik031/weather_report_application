import re
pat="[A-Za-z]{1,}"
s="There are five types of Inheritance"
i=re.findall(pat,s)
print(i)


import re
pat=r"^[A-Za-z]{1,}"
s="There are five types of Inheritance"
i=re.findall(pat,s)
print(i)


import re
pat=r"[A-Za-z]{1,}\Z"
s="There are five types of Inheritance"
i=re.findall(pat,s)
print(i)


import re
pat=r"[A-Za-z][A-Za-z]"
s="There are five types of Inheritance"
i=re.findall(pat,s)
print(i)
