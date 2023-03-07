import re
pat="[-,;]"
s="India GDP showed downfall during year 2020-2021; it is nearly -22.9 GDP, our neighbour country bangladesh has performed better than india even during covid crisis"
sub=" "
i=re.sub(pat,sub,s)
print(i)
