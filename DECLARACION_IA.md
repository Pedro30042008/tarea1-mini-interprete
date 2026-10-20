# Declaración de uso de Inteligencia Artificial

**Actividad:** Tarea 1 — Mini intérprete de expresiones  
**Fecha:** 19 de octubre de 2026

**Integrantes:**
- Maria Fernanda Miranda Sánchez - 420102320
- Pedro Pablo Ruiz Hernández - 323198507
- Alan Gael Alvarez Hernandez - 323113340



> Esta declaración es obligatoria en toda tarea, práctica y en el proyecto final.
> **No da ni quita puntos**: es un reporte adicional que se revisa aparte y se
> devuelve con comentarios. **No se evalúa cuánta IA usaron**, sino si pueden
> dar cuenta de lo que entregaron.

---

## 0. ¿Se usó IA en esta actividad?

- [ ] **No.** Firmen la última sección y terminen. Con eso queda completa.
- [x] **Sí.** Contesten los cinco puntos.

---

## 1. Herramienta(s) utilizada(s)

| Herramienta | Versión o modelo, si lo saben |
|---|---|
| ChatGPT (OpenAI) | GPT-6 |

---

## 2. Objetivo del uso

| Para qué la usamos | En qué parte del entregable |
|---|---|
| Proponer una distribución del trabajo entre los tres integrantes. | Organización de pruebas, revisión de componentes y correcciones del mini intérprete. |
| Consultar dudas de sintaxis de Python y pytest, y cómo expresar pruebas de entradas inválidas. | `tests/test_evaluator.py` |
| Analizar comportamientos en los que el intérprete debía rechazar la entrada y revisar posibles correcciones. | `src/mini_interprete/parser.py` y documentación de defectos en `ANALISIS.md`. |
| Resolver dudas sobre el uso de Git y GitHub para registrar cambios y colaborar. | Commits de pruebas y correcciones, rama de trabajo y Pull Request. |
|

---

## 3. Prompts principales

Textuales, tal como los escribieron. No los limpien ni los reescriban.

**Prompt 1:**

```text
Esta es nuestra tarea 1. Por favor leela. [https://github.com/karlycaramelo/tarea1-mini-interprete](https://github.com/karlycaramelo/tarea1-mini-interprete)

y estos son los archivos en general por si te sirven. 

Como podemos repartir las pruebas, la revisión del codigo y la correccion de errores entre tres integrantes?
```

**Prompt 2:**

```text
Me gustaria enfocarme en estos errores (ve el doc). Que casos de prueba puedo agregar para comprobar que mi codigo maneja correctamente los errores?
 
 La persona del equipo B ya me dio permiso de modifcar el parse y todo, puedo modificar en general todo el programa. Ademas, creo que es buena idea que haga las pruebas y que salga el error y de eso haga el commit ya que los commits a git Commits pequeños y descriptivos. `git log --oneline` debe contar el proceso. Un solo commit llamado `tarea` vale cero en ese rubro.
```

**Prompt 3:**

```text
Como creo un Pull Request sin modificar directamente main?
```

**Prompt 4:**

```text
okok, antes de empezar me puedes explicar como funciona el interprete? por que q vrga hace parser
```

**Prompt 5:**

```text
oye w, para la refactorizacion estaba pensando cambiar los if con un switch de java xd, pero no se si se si funcione xd
```

---

## 4. Cómo se incorporó o se descartó lo obtenido

| Qué produjo la herramienta                                                                                         | ¿Aceptado, modificado o descartado? | Por qué                                                                                                               | Dónde quedó (archivo / commit)                                  |
|--------------------------------------------------------------------------------------------------------------------|---|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| Sugerencia de dividir la revisión en pruebas normales, frontera e inválidas, con responsabilidades por componente. | Aceptado como apoyo para organizar el trabajo. | Permitió repartir responsabilidades y coordinar la revisión.                                                          | Organización del equipo; no corresponde a un commit específico. |
| Propuesta de prueba para rechazar `"2 3"` con `ErrorDeSintaxis`.                                                   | Incorporado. | La entrada carece de operador entre números y el código original ignoraba el segundo token.                           | `tests/test_evaluator.py`; `820af45`.                           |
| Comprobación de tokens restantes al terminar `parsear()`.                                                          | Incorporado. | Evita aceptar una expresión de la que sólo se procesó una parte.                                       | `src/mini_interprete/parser.py`; `0e4f7e4`.                     |
| Comprobación del fin de tokens antes de consumirlos en `_avanzar()`.                                               | Incorporado. | Sustituye un error de índice de Python por una excepción de sintaxis del intérprete.                                  | `src/mini_interprete/parser.py`; `fee92c6`.                     |
| Orientación sobre Git, commits pequeños y Pull Requests.                                                           | Utilizado como guía. | Se buscó que el historial distinguiera las pruebas de las correcciones.                                               | En general en el proyecto de Github.                            |
| Explicó el funcionamiento del parser, la construcción del AST y las responsabilidades de `_expresion()`, `_termino()` y `_factor()`. | Aceptado como apoyo para la comprensión. | La explicación permitió comprender cómo se construye el AST a partir de los tokens y cómo se respeta la precedencia de los operadores. No se incorporó código directamente. | Consulta de apoyo para comprender `parser.py`. |



### 4.1 Si la usaron para el análisis: el contraste

| | |
|---|---|
| ¿Qué encontró la herramienta que ustedes **no** habían notado? | En la revisión de entradas inválidas señaló que `parsear()` podía devolver un AST aunque quedaran tokens sin consumir, y que `_avanzar()` podía lanzar `IndexError` si la lista terminaba antes de lo esperado. |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? | No basta con que las pruebas nuevas pasen: también debe revisarse la duplicación de lógica entre `_expresion()` y `_termino()`, la capacidad de mantener el código y la diferencia entre corregir un defecto y refactorizar sin alterar el comportamiento.  |

### 4.2 ¿Cómo verificaron que lo que incorporaron era correcto?

Las pruebas de `"2 3"` y `"(1 + 2"` se añadieron en commits separados antes de corregir el parser. Se identificaron los comportamientos originales (devolver `2` e informar `IndexError`, respectivamente) y posteriormente se registraron dos correcciones independientes. Las pruebas verifican tanto el tipo de excepción esperado (`ErrorDeSintaxis`) como su posición (2 y 6).

Al ejecutar las pruebas con `python3 -m pytest -v` sobre la versión integrada, las pruebas originales y nuevas pasaron.

---

## 5. Reflexión

### 5.1 ¿Qué limitación concreta observaron **en esta actividad**?

Una sugerencia inicial fue comprobar los errores con sólo dos expresiones concretas. Esas pruebas sirven para demostrar los defectos detectados, pero no bastan para garantizar que todas las entradas incompletas o con tokens sobrantes estén cubiertas. Además, la corrección propuesta para calcular la posición al final de los tokens utiliza la representación del último token y puede no coincidir con la longitud real de la entrada cuando hay espacios finales. Por eso es importante contrastar cada propuesta con las reglas del README y probar otros casos, no copiarla sin verificar sus límites.

### 5.2 ¿Qué harían distinto la próxima vez?

Primero definimos por nuestra cuenta los casos de prueba y sus resultados esperados, basándonos en los requisitos del README y en nuestro análisis del código. Posteriormente, utilizamos IA para resolver dudas específicas de sintaxis, explorar alternativas de solución y considerar posibles casos adicionales. Para futuras actividades, procuraríamos conservar desde el inicio los prompts y las decisiones tomadas, con el fin de documentar mejor qué sugerencias se aceptaron, modificaron o descartaron, además de verificar todas las pruebas antes de integrar los cambios.

---

## Firma

> Declaramos que entendemos y podemos explicar todo lo que entregamos,
> independientemente de las herramientas que hayamos utilizado.

| Nombre | Número de cuenta |
|---|---|
| Maria Fernanda Miranda Sánchez  | 420102320|
| Pedro Pablo Ruiz Hernández  | 323198507 |
| Alan Gael Alvarez Hernandez | 323113340 |

