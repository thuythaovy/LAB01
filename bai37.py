# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:26:01 2024

@author: nguyenthuythaovy 
"""

def sum_even_numbers(n):
  return n * (n + 2) // 4
n = int(input("Nhập số nguyên dương chẵn: "))
result = sum_even_numbers(n)
print("Tổng là:", result)
