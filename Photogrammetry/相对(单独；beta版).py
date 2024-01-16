from numpy import *
from math import *
x0=0.4321
y0=0.1174
f=40.9349
f1=-40.9349
#exe=1e-2#精度
#左影像外方位
Xs1=0
Ys1=0
Zs1=0
phy1=0
omega1=0
kapa1=0
#右影像外方位，设所求初元素的值全为1
Bx=0.3*5616*0.009
m=1
n=1
By=Bx*m
Bz=Bx*n
phy2=1
omega2=1
kapa2=1
x1=[0 for x in range(55)]
x2=[0 for x in range(55)]
y1=[0 for x in range(55)]
y2=[0 for x in range(55)]
A=[0 for x in range(55)]
q=[0 for x in range(55)]
###############################
#计算相机畸变
#def as_num(x):#科学记数法转浮点数，转换函数
#   y='{:.5f}'.format(x) # 5f表示保留5位小数点的float型
#    return(y)
k1=-5.994e-5
k2=2.927e-8
p1=-2.713e-6
p2=3.156e-6
a=8.447e-5
b=1.237e-4
def delta(x,y,t):
    r=math.sqrt((x-x0)*(x-x0)+(y-y0)*(y-y0))
    t1=(x-x0)*(k1*r*r+k2*r**4)+p1*r*r+p1*2*(x-x0)**2+2*p2*(x-x0)*(y-y0)+a*(x-x0)+b*(y-y0)
    t2=(y-y0)*(k1*r*r+k2*r**4)+p2*r*r+p2*2*(y-y0)**2+2*p1*(x-x0)*(y-y0)
    if t==1:
        return t1    
    else:
        return t2  
#############################读入数据以及相机改正
x1=[0 for x in range(55)]
x2=[0 for x in range(55)]
y1=[0 for x in range(55)]
y2=[0 for x in range(55)]
f=open('C:/Users/lenovo/Desktop/bundleadjustment_SCBA_Point_Result.scbapts','r')
line=f.readlines()
for i in range(0,55):
    num=i*8+4   #每隔一个点读取均匀分布的55个点
    strtemp=line[num].strip().split('\t')
    strtemp1=line[num+1].strip().split('\t')
    x1[i]=float(strtemp[1])
    y1[i]=float(strtemp[2])
    x2[i]=float(strtemp1[1])
    y2[i]=float(strtemp1[2])
    x1[i]-=delta(x1[i],y1[i],1)-x0#畸变改正
    y1[i]-=delta(x1[i],y1[i],2)-y0
    x2[i]-=delta(x2[i],y2[i],1)-x0
    y2[i]-=delta(x2[i],y2[i],2)-y0
#x1[0]代表左相片第一个像点坐标，x2[1]代表右相片第二个像点坐标
####################################像空间辅助
t=0#计数器
while(t<5): #t<7:#循环100次很不靠谱，必须得使用精度限制，循环到大概7次左右就开始发散了
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
    for i in range (0,55):#55            
        P1=mat([[x1[i]],[y1[i]],[f1]])#左相片像空间（辅助）
        P2=mat([[x2[i]],[y2[i]],[f1]])#右相片像空间
        #print(shape(P1))检测,P1为三行一列
        P2=dot(R2,P2)#右相片像空间辅助
        N1=(Bx*P2[2,0]-Bz*P2[0,0])/(P1[0,0]*P2[2,0]-P2[0,0]*P1[2,0])
        N2=(Bx*P1[2,0]-Bz*P1[0,0])/(P1[0,0]*P2[2,0]-P2[0,0]*P1[2,0])
        q[i]=[N1*P1[1,0]-N2*P2[1,0]-By]        
        A[i]=[Bx,-P2[1,0]/P2[2,0]*Bx,-P2[0,0]*P2[1,0]/P2[2,0]*N2,-(P2[2,0]+P2[1,0]*P2[1,0]/P2[2,0])*N2,P2[0,0]*N2]
    qmat=mat(q)  
    Amat=mat(A)    
    result=(Amat.T*Amat).I*Amat.T*qmat
    #print(shape(Amat.T*qmat))
    m+=result[0,0]
    n+=result[1,0]
    phy2+=result[2,0]
    omega2+=result[3,0]
    kapa2+=result[4,0]
    print(m)
    print(n)
    print(phy2)
    print(omega2)
    print(kapa2)
    print(result)
    #
    #if((abs(result[2,0])<exe)and(abs(result[3,0])<exe)and(abs(result[4,0])<exe)):
        #break
    t+=1
print("循环次数:%d"%t)
V=Amat*result-qmat
S0=math.sqrt(V.T*V/50)
print('S0=',S0)
#pop=(Amat.T*Amat).I      
#print(pop)
#mi=S0*math.sqrt(pop)
#print('mi=',mi)
print('Bx=',Bx)
print('By=',Bx*m)
print('Bz=',Bx*n)
print('phy2=',phy2)
print('omega2=',omega2)
print('kapa2=',kapa2)




