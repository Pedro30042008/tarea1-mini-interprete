# Análisis — Tarea 1

**Integrantes:**
1. Alan Gael Alvarez Hernández
2. María Fernanda Miranda Sánchez
3. Pedro Pablo Ruiz Hernández

**Fork:**

https://github.com/Pedro30042008/tarea1-mini-interprete.git

**Rama:**

feature/pedro-ruiz

---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?

| Componente | Qué recibe | Qué entrega | De qué es responsable |
|---|---|---|---|
| `lexer` | | | |
| `parser` | Lista de Tokens | Nodo raíz del AST | Construir la estructura del AST a partir de la lista de Tokens recibida, respetando la precedencia de las operaciones y verificando las reglas de sintaxis planteadas. |
| `ast` | Un valor numérico o un operador definido junto con dos Nodos | Un Nodo `Numero` que contiene un valor numérico o un Nodo `OperacionBinaria` que contiene un operador, un Nodo Izquierdo y un Nodo Derecho. | Definir la estructura de los nodos `Numero` y `OperacionBinaria` que se encuentran dentro del AST. |
| `evaluator` | | | |

### 1.2 ¿Qué recorrido sigue una expresión desde que se recibe como texto hasta que produce un resultado?

> Usen `(3 + 4) * 2` como ejemplo y muestren cómo se ve entre etapa y etapa.

| Etapa | Cómo se ve `(3 + 4) * 2` aquí |
|---|---|
| texto | `"(3 + 4) * 2"` |
| tokens | |
| AST | `OperacionBinaria("*", OperacionBinaria("+", Numero(3), Numero(4)), Numero(2))` |
| resultado | |

**AST**

```text
*
├── +
│   ├── 3
│   └── 4
└── 2
```

> El dibujo del AST de la expresión `(3 + 4) * 2` hecho por el equipo coincide con el del programa.

---

## 2. Las pruebas que ya estaban

### 2.1 ¿Qué pruebas venían incluidas?

| Prueba | Componente | Comportamiento que verifica | ¿Cuántos operadores usa? | ¿Normal, frontera o inválida? |
|---|---|---|---|---|
| `test_construye_el_arbol_de_una_suma()` | parser | Verifica que parser construya el AST correcto para la suma de dos numeros `"3 + 4"` | 1 | Normal |
| `test_la_multiplicacion_se_agrupa_antes_que_la_suma()` | parser | Verifica que parser construya el AST correcto dado que la multiplicación tiene mayor prioridad en la expresión `"3 + 4 * 2"` | 2 | Normal |
| `test_los_parentesis_cambian_la_agrupacion()` | parser | Verifica que parser construya el AST correcto dado que los paréntesis tiene mayor prioridad en la expresión `"(3 + 4) * 2"` | 2 | Normal |

> Llenen la tabla **completa**, con las 13. Es tediosa a propósito: la única
> forma de saber qué no está cubierto es caracterizar sistemáticamente lo que
> sí. Cuando terminen, léanla como columna, no como renglones, y pregúntense
> qué combinación **no aparece nunca**.

### 2.2 ¿Qué comportamientos **no** estaban probados?

> Ésta es la pregunta importante de toda la tarea. Tómense su tiempo.

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
| | | | | |

---

## 4. Los defectos

### 4.1 ¿Qué defecto reveló primero una prueba nueva?

### 4.2 ¿Por qué el comportamiento observado era incorrecto?

> No basta con "daba mal". Digan contra qué lo están comparando: qué regla,
> qué línea de la semántica declarada del README.

### 4.3 ¿Qué cambio realizaron?

| Defecto | Entrada que lo revela | Daba | Debería dar | Commit rojo | Commit verde |
|---|---|---|---|---|---|
| | | | | | |

### 4.4 ¿Cómo saben que la corrección es general y no sólo hace pasar ese ejemplo?

---

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontraron?

> Al menos dos. Usen el vocabulario de clase: duplicación, rigidez,
> acoplamiento alto, condicionales repetidos, amplificación del cambio.

### 5.2 ¿Qué refactorización realizaron, y por qué conserva el comportamiento?

> "Las pruebas siguen pasando" es parte de la respuesta, pero no toda.
> ¿Por qué el cambio es equivalente?

### 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?

> Justifiquen. **"Ninguno" puede ser la respuesta correcta.** Si dicen que sí,
> digan qué problema concreto resuelve y qué costo tiene. Si dicen que no,
> digan qué tendría que cambiar en el sistema para que empezara a convenir.

### 5.4 ¿Qué parte del sistema sería más difícil de modificar si se agregara un operador nuevo?

> Por ejemplo `%`. ¿Cuántos archivos hay que tocar? ¿Por qué?

---

## Antes de la declaración: inténtenlo primero ustedes

Usar IA o no es decisión de cada quien, y el curso la permite. Pero **les
pedimos, por favor, que primero hagan el análisis por su cuenta.**

No es una prueba de honestidad. Es que el orden cambia lo que aprenden:

1. **Primero ustedes.** Lean el código, corran las pruebas, escriban sus
   respuestas. Aunque queden incompletas, aunque no encuentren todo.

2. **Después, si quieren, la IA** — pero como contraste, no como sustituto.
   Y entonces contesten dos preguntas, en `DECLARACION_IA.md`:

   - **¿Qué encontró que ustedes no habían notado?**
     Eso es aprendizaje, y se declara sin ninguna pena.

   - **¿Qué *no* encontró, que en este curso sí consideramos un problema?**
     Ésta es la interesante. Una herramienta suele decir que el código
     "funciona bien" y no señalar, por ejemplo, la **duplicación** — porque
     duplicar no rompe nada, el programa corre igual. Pero ustedes ya saben
     por qué eso sí es un mal diseño, y saben nombrarlo. La herramienta no
     tomó esa clase.

> Si invierten el orden se pierden justamente lo segundo: **no se puede notar
> lo que a una herramienta le faltó si uno nunca se formó una opinión propia
> antes de preguntarle.** Y que un programa funcione no implica que esté bien
> diseñado — eso lo dijimos en clase mucho antes de esta tarea.

---

## Declaración de uso de Inteligencia Artificial

Va en `DECLARACION_IA.md`, no aquí. Es obligatoria, pero **no da ni quita
puntos**: es un reporte adicional que se revisa aparte y se les devuelve con
comentarios.

**No se evalúa cuánta IA usaron.** Se evalúa si pueden dar cuenta de lo que
entregaron. *"No usamos"* es una declaración válida y completa; *"lo
descartamos porque..."* es de las mejores respuestas posibles.
