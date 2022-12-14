from pickle import TRUE
import queue


while TRUE:
    x=int(input())
    if x==0:
        break
    q=queue.Queue()
    cnt=0
    q.put(x)
    while not(q.empty()):
        k= q.get()
        cnt+=1
        if k==1: break
        if(k%2==0): q.put(int(k/2))
        else : q.put(3*k+1)
    print(cnt)
