from collections import deque
from queue import Queue
# Tạo queue
# put là để thêm vào
q=Queue()
q.put(5)
q.put(2)
q.put(3)
#qsize trả về kích thước queue
print(q.qsize())
#get() xóa và trả về phần tử đầu được thêm 
x=q.get()
print(x)
print("kich thuoc con lai cua queue la : ",q.qsize())
#Tạo deque
dq=deque()
dq.append(2)
dq.append(3)
dq.append(4)
print(dq)
#popleft() xóa và trả về phần tử đầu tiên bên trái
x=dq.popleft()
print(x)
print("kich thuoc con lai cua dq la",dq)
#pop xóa và trả về phần tử đầu tiên bên phải
x=dq.pop()
print(x)

