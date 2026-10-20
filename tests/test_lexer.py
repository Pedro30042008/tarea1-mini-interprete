"""Pruebas del lexer: del texto a los tokens."""

import pytest
from mini_interprete.lexer import tokenizar
from mini_interprete.tokens import Token, TipoToken
from mini_interprete.errores import ErrorDeSintaxis


def test_tokeniza_un_numero_solo():
    assert tokenizar("42") == [Token(TipoToken.NUMERO, 42, 0)]

# Pruebas Agregadas:

# Caso Normal:

def test_tokenizar_numeros_con_ceros_a_la_izquierda():
    assert tokenizar("00001") == [Token(TipoToken.NUMERO, 1, 0)]
    
def test_tokeniza_una_suma():
    assert tokenizar("3+4") == [
        Token(TipoToken.NUMERO, 3, 0),
        Token(TipoToken.MAS, "+", 1),
        Token(TipoToken.NUMERO, 4, 2),
    ]


def test_los_espacios_no_producen_tokens():
    assert len(tokenizar("  3   +   4  ")) == 3


def test_tokeniza_parentesis():
    tipos = [token.tipo for token in tokenizar("(3)")]
    assert tipos == [TipoToken.PAR_IZQ, TipoToken.NUMERO, TipoToken.PAR_DER]

def test_tokeniza_expresion_con_varios_operadores():
    resultado = tokenizar("125 + 30 * 4")

    assert resultado == [
        Token(TipoToken.NUMERO, 125, 0),
        Token(TipoToken.MAS, "+", 4),
        Token(TipoToken.NUMERO, 30, 6),
        Token(TipoToken.POR, "*", 9),
        Token(TipoToken.NUMERO, 4, 11)
    ]

def test_tokeniza_expresion_con_parentesis_y_operadores():
    resultado = tokenizar("(15 - 3) / 4 + 2")

    assert resultado == [
        Token(TipoToken.PAR_IZQ, "(", 0),
        Token(TipoToken.NUMERO, 15, 1),
        Token(TipoToken.MENOS, "-", 4),
        Token(TipoToken.NUMERO, 3, 6),
        Token(TipoToken.PAR_DER, ")", 7),
        Token(TipoToken.ENTRE, "/", 9),
        Token(TipoToken.NUMERO, 4, 11),
        Token(TipoToken.MAS, "+", 13),
        Token(TipoToken.NUMERO, 2, 15)
    ]

def test_rechaza_caracteres_desconocidos():
    resultado = "3 @ + 4"

    with pytest.raises(ErrorDeSintaxis) as error:
        tokenizar(resultado)

    assert error.value.posicion == 2