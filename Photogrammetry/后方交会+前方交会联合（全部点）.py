from numpy import *
from math import *
with open(r'C:\Users\lenovo\Desktop\摄影测量学编程数据及说明\bundleadjustment_SCBA_Camera_Result.scbacmr') as c:  #读取相机信息
    Camera=c.readline()
    contents=c.readline()
    lineData=contents.strip().split('\t')
    x0=0.4321
    y0=0.1174
    f_dis=40.9349 
    Pixel=0.009             #像素大小
    k1=-5.994e-5              #径向畸变差参数k1
    k2=2.927e-8              #径向畸变差参数k2
    p1=-2.713e-6               #切向畸变差参数p1
    p2=3.156e-6               #切向畸变差参数p2
    Alpha=8.447e-5           #像元仿射变换参数α
    Beta=1.237e-4             #像元仿射变换参数β

with open(r'C:\Users\lenovo\Desktop\摄影测量学编程数据及说明\bundleadjustment_SCBA_Photo_Result.scbapht') as u:
    u.readline()
    contents=u.readline()
    lineData=contents.strip().split('\t')
    print(lineData)
    Xs0_left=float(lineData[0])
    Ys0_left=float(lineData[1])
    Zs0_left=float(lineData[2])
    Phi0_left=float(lineData[3])
    Omega0_left=float(lineData[4])
    Kappa0_left=float(lineData[5])
    contents=u.readline()
    #print(contents)
    lineData=contents.strip().split('\t')
    print(lineData)
    Xs0_right=float(lineData[0])
    Ys0_right=float(lineData[1])
    Zs0_right=float(lineData[2])
    Phi0_right=float(lineData[4])
    Omega0_right=float(lineData[5])
    Kappa0_right=float(lineData[6])



def rotate_mat(Phi0_left,Omega0_left,Kappa0_left):
    a1_l=cos(Phi0_left)*cos(Kappa0_left)-sin(Phi0_left)*sin(Omega0_left)*sin(Kappa0_left)
    a2_l=-cos(Phi0_left)*sin(Kappa0_left)-sin(Phi0_left)*sin(Omega0_left)*cos(Kappa0_left)
    a3_l=-sin(Phi0_left)*cos(Omega0_left)
    b1_l=cos(Omega0_left)*sin(Kappa0_left)
    b2_l=cos(Omega0_left)*cos(Kappa0_left)
    b3_l=-sin(Omega0_left)
    c1_l=sin(Phi0_left)*cos(Kappa0_left)+cos(Phi0_left)*sin(Omega0_left)*sin(Kappa0_left)
    c2_l=-sin(Phi0_left)*sin(Kappa0_left)+cos(Phi0_left)*sin(Omega0_left)*cos(Kappa0_left)
    c3_l=cos(Phi0_left)*cos(Omega0_left)
    return mat([[a1_l,a2_l,a3_l],[b1_l,b2_l,b3_l],[c1_l,c2_l,c3_l]])


for i in range(5):
    with open(r'C:\Users\lenovo\Desktop\bundleadjustment_SCBA_Point_Result.scbapts') as f:
        a1_l=cos(Phi0_left)*cos(Kappa0_left)-sin(Phi0_left)*sin(Omega0_left)*sin(Kappa0_left)
        a2_l=-cos(Phi0_left)*sin(Kappa0_left)-sin(Phi0_left)*sin(Omega0_left)*cos(Kappa0_left)
        a3_l=-sin(Phi0_left)*cos(Omega0_left)
        b1_l=cos(Omega0_left)*sin(Kappa0_left)
        b2_l=cos(Omega0_left)*cos(Kappa0_left)
        b3_l=-sin(Omega0_left)
        c1_l=sin(Phi0_left)*cos(Kappa0_left)+cos(Phi0_left)*sin(Omega0_left)*sin(Kappa0_left)
        c2_l=-sin(Phi0_left)*sin(Kappa0_left)+cos(Phi0_left)*sin(Omega0_left)*cos(Kappa0_left)
        c3_l=cos(Phi0_left)*cos(Omega0_left)
        a1_r=cos(Phi0_right)*cos(Kappa0_right)-sin(Phi0_right)*sin(Omega0_right)*sin(Kappa0_right)
        a2_r=-cos(Phi0_right)*sin(Kappa0_right)-sin(Phi0_right)*sin(Omega0_right)*cos(Kappa0_right)
        a3_r=-sin(Phi0_right)*cos(Omega0_right)
        b1_r=cos(Omega0_right)*sin(Kappa0_right)
        b2_r=cos(Omega0_right)*cos(Kappa0_right)
        b3_r=-sin(Omega0_right)
        c1_r=sin(Phi0_right)*cos(Kappa0_right)+cos(Phi0_right)*sin(Omega0_right)*sin(Kappa0_right)
        c2_r=-sin(Phi0_right)*sin(Kappa0_right)+cos(Phi0_right)*sin(Omega0_right)*cos(Kappa0_right)
        c3_r=cos(Phi0_right)*cos(Omega0_right)

        contents = f.readline()
        lineData=contents.strip( ).split('\t')
        Point_Num = int(lineData[0])
        f.readline()
        id=[]
        L_l=[]
        L_r=[]
        A_l=[]
        A_r=[]
        #print (Point_Num)
        for i in range(58):
            Data=f.readline()
            Point_Data=Data.strip().split('\t')
            Point_Name=int(Point_Data[0])
            XA=float(Point_Data[1])
            YA=float(Point_Data[2])
            ZA=float(Point_Data[3])
            id.append([Point_Name])
            f.readline()

        
            Data=f.readline()
            Point_Data=Data.strip().split('\t')
            x=float(Point_Data[1])
            y=float(Point_Data[2])
            r=sqrt((x-x0)*(x-x0)+(y-y0)*(y-y0))
            delta_x=(x-x0)*(k1*r*r+k2*r*r*r*r)+p1*(r*r+2*(x-x0)*(x-x0))+2*p2*(x-x0)*(y-y0)+Alpha*(x-x0)+Beta*(y-y0)
            delta_y=(y-y0)*(k1*r*r+k2*r*r*r*r)+p2*(r*r+2*(y-y0)*(y-y0))+2*p1*(x-x0)*(y-y0)
            x_appro=-f_dis*(a1_l*(XA-Xs0_left)+b1_l*(YA-Ys0_left)+c1_l*(ZA-Zs0_left))/(a3_l*(XA-Xs0_left)+b3_l*(YA-Ys0_left)+c3_l*(ZA-Zs0_left))
            y_appro=-f_dis*(a2_l*(XA-Xs0_left)+b2_l*(YA-Ys0_left)+c2_l*(ZA-Zs0_left))/(a3_l*(XA-Xs0_left)+b3_l*(YA-Ys0_left)+c3_l*(ZA-Zs0_left))
            x_cor=x-x0-delta_x
            y_cor=y-y0-delta_y
            L_l.append([x_cor-x_appro])
            L_l.append([y_cor-y_appro])
            X=XA-Xs0_left
            Y=YA-Ys0_left
            Z=ZA-Zs0_left
            X_ba=a1_l*(XA-Xs0_left)+b1_l*(YA-Ys0_left)+c1_l*(ZA-Zs0_left)
            Y_ba=a2_l*(XA-Xs0_left)+b2_l*(YA-Ys0_left)+c2_l*(ZA-Zs0_left)
            Z_ba=a3_l*(XA-Xs0_left)+b3_l*(YA-Ys0_left)+c3_l*(ZA-Zs0_left)
            a11=(a1_l*f_dis+a3_l*(x_cor))/Z_ba
            a12=(b1_l*f_dis+b3_l*(x_cor))/Z_ba
            a13=(c1_l*f_dis+c3_l*(x_cor))/Z_ba
            a21=(a2_l*f_dis+a3_l*(y_cor))/Z_ba
            a22=(b2_l*f_dis+b3_l*(y_cor))/Z_ba
            a23=(c2_l*f_dis+c3_l*(y_cor))/Z_ba
            a14=(y_cor)*sin(Omega0_left)-cos(Omega0_left)*((x_cor)*(cos(Kappa0_left)*(x_cor)-sin(Kappa0_left)*(y_cor))/f_dis+f_dis*cos(Kappa0_left))
            a15=-f_dis*sin(Kappa0_left)-(x_cor)/f_dis*((x_cor)*sin(Kappa0_left)+(y_cor)*cos(Kappa0_left))
            a16=y_cor
            a24=-(x_cor)*sin(Omega0_left)-cos(Omega0_left)*((y_cor)*((cos(Kappa0_left)*(x_cor)-sin(Kappa0_left)*(y_cor)))/f_dis-f_dis*sin(Kappa0_left))
            a25=-f_dis*cos(Kappa0_left)-(y_cor)/f_dis*((x_cor)*sin(Kappa0_left)+(y_cor)*cos(Kappa0_left))
            a26=-(x_cor)
            A_l.append([a11,a12,a13,a14,a15,a16])
            A_l.append([a21,a22,a23,a24,a25,a26])        
            Data=f.readline()
            Point_Data=Data.strip().split('\t')
            x=float(Point_Data[1])
            y=float(Point_Data[2])
            r=sqrt((x-x0)*(x-x0)+(y-y0)*(y-y0))
            delta_x=(x-x0)*(k1*r*r+k2*r*r*r*r)+p1*(r*r+2*(x-x0)*(x-x0))+2*p2*(x-x0)*(y-y0)+Alpha*(x-x0)+Beta*(y-y0)
            delta_y=(y-y0)*(k1*r*r+k2*r*r*r*r)+p2*(r*r+2*(y-y0)*(y-y0))+2*p1*(x-x0)*(y-y0)
            x_appro=-f_dis*(a1_r*(XA-Xs0_right)+b1_r*(YA-Ys0_right)+c1_r*(ZA-Zs0_right))/(a3_r*(XA-Xs0_right)+b3_r*(YA-Ys0_right)+c3_r*(ZA-Zs0_right))
            y_appro=-f_dis*(a2_r*(XA-Xs0_right)+b2_r*(YA-Ys0_right)+c2_r*(ZA-Zs0_right))/(a3_r*(XA-Xs0_right)+b3_r*(YA-Ys0_right)+c3_r*(ZA-Zs0_right))
            x_cor=x-x0-delta_x
            y_cor=y-y0-delta_y
            L_r.append([x_cor-x_appro])
            L_r.append([y_cor-y_appro])
            X=XA-Xs0_right
            Y=YA-Ys0_right
            Z=ZA-Zs0_right
            X_ba=a1_r*(XA-Xs0_right)+b1_r*(YA-Ys0_right)+c1_r*(ZA-Zs0_right)
            Y_ba=a2_r*(XA-Xs0_right)+b2_r*(YA-Ys0_right)+c2_r*(ZA-Zs0_right)
            Z_ba=a3_r*(XA-Xs0_right)+b3_r*(YA-Ys0_right)+c3_r*(ZA-Zs0_right)
            a11=(a1_r*f_dis+a3_r*(x_cor))/Z_ba
            a12=(b1_r*f_dis+b3_r*(x_cor))/Z_ba
            a13=(c1_r*f_dis+c3_r*(x_cor))/Z_ba
            a21=(a2_r*f_dis+a3_r*(y_cor))/Z_ba
            a22=(b2_r*f_dis+b3_r*(y_cor))/Z_ba
            a23=(c2_r*f_dis+c3_r*(y_cor))/Z_ba
            a14=(y_cor)*sin(Omega0_right)-cos(Omega0_right)*((x_cor)*((cos(Kappa0_right)*(x_cor)-sin(Kappa0_right)*(y_cor)))/f_dis+f_dis*cos(Kappa0_right))
            a15=-f_dis*sin(Kappa0_right)-(x_cor)/f_dis*((x_cor)*sin(Kappa0_right)+(y_cor)*cos(Kappa0_right))
            a16=y_cor
            a24=-(x_cor)*sin(Omega0_right)-cos(Omega0_right)*((y_cor)*((cos(Kappa0_right)*(x_cor)-sin(Kappa0_right)*(y_cor)))/f_dis-f_dis*sin(Kappa0_right))
            a25=-f_dis*cos(Kappa0_right)-(y_cor)/f_dis*((x_cor)*sin(Kappa0_right)+(y_cor)*cos(Kappa0_right))
            a26=-(x_cor)
            A_r.append([a11,a12,a13,a14,a15,a16])
            A_r.append([a21,a22,a23,a24,a25,a26])

        A_l=mat(A_l)
        A_r=mat(A_r)
        L_l=mat(L_l)
        L_r=mat(L_r)
        X_l=(A_l.T*A_l).I*A_l.T*L_l
        X_r=(A_r.T*A_r).I*A_r.T*L_r
        #print (X_l)
        #print (X_r)
        X_l=array(X_l)
        X_r=array(X_r)
        Xs0_left+=X_l[0][0]
        Ys0_left+=X_l[1][0]
        Zs0_left+=X_l[2][0]
        Phi0_left+=X_l[3][0]
        Omega0_left+=X_l[4][0]
        Kappa0_left+=X_l[5][0]
        Xs0_right+=X_r[0][0]
        Ys0_right+=X_r[1][0]
        Zs0_right+=X_r[2][0]
        Phi0_right+=X_r[3][0]
        Omega0_right+=X_r[4][0]
        Kappa0_right+=X_r[5][0]
        f.close()

print('Xs0_left=%f'%Xs0_left,'Ys0_left=%f'%Ys0_left,'Zs0_left=%f'%Zs0_left,'Phi0_left=%f'%Phi0_left,'Omega0_left=%f'%Omega0_left,'Kappa0_left=%f'%Kappa0_left)
print(Xs0_right,Ys0_right,Zs0_right,Phi0_right,Omega0_right,Kappa0_right)

BX=Xs0_right-Xs0_left
BY=Ys0_right-Ys0_left
BZ=Zs0_right-Zs0_left

R_left=rotate_mat(Phi0_left,Omega0_left,Kappa0_left)
R_right=rotate_mat(Phi0_right,Omega0_right,Kappa0_right)


    
with open(r'C:\Users\lenovo\Desktop\bundleadjustment_SCBA_Point_Result.scbapts') as f:
    contents = f.readline()
    lineData=contents.strip( ).split('\t')
    Point_Num = int(lineData[0])
    f.readline()
    id=[]
    #print (Point_Num)
    for i in range(Point_Num):
        f.readline()
        f.readline()
        Data=f.readline()
        Point_Data=Data.strip().split('\t')
        x=float(Point_Data[1])
        y=float(Point_Data[2])
        r=sqrt((x-x0)*(x-x0)+(y-y0)*(y-y0))
        delta_x=(x-x0)*(k1*r*r+k2*r*r*r*r)+p1*(r*r+2*(x-x0)*(x-x0))+2*p2*(x-x0)*(y-y0)+Alpha*(x-x0)+Beta*(y-y0)
        delta_y=(y-y0)*(k1*r*r+k2*r*r*r*r)+p2*(r*r+2*(y-y0)*(y-y0))+2*p1*(x-x0)*(y-y0)
        x1=float(Point_Data[1])-x0-delta_x
        y1=float(Point_Data[2])-y0-delta_y
        Coo1=R_left*mat([[x1],[y1],[-f_dis]])#矩阵[X1,Y1,Z1].T
        Coo1=array(Coo1)
        X1=Coo1[0][0]
        Y1=Coo1[1][0]
        Z1=Coo1[2][0]

        Data=f.readline()
        Point_Data=Data.strip().split('\t')
        x=float(Point_Data[1])
        y=float(Point_Data[2])
        r=sqrt((x-x0)*(x-x0)+(y-y0)*(y-y0))
        delta_x=(x-x0)*(k1*r*r+k2*r*r*r*r)+p1*(r*r+2*(x-x0)*(x-x0))+2*p2*(x-x0)*(y-y0)+Alpha*(x-x0)+Beta*(y-y0)
        delta_y=(y-y0)*(k1*r*r+k2*r*r*r*r)+p2*(r*r+2*(y-y0)*(y-y0))+2*p1*(x-x0)*(y-y0)
        x2=float(Point_Data[1])-x0-delta_x
        y2=float(Point_Data[2])-y0-delta_y
        Coo2=R_right*mat([[x2],[y2],[-f_dis]])
        Coo2=array(Coo2)
        X2=Coo2[0][0]
        Y2=Coo2[1][0]
        Z2=Coo2[2][0]

        N1=(BX*Z2-BZ*X2)/(X1*Z2-Z1*X2)
        N2=(BX*Z1-BZ*X1)/(X1*Z2-Z1*X2)

        X=Xs0_left+N1*X1
        Y=Ys0_left+0.5*(N1*Y1+N2*Y2+BY)
        Z=Zs0_left+N1*Z1
        print('前方交会结果点')
        print(X,Y,Z)

        
    
