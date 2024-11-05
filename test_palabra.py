#test_palabra.py

import pytest
from palabra import corregir_palabra

# Casos de prueba
@pytest.mark.parametrize("s, expected", [
    ("HoUse", "house"),
    ("ViP", "VIP"),
    ("maTRIx", "matrix"),
])
def test_corregir_palabra(s, expected):
    assert corregir_palabra(s) == expected
