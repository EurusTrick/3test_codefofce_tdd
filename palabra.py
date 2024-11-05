#palabra.py

def corregir_palabra(s):
    mayusculas = sum(1 for c in s if c.isupper())
    minusculas = len(s) - mayusculas
    
    # Cambia a mayúsculas si hay más letras mayúsculas, de lo contrario a minúsculas
    if mayusculas > minusculas:
        return s.upper()
    else:
        return s.lower()

# Lectura de entrada
s = input().strip()

# Imprime la palabra corregida
print(corregir_palabra(s))
