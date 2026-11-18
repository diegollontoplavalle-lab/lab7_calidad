import pytest

from primo import es_primo


# TDD: estas pruebas se escriben primero, antes de implementar es_primo.
@pytest.mark.parametrize("numero", [2, 3, 5, 7, 11, 13, 97])
def test_numeros_primos(numero):
    assert es_primo(numero)


@pytest.mark.parametrize("numero", [4, 6, 9, 15, 100])
def test_numeros_compuestos(numero):
    assert not es_primo(numero)


@pytest.mark.parametrize("numero", [0, 1, -7])
def test_numeros_menores_que_dos_no_son_primos(numero):
    assert not es_primo(numero)