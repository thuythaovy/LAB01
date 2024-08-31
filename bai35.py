# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:23:49 2024

@author: nguyenthuythaovy 
"""

def sum_natural_numbers(n):
  return n * (n + 1) // 2
n = int(input("Nhập số nguyên dương: "))
result = sum_natural_numbers(n)
print("Tổng là:", result)
