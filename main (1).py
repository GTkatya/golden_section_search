import math 
 
def f(x): 
    return 0.309*x**3 + (-7.950*x**2) + 27.738*x - 20.946 
 # Золотое сечение 
def golden_section_search(a, b, epsilon): 
    phi = (1 + math.sqrt(5)) / 2  
    x1 = b - (b - a) / phi 
    x2 = a + (b - a) / phi 
 
    while abs(b - a) > epsilon: 
        if f(x1) < f(x2): 
            b = x2 
        else: 
            a = x1 
 
        x1 = b - (b - a) / phi 
        x2 = a + (b - a) / phi 
 
    return (a + b) / 2 
 
# Задаю начальные параметры 
a = 1.4 
b = 3.2 
epsilon = 0.01 #exp = 0.01 
 
# Вызываем функцию для поиска точки минимума 
minimum_point = golden_section_search(a, b, epsilon) 
 
# Выводим результат 
print("Точка минимума функции:", minimum_point) 
print("Значение функции в точке минимума:", f(minimum_point))