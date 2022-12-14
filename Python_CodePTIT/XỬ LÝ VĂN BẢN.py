from distutils import text_file
import re
from pickle import TRUE
text=""
reg='[\w\s,:]+'
while True:
    try: 
        text += input()            
    except EOFError: break
text=re.findall(reg,text)
for i in text:   
    x = i.lower().split()
    x[0] = x[0].title()
    print(' '.join(x))