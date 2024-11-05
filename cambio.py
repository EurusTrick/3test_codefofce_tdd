# cambio.py

def min_palas_sin_cambio(k, r):
    for n in range(1, 11):  # Probamos hasta 10 palas como máximo
        total = n * k
        if total % 10 == 0 or total % 10 == r:
            return n

# Lectura de entrada
k, r = map(int, input().strip().split())

# Imprime el número mínimo de palas
print(min_palas_sin_cambio(k, r))
