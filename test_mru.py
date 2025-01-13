import pytest
from mru import calcular_mru

def test_calcular_mru():
    # Caso de prueba del documento
    xo = 0
    v = 12.7
    tiempo_total = 6.3
    intervalo = 0.6
    informacion = calcular_mru(xo,v,tiempo_total,intervalo)

    assert informacion
    assert informacion[0] == pytest.approx([0.0, 0.0], abs=0.1)
    assert informacion[1] == pytest.approx([0.6, 7.62], abs=0.1)
    # Verificar el último punto
    assert informacion[-1] == pytest.approx([6.00, 76.20], abs=0.1)
