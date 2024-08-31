# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:41:47 2024

@author: nguyenthuythaovy 
"""

import math

def tinh(hinh, tinh, *args, **kwargs):
    """Hàm tính chu vi hoặc diện tích của các hình.

    Args:
        hinh (str): Loại hình (vuong, chu_nhat, tron).
        tinh (str): Phép tính (cv: chu vi, dt: diện tích).
        *args: Các tham số vị trí bổ sung (ví dụ: cạnh hình vuông).
        **kwargs: Các tham số từ khóa bổ sung (ví dụ: bán kính hình tròn).

    Returns:
        Số thực: Kết quả tính toán.
    """

    if hinh == 'vuong':
        canh = args[0]
        if tinh == 'cv':
            return 4 * canh
        elif tinh == 'dt':
            return canh * canh
    elif hinh == 'chu_nhat':
        chieu_dai, chieu_rong = args
        if tinh == 'cv':
            return 2 * (chieu_dai + chieu_rong)
        elif tinh == 'dt':
            return chieu_dai * chieu_rong
    elif hinh == 'tron':
        ban_kinh = kwargs.get('ban_kinh')
        if tinh == 'cv':
            return 2 * math.pi * ban_kinh
        elif tinh == 'dt':
            return math.pi * ban_kinh**2
    else:
        return "Hình không hợp lệ"
while True:
    hinh = input("Nhập hình (vuong, chu_nhat, tron, hoặc exit để thoát): ")
    if hinh.lower() == 'exit':
        break
    phep_tinh = input("Nhập phép tính (cv: chu vi, dt: diện tích): ")

    if hinh == 'vuong':
        canh = float(input("Nhập độ dài cạnh hình vuông: "))
        ket_qua = tinh(hinh, phep_tinh, canh)
    elif hinh == 'chu_nhat':
        chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
        chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
        ket_qua = tinh(hinh, phep_tinh, chieu_dai, chieu_rong)
    elif hinh == 'tron':
        ban_kinh = float(input("Nhập bán kính hình tròn: "))
        ket_qua = tinh(hinh, phep_tinh, hinh='tron', ban_kinh=ban_kinh)
    else:
        print("Hình không hợp lệ")
        continue

    print("Kết quả:", ket_qua)