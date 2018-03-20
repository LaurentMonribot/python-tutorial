#!/usr/bin/env python3
import sys
#import mylib
from mylib import title
print(sys.platform)
print('Hello world')
print(2**100)
x='Spam'
print(x*8)
x+= "1234567"
print(x)
#print(mylib.title)
print(title)
print(1.5*4)


t=6.982
d=19.7
v=d/t
s="la vitesse est de {:.4f} m/s"
print(s.format(v))

vers=sys.version_info
strVersion = str(vers)
texte= 'version :'
for i in (0,1,2,3,4):
    texte=texte + "  " + strVersion.split('(')[1].split(')')[0].split(',')[i].split('=')[1]
print(texte)


v2=[str(x) for x in vers]
print(v2)

version=".".join(str(x) for x in vers)
print("Hello python (version " + version + ")" )
