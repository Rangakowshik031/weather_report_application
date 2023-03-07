import re
pat="[\w]+@+[\w]+[\.]+[\w]{2,}"
pat1="[\w]@+[\w]{2,}.org.in."
s="Myself kowshik and my personal mail id is kowshikranga12@gmail.com and my college mail id kowshik@cbit.org.in."
if(re.search(pat,s) and re.search(pat1,s)):
    print("matched")
else:
    print("non match")
    
