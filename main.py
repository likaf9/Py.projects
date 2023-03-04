a = 1
b = 1.2
c = True
d = "Привет"
e =  (-0.5)**0.5
print("Первая переменная: ", type (a))
print("Вторая переменная: ", type (b))
print("Третья переменная: ", type (c))
print("Четвертая переменная: ", type (d))
print("Пятая переменная: ", type (e))



import sys
max_int = sys.maxsize
sys.float_info = sys.maxsize
print(f'Максимальное INT = {max_int}\nМаксимальное FLOAT = {sys.float_info}')


s = "Я люблю динамическую типизацию!"
print(len(s.encode('cp1251')))
print(len(s.encode('utf8')))
print(len(s.encode('utf16')))
print(len(s.encode('utf32')))


a = 1a = 1
b = 2
f = (a - b) * (a + b)
print(f)
f = a**2 - 2*a*b + b**2
print(f)
f = a**2 + 2*a*b + b**2
print(f)
f= a**3 - 3*a**2*b + 3*a*b**2 - b**3
print(f)
f = a**3 + 3*a**2*b + 3*a*b**2 - b**3
print(f)
f= (a + b)*(a**2 + a*b + b**2)
print(f)
f = (a - b)*(a**2 + a*b + b**2)
print(f)


a = 1
b = 2
c = 3
f = ((((a * a) + ((a + c)**2) / (10 * b))- (c**2 * a * 4))**(-1/2))



number = 0.1
while number <= 0.3:
    number += 0.1
    print(number)
number = round(number, 1)
print(number)
