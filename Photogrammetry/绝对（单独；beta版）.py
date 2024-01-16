from numpy import *
from math import *
xtp=[0 for x in range(55)]
ytp=[0 for x in range(55)]
ztp=[0 for x in range(55)]
x=[0 for x in range(55)]
y=[0 for x in range(55)]
z=[0 for x in range(55)]
############重心化改正
xg=sum(x)/55
yg=sum(y)/55
zg=sum(z)/55
############读取控制点并重心化改正
f=open('C:/Users/lenovo/Desktop/bundleadjustment_SCBA_Point_Result.scbapts','r')
line=f.readlines()
for i in range(0,55):
    num=i*8+2   #每隔一个点读取均匀分布的55个点
    strtemp=line[num].strip().split()
    print(strtemp[2])
    xtp[i]=float(strtemp[1])#地面摄测坐标
    ytp[i]=float(strtemp[2])
    ztp[i]=float(strtemp[3])
    xtpg=sum(xtp)/55
    ytpg=sum(ytp)/55
    ztpg=sum(ztp)/55
    xtp[i]=float(strtemp[1])-xtpg#地面摄测坐标
    ytp[i]=float(strtemp[2])-ytpg
    ztp[i]=float(strtemp[3])-ztpg
    x[i]-=xg#模型点
    y[i]-=yg
    z[i]-=zg
########################初值设定
t=0#计时器
while(True):
    phy0=0
    omega0=0
    kapa0=0
    rho=1
    deltax=0
    deltat=0
    deltaz=0
    a1=math.cos(phy0)*math.cos(kapa0)-math.sin(phy0)*math.sin(omega0)*math.sin(kapa0)
    a2=-math.cos(phy0)*math.sin(kapa0)-math.sin(phy0)*math.sin(omega0)*math.cos(kapa0)
    a3=-math.sin(phy0)*math.cos(omega0)
    b1=math.cos(omega0)*math.sin(kapa0)
    b2=math.cos(omega0)*math.cos(kapa0)
    b3=-math.sin(omega0)
    c1=math.sin(phy0)*math.cos(kapa0)+math.cos(phy0)*math.sin(omega0)*math.sin(kapa0)
    c2=-math.sin(phy0)*math.sin(kapa0)+math.cos(phy0)*math.sin(omega0)*math.cos(kapa0)
    c3=math.cos(phy0)*math.sin(omega0)
    R=mat([[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]])


    B=[0 for x in range(55)]
    L=[0 for x in range(55)]
    result=[0 for x in range(55)]
    for i in range(0,55):
        B[3*i]=[1,0,0,x[i],-z[i],0,y[i]]
        B[3*i+1]=[0,1,0,y[i],0,-z[i],x[i]]
        B[3*i+2]=[0,0,1,z[i],x[i],y[i],0]
        t1=mat([xtp[i]],[ytp[i]],[ztp[i]])#
        t2=mat([x[i],y[i],z[i]])#有问题
        t2=pho*R*t2
        l=t1-t2
        L[3*i]=[l[0]]
        L[3*i+1]=[l[1]]
        L[3*i+2]=[l[2]]
    Bm=mat(B)
    Lm=mat(L)
    result=(Bm.T*Bm).I*Bm*L
    deltax+=result[0]
    deltat+=result[1]
    deltaz+=result[2]
    rho=(1+result[3])*rho
    phy0+=result[4]
    omega0+=result[5]
    kapa0+=result[6]
    print(result)
    t+=1
    if(t>10):
        break
#########################坐标求算
a1=math.cos(phy0)*math.cos(kapa0)-math.sin(phy0)*math.sin(omega0)*math.sin(kapa0)
a2=-math.cos(phy0)*math.sin(kapa0)-math.sin(phy0)*math.sin(omega0)*math.cos(kapa0)
a3=-math.sin(phy0)*math.cos(omega0)
b1=math.cos(omega0)*math.sin(kapa0)
b2=math.cos(omega0)*math.cos(kapa0)
b3=-math.sin(omega0)
c1=math.sin(phy0)*math.cos(kapa0)+math.cos(phy0)*math.sin(omega0)*math.sin(kapa0)
c2=-math.sin(phy0)*math.sin(kapa0)+math.cos(phy0)*math.sin(omega0)*math.cos(kapa0)
c3=math.cos(phy0)*math.sin(omega0)
R=mat([[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]])
for i in range(0,55):
    temp=mat([x[i],y[i],z[i]])
    temp1=mat([deltax,deltay,deltaz])
    point=rho*R*temp+temp1
print(point)
    






