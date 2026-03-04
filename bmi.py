weight = float(input("Введите вес, кг: "))
height = float(input("Введите рост, см: "))
try:
  weight = float(weight)
  height = float(height)
except ValueError:
  print("Введите корректное значение")
  exit()
bmi = round(weight / height ** 2, 2)
if bmi < 16:
    print(f"Ваш ИМТ: {bmi}; выраженный дефицит массы тела")
elif bmi >= 16 and bmi < 18.5:
    print(f"Ваш ИМТ: {bmi}; недостаточная масса тела")
elif bmi >= 25 and bmi < 30:
    print(f"Ваш ИМТ: {bmi}; избыточная масса тела")
elif bmi >= 30 and bmi < 35:
    print(f"Ваш ИМТ: {bmi}; ожирение 1 степени")
elif bmi >= 35 and bmi < 40:
    print(f"Ваш ИМТ: {bmi}; ожирение 2 степени")
elif bmi > 40:
    print(f"Ваш ИМТ: {bmi}; ожирение З степени")
else:
    print(f"Baш ИМТ: {bmi}; нормальный вес")
