import pytest
from caida import calcular_caida

def test_calcular_caida():
    # Caso de prueba del documento
    yo = 18
    vo = 0
    g = -9.8
    intervalo = 0.3
    informacion,tf,vf = calcular_caida(yo,vo,g,intervalo)

    assert tf == pytest.approx(1.92, abs=0.1)
    assert vf == pytest.approx(18.78, abs=0.1)
    
    assert informacion
    assert informacion[0] == pytest.approx([0.0, 18.0, 0.0], abs=0.1)
    assert informacion[1] == pytest.approx([0.3, 17.56, -2.94], abs=0.1)
    # Verificar el último punto
    assert informacion[-1] == pytest.approx([1.80, 2.12, -17.64], abs=0.1)
