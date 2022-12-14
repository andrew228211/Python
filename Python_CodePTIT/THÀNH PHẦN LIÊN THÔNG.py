n,m,k=map(int,input().split())
di= [[0]*(n+1) for i in range(n+1)]
chuaxet=[0]*(n+1)
def dfs(u):
    global n,chuaxet,di
    chuaxet[u]=1
    st=[]
    st.append(u)
    while len(st)>0:
        x=st.pop()
        for i in range(1,n+1):
            if chuaxet[i] == 0 and di[x][i] == 1:
                chuaxet[i]=1
                st.append(i)
for i in range(m):
    u,v=map(int,input().split())
    di[u][v]=1
    di[v][u]=1
dfs(k)
for i in range(1,n+1):
    if chuaxet[i]==0:
        print(i)