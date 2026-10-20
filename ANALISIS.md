# Análisis — Tarea 1

**Integrantes:**
1. Alan Gael Alvarez Hernández
2. María Fernanda Miranda Sánchez
3. Pedro Pablo Ruiz Hernández

**Fork:**

https://github.com/Pedro30042008/tarea1-mini-interprete.git

**Rama:**

main
---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?

| Componente | Qué recibe | Qué entrega | De qué es responsable |
|---|---|---|---|
| `lexer` | Cadena de texto | Lista de tokens | Traducir los caracteres de la cadena de texto dada a tokens, los cuales, tienen tipo, valor y posición dentro de la cadena de texto. |
| `parser` | Lista de Tokens | Nodo raíz del AST | Construir la estructura del AST a partir de la lista de Tokens recibida, respetando la precedencia de las operaciones y verificando las reglas de sintaxis planteadas. |
| `ast` | Un valor numérico o un operador definido junto con dos Nodos | Un Nodo `Numero` que contiene un valor numérico o un Nodo `OperacionBinaria` que contiene un operador, un Nodo Izquierdo y un Nodo Derecho. | Definir la estructura de los nodos `Numero` y `OperacionBinaria` que se encuentran dentro del AST. |
| `evaluator` | Nodo raíz del AST | Resultado numérico de la evaluación del AST | Evaluar recursivamente los nodos del AST hasta obtener el resultado de la expresión. |

### 1.2 ¿Qué recorrido sigue una expresión desde que se recibe como texto hasta que produce un resultado?

| Etapa | Cómo se ve `(3 + 4) * 2` aquí |
|---|---|
| texto | `"(3 + 4) * 2"` |
| tokens | [`(PAR_IZQ, "(", 0)`, `(NUMERO, 3, 1)`, `(MAS, "+", 3)`, `(NUMERO, 4, 5)`, `(PAR_DER, ")", 6)`, `(POR, "*", 8)`, `(NUMERO, 2, 10)`] |
| AST | `OperacionBinaria("*", OperacionBinaria("+", Numero(3), Numero(4)), Numero(2))` |
| resultado | 14 |

**AST**

```text
*
├── +
│   ├── 3
│   └── 4
└── 2
```
---

## 2. Las pruebas que ya estaban

### 2.1 ¿Qué pruebas venían incluidas?

| Prueba | Componente | Comportamiento que verifica | ¿Cuántos operadores usa? | ¿Normal, frontera o inválida? |
|---|---|---|---|---|
| `test_tokeniza_un_numero_solo()` | lexer | Verifica que lexer convierta en un único token a un número con varios dígitos `42` | 0 | Normal |
| `test_tokeniza_una_suma()` | lexer | Verifica que lexer produzca tres tokens para la suma de dos numeros `"3+4"` | 1 | Normal |
| `test_los_espacios_no_producen_tokens()` | lexer | Verifica que lexer produzca tres tokens para la expresión `"  3   +   4  "`, sin generar más por los espacios. | 1 | Normal |
| `test_tokeniza_parentesis()` | lexer | Verifica que lexer genere los tokens correspondientes a los paréntesis en `(3)` | 0 | Normal |
| `test_construye_el_arbol_de_una_suma()` | parser | Verifica que parser construya el AST correcto para la suma de dos numeros `"3 + 4"` | 1 | Normal |
| `test_la_multiplicacion_se_agrupa_antes_que_la_suma()` | parser | Verifica que parser construya el AST correcto dado que la multiplicación tiene mayor prioridad en la expresión `"3 + 4 * 2"` | 2 | Normal |
| `test_los_parentesis_cambian_la_agrupacion()` | parser | Verifica que parser construya el AST de `"(3 + 4) * 2"`, respetando la agrupación establecida por los paréntesis. | 2 | Normal |
| `test_suma()` | evaluator | Verifica que la suma de dos números otorgue el resultado correcto `"3 + 4"` | 1 | Normal |
| `test_resta()` | evaluator | Verifica que la resta de dos números otorgue el resultado correcto `"10 - 3"` | 1 | Normal |
| `test_multiplicacion()` | evaluator | Verifica que la multiplicación de dos números otorgue el resultado correcto `"6 * 7"` | 1 | Normal |
| `test_division()` | evaluator | Verifica que la división de `"10 / 2"` sea 5 | 1 | Normal |
| `test_precedencia_sin_parentesis()` | evaluator | Verifica que el resultado de `"3 + 4 * 2"` sea 11, respetando la precedencia de la multiplicación. | 2 | Normal |
| `test_precedencia_con_parentesis()` | evaluator | Verifica que el resultado de `"(3 + 4) * 2"` sea 14, realizando primero la operación entre paréntesis. | 2 | Normal |


### 2.2 ¿Qué comportamientos **no** estaban probados?

- La precedencia de operadores en expresiones que incluyan en conjunto los operadores de suma, resta, multiplicación y división.

- La asociatividad de operadores del mismo nivel de precedencia, especialmente cuando aparecen varias restas o divisiones consecutivas.

- Agregar 0's antes de un número es válido; por ejemplo `007` es `7`.

- El comportamiento ante entradas inválidas, como números decimales en la entrada, operadores mal colocados, expresiones incompletas, cadena vacía o caracteres desconocidos.

- El comportamiento de expresiones cuando utilizan múltiples paréntesis, incluyendo agrupaciones anidadas y paréntesis sin cerrar.	

- La división entre cero debe reportarse como `ErrorDeEvaluacion`.

- El comportamiento de la división cuando el resultado no es un número entero.

---

## 3. Las pruebas que agregaron

### 3.1 ¿Cuáles son casos normales, cuáles frontera y cuáles inválidos?

| Prueba (archivo::nombre) | Entrada | Esperado | Categoría | ¿Por qué esa categoría? |
|---|---|---|---|---|
| `test_lexer.py :: test_rechaza_caracteres_desconocidos()` | `"3 @ + 4"` | `ErrorDeSintaxis`, posición 2 | Inválido | Comprueba que el lexer rechace caracteres no reconocidos y reporte la posición exacta donde aparecen, en lugar de ignorarlos. |
| `test_lexer.py :: test_tokeniza_expresion_con_varios_operadores()` | `"125 + 30 * 4"` | `[Token(NUMERO, 125, 0), Token(MAS, '+', 4), Token(NUMERO, 30, 6), Token(POR, '*', 9), Token(NUMERO, 4, 11)]` | Normal | Verifica que el lexer reconozca correctamente una expresión con varios operadores y números de distintas longitudes, conservando sus valores y posiciones originales. |
| `test_lexer.py :: test_tokeniza_expresion_con_parentesis_y_operadores()` | `"(15 - 3) / 4 + 2"` | Lista de 9 tokens con sus tipos, valores y posiciones correspondientes. | Normal | Verifica que el lexer identifique correctamente números, paréntesis y diferentes operadores dentro de una misma expresión. |
| `test_lexer.py :: test_tokenizar_numeros_con_ceros_a_la_izquierda()` | `00001` | `[Token(TipoToken.NUMERO, 1, 0)]` | Normal | Verifica que los ceros adicionales a la izquierda no modifiquen el valor del número entero. |
| `test_parser.py :: test_los_negativos_unarios_son_invalidos()` | `-1` | `ErrorDeSintaxis` | Frontera | Comprueba que el parser rechace el uso del menos unario, al encontrarse fuera de las expresiones numéricas permitidas por la gramática. |
| `test_parser.py :: test_los_numeros_inician_en_cero()` | `0` | `Numero(0)` | Frontera | Comprueba que el parser acepte el cero como el menor número entero sin signo permitido por el intérprete. |
| `test_parser.py :: test_expresion_vacia()` | `""` | `ErrorDeSintaxis` | Frontera | Comprueba el comportamiento del parser para que rechace una entrada de cero caracteres, por debajo de la longitud mínima necesaria para construir una expresión válida. |
| `test_evaluator.py :: test_rechaza_numeros_sin_operador()` | `"2 3"` | `ErrorDeSintaxis, posición 2` | Inválido | Verifica que el intérprete rechace dos números consecutivos sin operador. |
| `test_evaluator.py :: test_rechaza_parentesis_sin_cerrar()` | `"(1 + 2"` | `ErrorDeSintaxis, posición 6` | Inválido | Verifica que el intérprete rechace una expresión que tenga paréntesis de apertura, pero no de cierre. |
| `test_parser.py :: test_resta_encadenada_asociativa_izquierda()` | `"10 - 3 - 2"` | `OperacionBinaria("-", OperacionBinaria("-", Numero(10), Numero(3)), Numero(2))` | Normal | Verifica que el parser construya correctamente el AST para varias restas consecutivas, respetando la asociatividad por la izquierda. |
| `test_parser.py :: test_division_encadenada_asociativa_izquierda()` | `"24 / 4 / 2"` | `OperacionBinaria("/", OperacionBinaria("/", Numero(24), Numero(4)), Numero(2))` | Normal | Verifica que el parser construya correctamente el AST para varias divisiones consecutivas, respetando la asociatividad por la izquierda. |
---

## 4. Los defectos

### 4.1 ¿Qué defecto reveló primero una prueba nueva?

La primera prueba nueva que reveló un defecto fue `test_expresion_vacia()`, que verificaba el comportamiento del parser cuando recibía una cadena vacía.
Antes de la corrección, el intérprete intentaba acceder a un token inexistente, lo que provocaba un `IndexError` de Python.
Sin embargo, de acuerdo con la semántica declarada, una entrada inválida debe rechazarse mediante `ErrorDeSintaxis`, indicando la posición del error.
La prueba permitió identificar este comportamiento incorrecto y posteriormente corregirlo en el parser.

### 4.2 ¿Por qué el comportamiento observado era incorrecto?

El comportamiento era incorrecto porque una cadena vacía no contiene ningún número ni una expresión que pueda reconocerse mediante la gramática del intérprete.

En la sección 7 del `README.md`, la semántica declarada establece que las entradas inválidas deben rechazarse utilizando `ErrorDeSintaxis`, y no mediante errores internos de Python. Además, los mensajes de error deben indicar la posición donde se detectó el problema.

Por lo tanto, al recibir `""`, el parser debía lanzar `ErrorDeSintaxis` con posición `0`, en lugar de generar un `IndexError` por intentar acceder a un token inexistente.


### 4.3 ¿Qué cambio realizaron?

| Defecto | Entrada que lo revela | Daba | Debería dar | Commit rojo | Commit verde |
|---|---|---|---|---|---|
| El parser no procesa correctamente una expresión vacía. | `""` | `IndexError` | `ErrorDeSintaxis`, posición 0 | `df9f157` | `d4483a5` |
| El intérprete acepta dos números consecutivos sin operador. | `"2 3"` | `2` | `ErrorDeSintaxis`, posición 2 | `820af45` | `0e4f7e4` |
| El parser no maneja correctamente una expresión con un paréntesis sin cerrar. | `"(1 + 2"` | `IndexError` | `ErrorDeSintaxis`, posición 6 | `064f43d` | `fee92c6` |
| El lexer ignora caracteres desconocidos en lugar de rechazarlos. | `"3 @ + 4"` | Ignoraba `@` y generaba los tokens restantes. | `ErrorDeSintaxis`, posición 2 | `ee2d4dc` | `e424e40` |
| El parser agrupa las operaciones de igual precedencia por la derecha. | `"10 - 3 - 2"` y `"24 / 4 / 2"` | `10 - (3 - 2)` y `24 / (4 / 2)` | `(10 - 3) - 2` y `(24 / 4) / 2` | `7a04549` | `abb5ae3` |

### 4.4 ¿Cómo saben que la corrección es general y no sólo hace pasar ese ejemplo?
Las correcciones realizadas no se limitaron a modificar el resultado de las expresiones utilizadas en las pruebas, sino que cambiaron el comportamiento general de los componentes responsables.

En el caso del lexer, anteriormente cualquier carácter desconocido se ignoraba mediante i += 1. Ahora se lanza ErrorDeSintaxis indicando el carácter encontrado y su posición. Esta corrección funciona para cualquier carácter que no sea un espacio, un dígito o un símbolo reconocido.

En el parser, las correcciones del manejo de entradas inválidas permiten rechazar expresiones vacías, tokens sobrantes y finales inesperados mediante ErrorDeSintaxis, evitando que se produzcan errores internos de Python en los casos corregidos.

También se corrigió la asociatividad de los operadores. Antes, _expresion() y _termino() procesaban recursivamente las operaciones por la derecha, generando árboles incorrectos cuando aparecían varios operadores del mismo nivel de precedencia.

Se sustituyó esa construcción por ciclos while que acumulan los nodos en el lado izquierdo del AST. Como el procedimiento se aplica a todos los operadores de suma/resta y multiplicación/división, la corrección no está limitada a las expresiones "10 - 3 - 2" y "24 / 4 / 2".

---

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontraron?
Identificamos las siguientes señales de problemas de mantenibilidad:

**1. Responsabilidades mezcladas en `lexer.py`.**

Originalmente, la función `tokenizar()` se encargaba tanto de recorrer la cadena de entrada como de reconocer números completos, convertirlos a enteros y crear sus tokens.

Aunque este comportamiento era correcto, concentrar ambas responsabilidades en una misma función dificultaba modificar o probar por separado el reconocimiento de números.

Este problema se relaciona con la separación de responsabilidades y se abordó mediante una extracción de método.

**2. Duplicación estructural en `parser.py`.**

Los métodos `_expresion()` y `_termino()` contienen una estructura similar para construir operaciones binarias: obtienen un operando izquierdo, comprueban el operador actual, avanzan, obtienen el operando derecho y construyen un nodo `OperacionBinaria`.

Aunque trabajan con operadores y niveles de precedencia diferentes, la lógica general está repetida. Esto puede aumentar el costo de mantenimiento, ya que ciertos cambios al procedimiento de construcción del AST podrían requerir modificaciones en ambos métodos.


### 5.2 ¿Qué refactorización realizaron, y por qué conserva el comportamiento?
Se realizó una refactorización en `lexer.py`.

Originalmente, `tokenizar()` contenía directamente la lógica encargada de reconocer números completos, recorrer sus dígitos, convertirlos a enteros y construir el token correspondiente.

Esta lógica se extrajo a una función auxiliar denominada `_leer_numero(texto, inicio)`, que recibe la cadena y la posición inicial del número, y devuelve el token generado junto con la posición desde donde debe continuar el recorrido.

De esta manera, `tokenizar()` conserva la responsabilidad de coordinar el análisis de la cadena y delega el reconocimiento completo de números a `_leer_numero()`. Y conserva el mismo comportamiento.




### 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?
En el caso de Factory Method, tenemos la posible implementación en las clases Numero y OperacionBinaria que heredan de la clase Nodo. Estas sirven para identificar que tipo de nodo se encuentra dentro de un AST. Dado que estos objetos son los únicos tipos de nodos dentro del AST con los que trabajamos durante la Tarea 1, no es necesario complicar el desarrollo metiendo clases e interfaces que extiendan el código.

En el caso de Adapter, los componentes del programa ya pueden comunicarse entre sí. El lexer genera los tokens que recibe el parser, y este construye el AST que posteriormente utiliza el evaluator. Por lo tanto, no tenemos interfaces incompatibles que necesitemos adaptar.

Sin embargo, si en el futuro el intérprete creciera y necesitáramos diferentes formas de crear objetos, podríamos considerar Factory Method. De igual manera, Adapter podría ser útil si quisiéramos integrar algún componente externo que utilizara una estructura de datos diferente.


### 5.4 ¿Qué parte del sistema sería más difícil de modificar si se agregara un operador nuevo?
Si se agregara el operador módulo `%`, sería necesario modificar al menos cuatro archivos del código fuente:

1. `tokens.py`: agregar un nuevo tipo de token para representar %.
2. `lexer.py`: agregar el símbolo % al diccionario `SIMBOLOS` para que pueda reconocerse durante la tokenización.
3. `parser.py`: incorporar el nuevo tipo de token al nivel de precedencia correspondiente, suponiendo que % tenga la misma precedencia que multiplicación y división.
4. `evaluator.py`: agregar la operación de módulo y definir su comportamiento, especialmente cuando el divisor sea cero.

También sería necesario agregar pruebas para comprobar el reconocimiento del operador, su precedencia, asociatividad, evaluación y manejo de errores.

La parte que requiere mayor cuidado es el parser, porque debe integrar el nuevo operador sin modificar la precedencia ni la asociatividad de las operaciones existentes.

En total, se modificarían al menos cuatro archivos de código fuente, además de los archivos de pruebas correspondientes.

`Alan Gael Alvarez Hernandez, Pedro Pablo Ruiz Hernández, Miranda Sanchez
