#   Tìm số nhóm bạn? Nhóm đông nhất là bao nhiêu ?

#Cách 1: BFS or DFS
'''
from codecs import xmlcharrefreplace_errors
import queue
from re import X
from tkinter import N
from turtle import xcor
import zipapp


if __name__ == "__main__":
    n,m=map(int,input().split())
    a=[[] for i in range(n+5)]
    for i in range (m):
        u, v = map(int, input().split())
        a[u].append(v)
        a[v].append(u)
    d=[0]*(n+5)
    k,res = 0,0
    for i in range(1,n+1):
        if d[i]==0:
            k+=1
            z=1
            d[i]=1
            Q=queue.Queue()
            Q.put(i)
            while Q.qsize():
                u=Q.get()
                for v in a[u]:
                    if d[v]==0:
                        d[v]=1
                        z+=1
                        Q.put(v)
            if z>res: res=z 
    print(k,res,sep="\n")
'''

#   Cách 2: Disjoin Set Union
f=[0]*100005
d=[1]*100005

def getroot(x):
    while f[x]: x=f[x]
    return x

if __name__ == "__main__":
    n,m=map(int,input().split())
    k=n 
    res=0
    for i in range(m):
        u,v=map(int,input().split())
        x=getroot(u)
        y=getroot(v)
        if x!=y:
            while u!=x :
                z=f[u]
                f[u]=x 
                u=z
            while v!=y :
                z=f[v]
                f[v]=x #chu y day van la x
                v=z
            k-=1
            f[y]=x 
            d[x]+=d[y]
            if res<d[x]: res=d[x]
    print(k,res,sep="\n")