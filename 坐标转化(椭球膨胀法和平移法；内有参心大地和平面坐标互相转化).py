from numpy import *
from math import *
r=206265
a=6378137
b=6356755.2882
f=0.003352810664
#a=6379118
alfa=0.003352810664
epie=sqrt((a*a-b*b)/b/b)
e=sqrt((a*a-b*b)/a/a)
#################################################################
#################################################################
def GaussPositive(B,L):
    a=a+deltaa
    f=alfa+deltaalfa
    DH=19
    L0=6*DH-3 
    L0=L0/180*pi
    b=a*(1-f)
    e1=sqrt((a*a-b*b)/(a*a))
    e2=sqrt((a*a-b*b)/(b*b))
    m=[0 for x in range(5)]   
    n=[0 for x in range(5)]
    m[0]=(1-e1*e1)*a
    m[1]=3*e1*e1*m[0]/2
    m[2]=5*e1*e1*m[1]/4
    m[3]=7*e1*e1*m[2]/6
    m[4]=9*e1*e1*m[3]/8
    n[0]=m[0]+m[1]/2 +3*m[2]/8+5*m[3]/16+35*m[4]/128
    n[1]=m[1]/2+m[2]/2+15*m[3]/32+7*m[4]/16
    n[2]=m[2]/8+3*m[3]/16+7*m[4]/32
    n[3]=m[3]/32+m[4]/16
    n[4]=m[4]/128
    X=n[0]*B-sin(2*B)*n[1]/2+sin(4*B)*n[2]/4+n[3]*sin(6*B)/6+n[4]*sin(8*B)/8
    l=L-L0
    t=tan(B)
    g=e2*cos(B)
    W=sqrt(1-e1*e1*sin(B)*sin(B))
    N=a/W
    xr=X+N*sin(B)*cos(B)*l*l/2+N*sin(B)*pow(cos(B),3)*(5-t*t+9*g*g+4*pow(g,4))*pow(l,4)/24+N*sin(B)*pow(cos(B),5)*(61-58*t*t+pow(t,4))*pow(l,6)/720
    yr=N*cos(B)*l+N*pow(cos(B),3)*(1-t*t+g*g)*pow(l,5)/6+N*pow(cos(B),5)*(5-18*t*t+pow(t,4)+14*g*g-58*g*g*t*t)*pow(l,5)/120
    return xr,yr
####################################################
####################################################
#椭球平移法
print('取高程异常平均值为19m，正常高1000m对应大地高981米')
print('以GPS19作为参考点,椭球平移法转换')
print('已写入xy.txt文件的点号为')
deltaa=0
deltaalfa=0
B1=(39+55/60+55.3451/3600)/180*pi
L1=(113+21/60+24.479/3600)/180*pi
H1=1035.0203
B2=B1
L2=L1
H2=54.0203
N1=a/sqrt(1-e*e*sin(B1)*sin(B1))
x1=(N1+H1)*cos(B1)*cos(L1)
y1=(N1+H1)*cos(B1)*sin(L1)
z1=(N1*(1-e*e)+H1)*sin(B1)
N2=a/sqrt(1-e*e*sin(B2)*sin(B2))
x2=(N2+H2)*cos(B2)*cos(L2)
y2=(N2+H2)*cos(B2)*sin(L2)
z2=(N2*(1-e*e)+H2)*sin(B2)
deltax=x2-x1
deltay=y2-y1
deltaz=z2-z1
f1=open('C:/Users/lenovo/Desktop/xy1.txt','w')
f1.writelines('点名\t x\t\t  y\t\n')
f0=open('C:/Users/lenovo/Desktop/xyz.txt','r')
line=f0.readlines()
for i in range(0,28):
    strtemp=line[i].strip().split('\t')
    print('pointname=%s'%strtemp[0])
    X=float(strtemp[1])+deltax
    Y=float(strtemp[2])+deltay
    Z=float(strtemp[3])+deltaz
    Bpie=atan(Z/sqrt(X*X+Y*Y))
    while True:
        N=a/sqrt(1-e*e*sin(Bpie)*sin(Bpie))
        H=Z/sin(Bpie)-N*(1-e*e)
        B1=atan(Z*(N+H)/sqrt(X*X+Y*Y)/(N*(1-e*e)+H))
        if abs(Bpie-B1)<0.0000001:
            Bpie=B1
            break
        Bpie=B1
    N=a/sqrt(1-e*e*sin(Bpie)*sin(Bpie))
    Lpie=atan(Y/X)+pi
    H=Z/sin(Bpie)-N*(1-e*e)
    (xr,yr)=GaussPositive(Bpie,Lpie)
    f1.writelines('%s\t %f\t  %f\t\n'%(strtemp[0],xr,yr))
f1.close()
#################################################################
#椭球膨胀法:
'''judge=input('选择使用椭球膨胀法0.0')
if judge=='1':
    deltaalfa=0
    deltaa=981
    print('使用椭球膨胀法1')
if judge=='2':
    deltaalfa=0
    deltaa=981/(1-2*alfa*(39+55/60)/pi)
    print('使用椭球膨胀法2')
if judge=='3':
    deltaa=981
    deltaalfa=alfa*(a/(a+deltaa)-1)
    print('使用椭球膨胀法3')
f3=open('C:/Users/lenovo/Desktop/xy4.txt','w')##注意此处用不同的方法时要存到不同的文件
f3.writelines('点名\t x\t\t  y\t\n')
f2=open('C:/Users/lenovo/Desktop/xyz.txt','r')
print('已处理好存入xyz2.txt的点为:')
line=f2.readlines()
for i in range(0,28):
    strtemp=line[i].strip().split('\t')
    print('pointname=%s'%strtemp[0])
    X=float(strtemp[1])
    Y=float(strtemp[2])
    Z=float(strtemp[3])   
    B=atan(Z/sqrt(X*X+Y*Y))
    while True:
        N=a/sqrt(1-e*e*sin(B)*sin(B))
        H=Z/sin(B)-N*(1-e*e)
        B1=atan(Z*(N+H)/sqrt(X*X+Y*Y)/(N*(1-e*e)+H))
        if abs(B-B1)<0.0000001:
            B=B1
            break
        B=B1
    N=a/sqrt(1-e*e*sin(B)*sin(B))
    L=atan(Y/X)+pi
    H=Z/sin(B)-N*(1-e*e)
    v=sqrt(1+epie*epie*cos(B)*cos(B))
    N=(a*a/b)/v
    M=N/v/v
    a2=M*(2-e*e*sin(B)*sin(B))*sin(B)*cos(B)/(M+H)/(1-alfa)
    a4=M*(1-e*e*sin(B*B))*sin(B)*sin(B)/(1-alfa)
    a0=[[0,0],[N*e*e*sin(B)*cos(B)/(M+N)/a,a2],[-N*(1-e*e*sin(B)*sin(B))/a,a4]]
    A=mat(a0)
    result=(A*(mat([deltaa,deltaalfa])).T).T
    #print(result.shape)
    L=L
    B+=result[0,0]
    H+=result[0,1]
    (xr,yr)=GaussPositive(B,L)
    f3.writelines('%s\t %f\t  %f\t\n'%(strtemp[0],xr,yr))
f3.close()'''



























    
