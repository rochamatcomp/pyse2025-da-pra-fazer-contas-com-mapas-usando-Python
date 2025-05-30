"""
Python Sudeste 2025
Dá pra fazer contas com mapas usando Python?
Uma introdução aos dados espaciais com Python.

Álgebra elementar
"""

# https://numexpr.readthedocs.io/en/latest/user_guide.html
import numexpr as ne


def algebra_de_mapas(expressao, **mapas):
    resultado = ne.evaluate(expressao, local_dict=mapas)

    return resultado


# def algebra_de_mapas(mapas, operador, pesos):

#     resultado = operador(*mapas)

#     return resultado
