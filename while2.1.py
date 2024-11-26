a = int(input("Введите четное число: "))
b = int(input("Введите нечетное число : "))

summ = 0          
summch = 0     
summ9 = 0        

i = a
while i <= b:
    if i % 2 != 0: 
        summ += i
    else:           
        summch += i
    
    if i % 9 == 0:  
        summ9 += i
    
    i += 1 

print("Сумма нечетных чисел: ", summ)
print("Сумма четных чисел: ", summch)
print("Сумма чисел, кратных 9: ", summ9)
