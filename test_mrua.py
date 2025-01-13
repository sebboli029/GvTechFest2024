import pytest
from mrua import calcular_mrua

def test_calcular_mrua():
    # Caso de prueba del documento
    vo = 30
    angulo = 45
    yo = 1.9
    g = -9.8
    intervalo = 0.5
    informacion, tf, x_max, y_max = calcular_mrua(yo, vo, g, intervalo, angulo)

    assert tf == pytest.approx(4.42, abs=0.1)
    assert x_max == pytest.approx(93.75, abs=0.1)
    assert y_max == pytest.approx(24.85, abs=0.1)
    assert informacion
    assert informacion[0] == pytest.approx([0.0, 0.0, 1.9, 21.21, 21.21], abs=0.1)
    assert informacion[1] == pytest.approx([0.5, 10.61, 11.28, 21.21, 16.31], abs=0.1)
    # Verificar el último punto
    assert informacion[-1] == pytest.approx([4.0, 84.85, 8.35, 21.21, -17.99], abs=0.1)