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
