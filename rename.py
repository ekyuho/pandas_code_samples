import os
import glob
import re

d=glob.glob('*')
for x in d:
    if re.match('^_\d',x): 
        s1='^_'
        s2=''
        #cmd=f'ren "{x}" "{x.replace(s1,s2)}"'
        cmd=f'ren "{x}" "{x[1:]}"'
        print(cmd)
        os.system(cmd)
