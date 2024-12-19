a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = str(input("Введите один из следующих знаков: + - * / "))


if c == "+" :
  print(a + b)
elif c == "-" :
  print(a - b)
elif c == "*" :
  print(a * b)
elif c == "/" : 
  if b !=0:  
    print(a/b)
  else:
        print("Деление на ноль запрещено")
else:
  print("Брат, только 4 операции могу:  + - * /..... ")
