import re

pattern = '^t[a-z]*|\st[a-z]*'
text= 'Tom,does this Text match the pattern?'

matches=re.finditer(pattern,text)
for match in matches:
    print(text[match.start():match.end()])

matches1=re.findall(pattern,text,re.I)
print(matches1)