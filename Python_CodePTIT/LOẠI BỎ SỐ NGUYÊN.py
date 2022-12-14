# import os
# def check(s) :
# 	k = 0
# 	for i in s :
# 		if not i.isdigit() :
# 			return True
# 		k = k * 10 + int(i)
# 	if k <= 2147483647 and k >= -2147483648 :
# 		return False
# 	return True

f=open('DATA.in','r')
# a = []
# for line in f:
# 	for i in line.split():
# 		if check(i) : a.append(i)
# for i in sorted(a) :
# 	print(i, end = ' ')
# f.close()
set1=set()
cnt=0
for i in f:
	print(i.lower())
	cnt+=1
	set1.add(i.lower().strip())
print(cnt)
for i in set1:
	print(i)
