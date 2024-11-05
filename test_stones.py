#test_stones.py

import pytest
from stones import posicion_final

# Casos de prueba
@pytest.mark.parametrize("s, t, expected", [
    ("RGB", "RRR", 2),
    ("RRRBGBRBBB", "BBBRR", 3),
    ("BRRBGBRGRBGRGRRGGBGBGBRGBRGRGGGRBRRRBRBBBGRRRGGBBB", 
     "BBRBGGRGRGBBBRBGRBRBBBBRBRRRBGBBGBBRRBBGGRBRRBRGRB", 
     15),
])
def test_posicion_final(s, t, expected):
    assert posicion_final(s, t) == expected

#@pytest.mark.parametrize("s, t, expected", [...]) define tres nombres de parámetros: s, t y expected.
#Cada uno de estos parámetros representa un valor que pasaremos a la función test_posicion_final.
#La lista entre corchetes ([...]) contiene múltiples tuplas de valores que corresponden a estos parámetros.
