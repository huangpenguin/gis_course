import gc
#A B C D为点
Ns=['A','C','D','B','C','B']#弧-结点拓扑
Ne=['B','A','A','C','D','D']#终点
#Snext={'A':[3,2,1],'B':[4,6,1],'C':[2,5,4],'D':[3,6,5]} 节省内存就不适用字典了，改用函数
A0=[3,2,1,3]
B0=[4,6,1,4]
C0=[2,5,4,2]
D0=[3,6,5,3]
def Snext(t,Line_num):    
    if t=='A':
        return A0[A0.index(Line_num)+1]
    elif t=='B':
        return B0[B0.index(Line_num)+1]
    elif t=='C':
        return C0[C0.index(Line_num)+1]
    else:
        return D0[D0.iindex(Line_num)+1]
    

i=1#计数器
P=list()#面弧拓扑
Snumber=6
Pr=[0 for x in range(Snumber)]#右
Pl=[0 for x in range(Snumber)]#左
for S in range(1,Snumber+1):
    Sc=S;#当前弧段,第i边存在第i-1的多边形列表里
    if(Pr[Sc-1]!=0 and Pl[Sc-1]!=0):#True区分大小写
        continue
    if(Pl[Sc-1]==0):
        temp=list();#创建临时列表储存边数
        temp.append(Sc)
        Pl[Sc-1]=i#第i个多边形
        N0=Ns[Sc-1]
        Nc=Ne[Sc-1]
        while(True):       
            if(N0==Nc):            
                P.append(temp)#第i个多边形生成完成                
                i+=1#开始生成下一个多边形               
                continue
            else:
                #xiayige=Snext[Nc]                
                #xuhao=(xiayige.index(Sc))%3-3+1
                #Sc=xiayige[xuhao]#根据结点读入下一弧段;切片读取
                Sc=Snext(Nc,Sc)#找到下一弧段
                temp.append(Sc)                
                if(Nc==Ns[Sc-1]):
                    Pl[Sc]=i
                    Nc=Ne[Sc-1]                   
                elif(Nc==Ne[Sc-1]):
                    Pr[Sc]=i
                    Nc=Ns[Sc-1]
    else:
        temp=list();#创建临时列表储存边数
        temp.append(Sc)
        Pr[Sc-1]=i
        N0=Ne[Sc-1]
        Nc=Ns[Sc-1]       
        while(True):   
            if(N0==Nc):
                P.append(temp)#第i个多边形生成完成,储存在字典的i-1地址的位置
                i+=1#开始生成下一个多边形
                continue
            else:
                #xiayige=Snext[Nc]
                #xuhao=(xiayige.index(Sc)%3)-3+1
                #Sc=xiayige[xuhao]#根据结点读入下一弧段;切片读取
                Sc=Snext(Nc,Sc)
                temp.append(Sc)
                if(Nc==Ns[Sc-1]):
                    Pl[Sc]=i
                    Nc=Ne[Sc-1]                    
                elif(Nc==Ne[Sc-1]):
                    Pr[Sc]=i
                    Nc=Ns[Sc-1]
print("生成了%d个多边形"%i)
print('面弧拓扑对应为P的数组中的不同元素，如p[0]对应第一个多边形的面弧拓扑')
print('p如下')
print(P)
print('弧面拓扑对应在pl和pr两个中，如pr[0]=1对应1弧段的右多边形为第一个生成的多边形')
print('Pl如下:')
print(Pl)
print('Pr如下:')
print(Pr)



