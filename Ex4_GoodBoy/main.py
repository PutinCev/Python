# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 13:22:55 2025

@author: TBG
"""

print("Введите количество наборов данных")
t = int(input())
for НомерНабора in range(t):
    print(f"Введите количество чисел в наборе №{НомерНабора+1}")
    n = int(input())
    digits = []
    for НомерПозицииВНаборе in range(n):
        print("Введите число в набор")
        ЧислоВНаборе = int(input())
        digits.append(ЧислоВНаборе)
      
    
    max_surprise = 0
    for i in range(n):
        new_digits = digits.copy()
        new_digits[i] += 1
        product = 1
        for d in new_digits:
            product *= d
            if product > max_surprise:
                max_surprise = product
                
    print(f"Максимальное произведение, которое может получить Славик, добавив 1 к ровно одной из своих цифр в этом наборе {max_surprise}")