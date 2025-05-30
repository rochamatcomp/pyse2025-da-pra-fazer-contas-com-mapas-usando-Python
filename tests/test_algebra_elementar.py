"""
Python Sudeste 2025
Dá pra fazer contas com mapas usando Python?
Uma introdução aos dados espaciais com Python.

Testes da álgebra elementar
"""

import numpy as np
from pyse2025_da_pra_fazer_contas_com_mapas_usando_python.calculadora import(
    algebra_de_mapas
)

# https://numpy.org/doc/2.2/reference/generated/numpy.set_printoptions.html
# np.set_printoptions(precision=5)


def test_algebra_mapas_dimensao_1_resulta_mapa_dimensao_1():
    precipitacao = np.array([5])
    temperatura = np.array([4])
    esperado = np.array([22])

    expressao = "2*precipitacao + 3*temperatura"

    resultado = algebra_de_mapas(
        expressao=expressao,
        precipitacao=precipitacao,
        temperatura=temperatura
    )

    assert resultado.shape == esperado.shape
    assert resultado == esperado


def test_algebra_mapas_valor_float_resulta_valor_nao_exato():
    precipitacao = np.array([5.2])
    temperatura = np.array([4.3])
    esperado = np.array([23.3])

    expressao = "2*precipitacao + 3*temperatura"

    resultado = algebra_de_mapas(
        expressao=expressao,
        precipitacao=precipitacao,
        temperatura=temperatura
    )

    assert resultado.shape == esperado.shape

    # valor não exato
    assert resultado != esperado

    # valor próximo
    # https://numpy.org/doc/stable/reference/generated/
    # numpy.testing.assert_allclose.html
    np.testing.assert_allclose(resultado, esperado)
