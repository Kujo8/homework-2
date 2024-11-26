while True:
    x = float(input("Введите число: "))
   
    if (x > 0) and (x != 7):
        print('Number is positive')
    elif x < 0:
        print('Number is negative')
    elif x == 0:
        print('Number is equal to zero')
    elif x == 7:
        print('Good bye!')
        break  

