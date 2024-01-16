from numpy import *
from math import *
x0=0.4321
y0=0.1174
f=40.9349
f1=-40.9349
#左影像外方位
Xs1=796.0875
Ys1=-141.6018
Zs1=-5.0643
phy1=0.235967
omega1=0.102503
kapa1=-0.041294
#右影像外方位
Xs2=3381.0581
Ys2=-145.7630
Zs2=88.4453
phy2=-0.010207
omega2=0.062306
kapa2=-0.088815
x1=[0 for x in range(55)]
x2=[0 for x in range(55)]
y1=[0 for x in range(55)]
y2=[0 for x in range(55)]
Xa=[0 for x in range(55)]
Ya=[0 for x in range(55)]
Za=[0 for x in range(55)]
xa=[0 for x in range(55)]
ya=[0 for x in range(55)]
za=[0 for x in range(55)]
deltaxa=[0 for x in range(55)]
deltaya=[0 for x in range(55)]
deltaza=[0 for x in range(55)]
##############################计算相机畸变
k1=-5.994e-5
k2=2.927e-8
p1=-2.713e-6
p2=3.156e-6
a=8.447e-5
b=1.237e-4
def deltaasd(x,y,t):
    r=math.sqrt((x-x0)*(x-x0)+(y-y0)*(y-y0))
    t1=(x-x0)*(k1*r*r+k2*r**4)+p1*r*r+p1*2*(x-x0)**2+2*p2*(x-x0)*(y-y0)+a*(x-x0)+b*(y-y0)
    t2=(y-y0)*(k1*r*r+k2*r**4)+p2*r*r+p2*2*(y-y0)**2+2*p1*(x-x0)*(y-y0)
    if t==1:
        return t1    
    else:
        return t2  
###############################读取文件
f=open('C:/Users/lenovo/Desktop/bundleadjustment_SCBA_Point_Result.scbapts','r')
line=f.readlines()
for i in range(0,55):
    num=i*8+4   #每隔一个点读取均匀分布的55个点
    strtemp=line[num].strip().split('\t')
    strtemp1=line[num+1].strip().split('\t')
    strtemp2=line[num-2].strip().split('\t')
    x1[i]=float(strtemp[1])
    y1[i]=float(strtemp[2])
    x2[i]=float(strtemp1[1])
    y2[i]=float(strtemp1[2])
    Xa[i]=float(strtemp2[1])
    Ya[i]=float(strtemp2[2])
    Za[i]=float(strtemp2[3])    
    x1[i]=x1[i]-deltaasd(x1[i],y1[i],1)-x0#畸变改正
    y1[i]=y1[i]-deltaasd(x1[i],y1[i],2)-y0
    x2[i]=x2[i]-deltaasd(x2[i],y2[i],1)-x0
    y2[i]=y2[i]-deltaasd(x2[i],y2[i],2)-y0#x1[0]代表左相片第一个像点坐标，x2[1]代表右相片第二个像点坐标
########################旋转矩阵等初值运算
Bu=Xs2-Xs1
Bv=Ys2-Ys1
Bw=Zs2-Zs1
a1=math.cos(phy1)*math.cos(kapa1)-math.sin(phy1)*math.sin(omega1)*math.sin(kapa1)
a2=-math.cos(phy1)*math.sin(kapa1)-math.sin(phy1)*math.sin(omega1)*math.cos(kapa1)
a3=-math.sin(phy1)*math.cos(omega1)
b1=math.cos(omega1)*math.sin(kapa1)
b2=math.cos(omega1)*math.cos(kapa1)
b3=-math.sin(omega1)
c1=math.sin(phy1)*math.cos(kapa1)+math.cos(phy1)*math.sin(omega1)*math.sin(kapa1)
c2=-math.sin(phy1)*math.sin(kapa1)+math.cos(phy1)*math.sin(omega1)*math.cos(kapa1)
c3=math.cos(phy1)*math.sin(omega1)
R1=mat([[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]])

a1p=math.cos(phy2)*math.cos(kapa2)-math.sin(phy2)*math.sin(omega2)*math.sin(kapa2)
a2p=-math.cos(phy2)*math.sin(kapa2)-math.sin(phy2)*math.sin(omega2)*math.cos(kapa2)
a3p=-math.sin(phy2)*math.cos(omega2)
b1p=math.cos(omega2)*math.sin(kapa2)
b2p=math.cos(omega2)*math.cos(kapa2)
b3p=-math.sin(omega2)
c1p=math.sin(phy2)*math.cos(kapa2)+math.cos(phy2)*math.sin(omega2)*math.sin(kapa2)
c2p=-math.sin(phy2)*math.sin(kapa2)+math.cos(phy2)*math.sin(omega2)*math.cos(kapa2)
c3p=math.cos(phy2)*math.sin(omega2)
R2=mat([[a1p,a2p,a3p],[b1p,b2p,b3p],[c1p,c2p,c3p]])
#################循环部分
for i in range(0,55):
    q1=x1[i]
    q2=y1[i]
    q3=x2[i]
    q4=y2[i]
    P1=mat([[q1],[q2],[f1]])
    P1=R1*P1#处理变成像空间辅助
    P2=mat([[q3],[q4],[f1]])
    P2=R2*P2#处理变成像空间辅助
    N1=(Bu*P2[2,0]-Bw*P2[0,0])/(P1[0,0]*P2[2,0]-P2[0,0]*P1[2,0])
    N2=(Bu*P1[2,0]-Bw*P1[0,0])/(P1[0,0]*P2[2,0]-P2[0,0]*P1[2,0])
    xa[i]=Xs1+Bu+N2*P2[0,0]
    ya[i]=Ys1+Bv+N2*P2[1,0]#Ys1+0.5*(N1*P1[1,0]+N2*P2[1,0]+Bv)
    za[i]=Zs1+Bw+N2*P2[2,0]
    deltaxa[i]=xa[i]-Xa[i]
    deltaya[i]=ya[i]-Ya[i]
    deltaza[i]=za[i]-Za[i]
#print(xa)
#print(ya)
#print(za)
print('x的差值')
print(deltaxa)
print('y的差值')
print(deltaya)
print('z的差值')

print(deltaza)
#def as_num(x):#科学记数法转浮点数
#y='{:.5f}'.format(x) # 5f表示保留5位小数点的float型
#return(y)
##strip函数可以去除读取的空格，制表
#print(R1[0,2])#取出第1行第3列
#print(x1[0])注意这里第一个数存的不是有效数据是0
#dot(a,b)矩阵乘法，transpose（a）转置
#numpy.linalg.det()函数计算输入矩阵的行列式
#numpy.linalg.inv()函数来计算矩阵的逆
#print(U2[2,0]),矩阵调用必须使用中括号
#python矩阵生成为先按生成一个列表（按行存入或按多行存入），列表的每一个元素都是一个列表，也就是之后矩阵的每一行,再调用mat函数转化

