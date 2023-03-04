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



c = [1, 2, 3, 9]
l = [-1, 0.5, -0.45, 4.005]
bl = max(c)
b = max(l)
print("Максимальное INT =", bl, "Максимальное FLOAT =", b)



s = "Я люблю динамическую типизацию!"
print(len(s.encode('cp1251')))
print(len(s.encode('utf8')))
print(len(s.encode('utf16')))
print(len(s.encode('utf32')))