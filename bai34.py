# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:22:50 2024

@author: nguyenthuythaovy 
"""

def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True
n = int(input("Nhập số nguyên dương: "))
if is_prime(n):
  print(n, "là số nguyên tố")
else:
  print(n, "không phải là số nguyên tố")
  