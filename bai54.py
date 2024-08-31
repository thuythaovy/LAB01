# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:14:06 2024

@author: nguyenthuythaovy 
"""

def in_n_so_fibonacci_loop(n):
  """In ra n số Fibonacci đầu tiên bằng vòng lặp.

  Args:
    n: Số lượng số Fibonacci cần in.
  """

  fib1 = 0
  fib2 = 1
  print(fib1, end=' ')
  print(fib2, end=' ')
  for i in range(2, n):
    fib_next = fib1 + fib2
    print(fib_next, end=' ')
    fib1, fib2 = fib2, fib_next
n = int(input("Nhập số lượng số Fibonacci: "))
in_n_so_fibonacci_loop(n)
