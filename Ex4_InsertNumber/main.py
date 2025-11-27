
t = int(input("Введите количество наборов данных: "))
print(t)
for a in range(t):
    n, d = map(int, input("Введите количество разрядов и цифру для вставки через пробел: ").split())
    print(f"{n} {d}")
    
    digits = []  
    inserted = False
    for i in range(n):
        digit = int(input("Введите разряд числа: "))
        if not inserted and digit < d:
            digits.append(d)
            inserted = True
        digits.append(digit) 
    if not inserted:
        digits.append(d)
    
    result_number = ''.join(map(str, digits))
    print(result_number)