"""Del texto a los tokens.

    "3 + 4 * 2"  ->  [NUMERO(3), MAS, NUMERO(4), POR, NUMERO(2)]
"""

from .tokens import Token, TipoToken
from .errores import ErrorDeSintaxis

SIMBOLOS = {
    "+": TipoToken.MAS,
    "-": TipoToken.MENOS,
    "*": TipoToken.POR,
    "/": TipoToken.ENTRE,
    "(": TipoToken.PAR_IZQ,
    ")": TipoToken.PAR_DER,
}


def tokenizar(texto: str) -> list:
    """Parte el texto en tokens."""
    tokens = []
    i = 0
    while i < len(texto):
        caracter = texto[i]

        if caracter.isspace():
            i += 1

        elif caracter.isdigit():
            # Delega la lectura del numero y actualiza la posicion de recorrido.
            token, i = _leer_numero(texto, i)
            tokens.append(token)

        elif caracter in SIMBOLOS:
            tokens.append(Token(SIMBOLOS[caracter], caracter, i))
            i += 1

        else:
            raise ErrorDeSintaxis(
                f"caracter desconocido {caracter!r}",
                i
            )

    return tokens

# Reconoce un numero completo y devuelve su token y la posicion donde termina.
def _leer_numero(texto: str, inicio: int):
    i = inicio

    while i < len(texto) and texto[i].isdigit():
        i += 1

    token = Token(
        TipoToken.NUMERO,
        int(texto[inicio:i]),
        inicio
    )

    return token, i
