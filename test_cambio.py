# test_cambio.py

import pytest
from cambio import min_palas_sin_cambio

# Casos de prueba
@pytest.mark.parametrize("k, r, expected", [
    (117, 3, 9),
    (237, 7, 1),
    (15, 2, 2),
])
def test_min_palas_sin_cambio(k, r, expected):
    assert min_palas_sin_cambio(k, r) == expected
