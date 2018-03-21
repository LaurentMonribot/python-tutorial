#!/usr/bin/env python3
import re

st = '/usr/home:lumberjack'
match = re.match(r'\/(.*)\/(.*):(.*)', st)
print(match.groups())
print(match.groups()[0])

L=[123, 'spam', 1.23]
L+=[4,5,6]
L.append('NI')
L.pop(2)
L.reverse()
print(L)

M = [[1,2,3],[4,5,6],[7,8,9]]
col2 = [row[1] for row in M]
print(col2)
print([row[1] for row in M if row[1]%2==0 ])

diag=[M[i][i] for i in range(3)]
print(diag)
print(list(range(4)))
print(list(range(-6,7,2)))
print([[x**2,x**3] for x in range(4)])

#mylist = []
#[mylist.append(int(input("Please enter a number : "))) for i in range(5)]
#mylist.sort()
#print(mylist)

#la liste comprehension entre parentheses n'est évaluée que lors que l'on utilise l'iterateur next(G)
#G=(sum(row) for row in M)
#avec les crochets, l'évaluation de tous les éléments de la liste est faite d'un seul coup
G=[sum(row) for row in M]
print(G)

D={'food':'spam','quantity':4,'color':'pink','taste':'strawberry'}
print(D['food'])
D['quantity']+=1
print(D)
E={}
E['name']='toto'
E['job']='dev'
E['age']=20
print(E)
Ted=dict(name='test', job='dev', age=48)
print(Ted)
zipping=dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
#zipping=dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40, 3.1415])) Pi n'est jamais pris en compte
#zipping=dict(zip(['name', 'job', 'age', 'address'], ['Bob', 'dev', 40])) address n'est pas rempli
print(zipping)


rec={'name': {'first':'Bob', 'last':'Smith'}, 'jobs':['dev', 'mgr', 'devops'], 'age':40.5}
print(rec['name'])
print(rec['name']['last'])
print(rec['jobs'])
Ks=list(rec.keys())
Ks.sort()
print(Ks)
for key in (Ks):
    print(key, '==>', rec[key])

# sorted(D) équivaut à list(D.keys()).sort
for key in sorted(D):
    print(key, '==>', D[key])

T=(1,2,3,4,5,5,7,8)
print('len(T) ', len(T))
print('T.index(4) ', T.index(4))
print('T.count(5) ', T.count(5))
T=('spam', 3.0, [11,22,33])
print('T.index(3.0) ', T.index(3.0))


f=open('data.txt', 'r')
test=f.read()
f.close()
print(test)


l=[]
mydic={}
#close implicite dans le for
for line in open('data.txt'):
    if 'valeur' == line.split(',')[0] :
        l.append(int(line.split(',')[1]))
l.sort()
mydic={'valeur':l}
print(mydic)



#version avec des types d'objets différents triés par noms :
l0=[]
l1=[]
l2=[]
mydic={}
#close implicite dans le for
for line in open('data.txt'):
        l0.append(line.split(',')[0])
        l1.append(int(line.split(',')[1]))
mydic=dict(zip(l0, l1))
for key in sorted(mydic):
    l2.append(mydic[key])
l0.sort()
mydic=dict(zip(l0, l2))
print(mydic)



print(dir(f))

s='sp\xc4m'
file=open('unidata.txt', 'w', encoding='utf-8')
file.write(s)
file.close()

test=open('unidata.txt', 'r', encoding='utf-8').read()
print(test)

