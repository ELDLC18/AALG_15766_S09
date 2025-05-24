def mult(u,v):
    n = max(len(str(u)),len(str(v)))

    if(n < 10):
        return u * v
    else:
        s = n // 2
        w = u // 10**s
        x = u % 10**s
        y = v // 10**s
        z = v % 10**s
        return mult(w, y) * 10*(2*s) + (mult(w, z) + mult(x, y)) * 10*s + mult(x, z)


num1 = 1234
num2 = 5678

resultado = mult(num1,num2)
print(f"El resultado de {num1} × {num2} es {resultado}")