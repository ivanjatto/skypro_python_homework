def bank(X, Y):
    r = 0.1  
    A = X * (1 + r) ** Y
    return A


X = 1000  
Y = 5  
result = bank(X, Y)
print("Сумма на счету пользователя спустя", Y, "лет будет равна", result, "рублей.")