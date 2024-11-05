#stones.py

def posicion_final(s, t):
    posicion = 0  # Posición inicial en base 0

    # Itera sobre cada instrucción en t
    for instruccion in t:
        # Si el color de la piedra actual coincide con la instrucción
        if s[posicion] == instruccion:
            posicion += 1  # Avanza a la siguiente piedra

        # Si ya está en la última piedra, no puede avanzar más
        if posicion >= len(s):
            break

    # Devuelve la posición en base 1
    return posicion + 1

# Lectura de entrada
s = input().strip()
t = input().strip()

# Imprime la posición final
print(posicion_final(s, t))

