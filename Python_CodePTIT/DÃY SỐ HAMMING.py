a=[]
def Haming():
    global a
    i = 1
    while i <= 10**18:
        j = 1
        while j <= 10**18:
            k = 1
            while k <= 10**18:
                a += [i * j * k]
                k *= 5
            j *= 3
        i *= 2
Haming()
a.sort()   
def binSearch(l, r, x):
    if l > r:
        return 'Not in sequence'    
    m = (l + r) // 2
    if a[m] == x:
        return m + 1
    if a[m] < x:
        return binSearch(m + 1, r, x)
    return binSearch(l, m - 1, x) 
for _ in range(int(input())):
    n=int(input())
    # try:
    #     print(a.index(n)+1)
    # except:
    #     print("Not in sequence")
    print(binSearch(0, len(a), n))
    