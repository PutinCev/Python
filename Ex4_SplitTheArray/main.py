# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 18:19:47 2025

@author: TBG
"""
print("Введите количество числовых элементов в исходном массиве")
n = int(input())

digits = []

for i in range(n):
    print(f"Введите числовой элемент массива № {i+1}")
    digit = int(input())
    digits.append(digit)


total_sum = sum(digits)

if total_sum != 0:
    print("YES")
    print(1)
    print(f"1 {n}")
else:
    prefix_sum = 0
    found_index = -1
    for i in range(n):
        prefix_sum += digits[i]
        if prefix_sum != 0:
            found_index = i
            break
    
    if found_index != -1:
        print("YES")
        print(2)
        print(f"1 {found_index + 1}")
        print(f"{found_index + 2} {n}")
    else:
        print("NO")