"""def fatorial(n):
    print(f"Calculando o fatorial de {n}")
    if n == 0 or n == 1:
        print(f"Fatorial de {n} = 1")
        return 1
    else:
        fat = n * fatorial(n - 1)
        print(f"fatorial de {n} = {fat}")
    return fat
fatorial(10)
"""
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n -1) + fibonacci(n -2)
    
fibonacci(5)