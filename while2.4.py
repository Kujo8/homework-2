q = 0
q_max = 0
q_min = 0
while True:
    a = int(input("Введите число"))
    if a == 7:
        print("Пока") 
        break
    elif a > q_max:
        q_max = a
    elif a < q_min:
        q_min = a 

print('Сумма введенных чисел равна ', q)
print("Максиммальное из введенных чисел это - " , q_max)
print("Минимальное число-", q_min)

