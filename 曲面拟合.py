from numpy import *
from math import *
f=open('C:/Users/lenovo/Desktop/pointsBLH.txt','r')
line=f.readlines()
pointname=[0 for x in range(0,18)]
B=[0 for x in range(0,18)]
L=[0 for x in range(0,18)]
f=[0 for x in range(0,18)]
A=[0 for x in range(0,18)]
normalline0=[0 for x in range(0,18)]
for i in range(0,18):
  strtemp=line[i].strip().split('\t')
  pointname[i]=strtemp[0]
  #bi1[i]=strtemp[1]
  #bi2[i]=strtemp[2]
  #bi3[i]=strtemp[3]
  normalline0[i]=float(strtemp[1])
  B[i]=(float(strtemp[2])+float(strtemp[3])/60+float(strtemp[4])/3600)/180*pi
  L[i]=(float(strtemp[5])+float(strtemp[6])/60+float(strtemp[7])/3600)/180*pi
  f[i]=float(strtemp[9])
  
  A[i]=[1,B[i],L[i],B[i]**2,L[i]**2,B[i]*L[i]]
a=mat(A)
f=mat(f)
solution=a.I*f.T#矩阵形成时默认都是行向量，要转为列向量要转置一下.
print('系数a分别为')
print(solution)
v=a*solution-f.T
V=v.T*v
print('PVV=')
print(V[0]*10000)
print('M0=')
print(sqrt(V[0]*10000/(18-6)))
########################################################
print('正确性检查')
a=6378137
b=6356752.3124
e=sqrt((a*a-b*b)/a/a)
f2=open('C:/Users/lenovo/Desktop/xyz.txt','r')
line=f2.readlines()
index=0
for i in range(0,28):
    strtemp=line[i].strip().split('\t')
    print('pointname=%s'%strtemp[0])
    X=float(strtemp[1])
    Y=float(strtemp[2])
    Z=float(strtemp[3])   
    Bq=atan(Z/sqrt(X*X+Y*Y))
    while True:
        N=a/sqrt(1-e*e*sin(Bq)*sin(Bq))
        H=Z/sin(Bq)-N*(1-e*e)
        B1=atan(Z*(N+H)/sqrt(X*X+Y*Y)/(N*(1-e*e)+H))
        if abs(Bq-B1)<0.0000001:
            Bq=B1
            break
        Bq=B1
    N=a/sqrt(1-e*e*sin(Bq)*sin(Bq))
    L0=atan(Y/X)+pi
    H=Z/sin(Bq)-N*(1-e*e)
    Apie=[1,Bq,L0,Bq**2,L0**2,Bq*L0]
    Apie=mat(Apie)
    abnormal=Apie*solution
    normalline=H-abnormal
    print('正常高为%f'%normalline)
    if (strtemp[0]in pointname)==True:
      #print(pointname.index(strtemp[0]))
      print('原正常高为:%f'%normalline0[index])
      delta=normalline-normalline0[index]
      index+=1
      print('此点正常高差值为%f'%delta)






























