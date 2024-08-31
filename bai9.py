# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:10:24 2024

@author: nguyenthuythaovy
"""

a="1. Hủ tiếu"
b="2. Cháo lòng"
c="3. Bánh canh"
d="4. Bún riêu"
e="5. Phở bò"
print("========Menu========")
print(a)
print(b)
print(c)
print(d)
print(e)
print("====================")
x=int(input("Mời nhập lựa chọn (số):"))
if x==1:
    print(a)
    print("====================")
    print("Lựa chọn thành công")
elif x==2:
    print(b) 
    print("====================")
    print("Lựa chọn thành công")
elif x==3:
    print(c)
    print("====================")
    print("Lựa chọn thành công")
elif x==4:
    print(d)
    print("====================")
    print("Lựa chọn thành công")
elif x==5:
    print(e)
    print("====================")
    print("Lựa chọn thành công")
else:
    print("Không có trong menu")
    