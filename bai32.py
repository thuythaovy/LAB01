# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:19:36 2024

@author: nguyenthuythaovy 
"""

def tinh_cuoc_taxi(km):
  cuoc = 0
  if km <= 1:
    cuoc = 15000
  elif km <= 5:
    cuoc = 15000 + (km - 1) * 13500
  else:
    cuoc = 15000 + 4 * 13500 + (km - 5) * 11000
    if km > 120:
      cuoc *= 0.9
  return cuoc
km = float(input("Nhập số km: "))
cuoc = tinh_cuoc_taxi(km)
print("Cước taxi là:", cuoc, "đồng")
