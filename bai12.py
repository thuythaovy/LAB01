# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:45:45 2024

@author: nguyenthuythaovy
"""

import random
a=int(input("Yêu cầu số nguyên (1) hay yêu cầu số thực (2): "))
if a==1:
    so_ngau_nhien_a = random.randint(0, 100)
    print("Số ngẫu nhiên từ 0 đến 100:", so_ngau_nhien_a)
    so_ngau_nhien_b = random.randint(50, 99)
    print("Số ngẫu nhiên từ 50 đến 99:", so_ngau_nhien_b)
    so_ngau_nhien_c = random.randint(-39, 79)
    print("Số ngẫu nhiên từ -39 đến 79:", so_ngau_nhien_c)
    so_ngau_nhien_d = random.randint(-79, -39)
    print("Số ngẫu nhiên từ -79 đến -39:", so_ngau_nhien_d)
elif a==2:
    so_ngau_nhien_a = random.uniform(0, 100)
    print("Số ngẫu nhiên từ 0 đến 100:", so_ngau_nhien_a)
    so_ngau_nhien_b = random.uniform(50, 99)
    print("Số ngẫu nhiên từ 50 đến 99:", so_ngau_nhien_b)
    so_ngau_nhien_c = random.uniform(-39, 79)
    print("Số ngẫu nhiên từ -39 đến 79:", so_ngau_nhien_c)
    so_ngau_nhien_d = random.uniform(-79, -39)
    print("Số ngẫu nhiên từ -79 đến -39:", so_ngau_nhien_d)
else:
    print("Chỉ nhập 1 hoặc 2")
    