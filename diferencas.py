#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys

#######################################################################


def Escalona(x,resp):
 lu=np.zeros((n+1,n+1), float)
 resp2=np.zeros(n, float)
 resp2=resp
 lamda=[]
 moddet=0
 op=0
 for tt in xrange(0, n):
  for t in xrange(tt+1,n):
   #if abs(x.item(tt,tt))<abs(x.item(t,tt)):
   # moddet=moddet+1
   # y=np.copy(x[tt])
   # x[tt]=np.copy(x[t])
   # x[t]=np.copy(y)
   op=op+2+n
   lamda.append(x.item(t,tt)/x.item(tt,tt))
   resp2[t]=resp2[t]-lamda[-1]*resp2[tt]
   x[t]=np.copy(x[t]-lamda[-1]*x[tt])
   lu.itemset((t,tt),lamda[-1])
 for i in xrange(0,n+1):
  lu.itemset((i,i),1)
 return x,lamda,op,resp2,lu



def CalculoDet(x):
 det=1
 for i in xrange(0,n):
  det=det*x.item(i,i)
 return det



def Substitui(x,resp2):
 y=resp2
 for i in xrange(n-1,-1,-1):
  j=n-1
  while (j>i):
   y[i]=y[i]-x.item(i,j)*y[j]
   j=j-1
  y[i]=y[i]/x.item(i,i)
 return y

def Coeficientes(z,y):
 w=np.zeros([n], float)
 for tt in xrange(0,n):
  for t in xrange(0,n):
   w[tt]=np.copy(w[tt]+y[t]*z.item(tt,t))
 return w

def FazTudo(x,resp):
 lu=np.zeros((len(x)+1,len(x)+1), float)
 z=np.copy(x)
 n=len(x)+1
 moddet=0
 x,l,op,resp2,lu=Escalona(x,resp)
 det=CalculoDet(x)
 y=Substitui(x,resp2)
 simply=[ round(elem,2) for elem in y ]
 w=Coeficientes(z,y)
 return simply

##################################################################################


def p(x):
 return 1
def q(x):
 return 2
def r(x):
 return np.cos(x)

def montamatriz(x,y):
 mat=np.zeros((N,N), float)
 vet=np.zeros(N,float)

 mat.itemset((0,0), 2+h**2*q(x[1]))
 mat.itemset((0,1), -1+h/2*p(x[1]))
 vet=[h**2*r(x[1])+(-1-h/2*p(x[1]))*y[0]]
 mat.itemset((N-1,N-1), 2+h**2*q(x[N]))
 mat.itemset((N-1,N-2), -1+h/2*p(x[N]))

 for i in xrange(1,N-1):
  mat.itemset((i,i-1), -1-h/2*p(x[i]))
  mat.itemset((i,i), 2+h**2*q(x[i]))
  mat.itemset((i,i+1), -1+h/2*p(x[i]))
  vet.append(-h**2*r(x[i]))

 vet.append(h**2*r(x[N-1])+(-1-h/2*p(x[N-1]))*yfim)
 return mat, vet
 

yini=-0.3
yfim=-0.1
xini=0
xfim=np.pi/2.
n=N=9
h=(xfim-xini)/float(N+2)
y=[yini]
x=[xini]

for i in xrange(0,N+1):
 x.append(x[-1]+h)
print len(x)

mat,vet=montamatriz(x,y)

#print "mat:"
#for i in xrange(0,N):
# for j in xrange(0,N):
#  print '{:4}'.format(mat[i][j]),
# print '\n'
#
#print "vet:"
#for i in xrange(0,N):
# print str(vet[i])+'\n'
aux=FazTudo(mat,vet)
for i in xrange(0,9):
 y.append(aux[i])
y.append(yfim)

for i,j in zip(x,y):
 print i,j
