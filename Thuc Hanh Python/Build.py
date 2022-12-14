# import qrcode
# qr=qrcode.QRCode()
# qr.add_data("https://www.hackerrank.com/dashboard")
# qr.make()
# img=qr.make_image()
# img.save('BuildQr.png')
from base64 import encode
from cgitb import html
from email.encoders import encode_base64
from html.entities import html5
import requests
from bs4 import BeautifulSoup   
res=requests.get('https://qldt.ptit.edu.vn/default.aspx?page=gioithieu')
#print(res)
ob=res.text
print(ob)
# dau=ob.find("<table>")
# cuoi=ob.find("</table>")
# ob=ob[dau+7:cuoi]
# ob=ob.replace("<tbody>","")
# ob=ob.replace("</tbody>","")
# ob=ob.replace("<tr","")
# ob=ob.replace("/tr","")
# ob=ob.replace("td","")
# ob=ob.replace("/td","")
# ob=ob.replace(",\n","\n")
# f=open("Data.csv","w",encoding="utf-8")
# f.write(ob)
# f.close()
# print(ob)
# import os
# f=open("e.txt","r")
# for line in f:
#     line=line.strip()
#     print(line)
# import numpy as np
# arr=np.array([[1,2,3,4,5],[1,5,6,7,8,]])
# print(arr)
# print(np.__version__)
# from threading import local
# from turtle import left, title
# import numpy as np
# import matplotlib.pyplot as plt
# x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y=np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.subplot(2,1,1)
# plt.plot(x,y)
# plt.title("Quan li chi tieu")
# plt.xlabel("Ngan sach")
# plt.ylabel("Tien")
# x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y=np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
# plt.subplot(2,1,2)
# plt.plot(x,y)
# y=np.array([5,6,7,8,9])
# mylabels=["Apples","bananas","Cherries","Oranges","Dates"]
# myexplode=[0.2,0,0,0,0]
# plt.pie(y, labels = mylabels, explode = myexplode)
# plt.legend(title="Five Attribute")
# plt.show()
