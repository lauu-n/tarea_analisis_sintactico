# ANÁLISIS SINTÁCTICO

---

## Ejecución General

0. Requisitos
- Java
  ```bash
  sudo apt install default-jdk
  ```
- Instalar runtime de ANTLR para Python
  ```bash
  pip install antlr4-tools antlr4-python3-runtime
  ```
  
1. Crear venv
```bash
python -m venv venv
```
```bash
source venv/bin/activate
```

2. Instalar paquete de compilación en el *venv*
```bash
pip install antlr4-tools antlr4-python3-runtime
```

---
---

# Punto 2. Comprobación del Parse Tree

El objetivo de este ejercicio es implementar la gramática de la **diapositiva 11** utilizando ANTLR4 con lenguaje objetivo Python, y comprobar la estructura del **Árbol de Análisis Sintáctico (Parse Tree)** mostrado en la **diapositiva 12** para la expresión:

    3 + 4 * 5

---

## Gramática utilizada

El archivo `punto_2/Expresiones.g4` contiene la gramática sin etiquetas ni visitor:

```antlr
grammar Expresiones;

expr
    : expr '+' term
    | term
    ;

term
    : term '*' factor
    | factor
    ;

factor
    : ID
    | NUM
    | '(' expr ')'
    ;

ID  : [a-zA-Z_][a-zA-Z0-9_]* ;
NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
```

## ¿Cómo resuelve esta gramática la precedencia y la asociatividad?

1. **Precedencia de operadores**:
   La gramática está dividida en niveles (`expr`, `term`, `factor`). Como `term` está en un nivel inferior a `expr`, la multiplicación (`*`) se agrupa y se resuelve antes que la suma (`+`). Por esto, la multiplicación queda más abajo en el árbol sintáctico.

2. **Asociatividad por la izquierda**:
   Las reglas `expr : expr '+' term` y `term : term '*' factor` son recursivas por la izquierda, lo que asegura que las operaciones de igual jerarquía se resuelvan de izquierda a derecha.

---

## Comprobación del Parse Tree

Al ejecutar `python probar.py` con la cadena `3 + 4 * 5`, el parser genera la siguiente estructura:

### Representación textual (LISP)
```text
(expr (expr (term (factor 3))) + (term (term (factor 4)) * (factor 5)))
```

### Representación jerárquica
```text
expr
├── expr
│   └── term
│       └── factor
│           └── '3'
├── '+'
└── term
    ├── term
    │   └── factor
    │       └── '4'
    ├── '*'
    └── factor
        └── '5'
```

### Interpretación del árbol:
- La multiplicación `4 * 5` se agrupa dentro del subárbol `term`.
- La suma `+` une en la raíz `expr` al número `3` con el resultado de `4 * 5`.
- Esto comprueba formal y visualmente el árbol de la **diapositiva 12**.

---

## Parse Tree vs. AST (Diapositivas 12, 13 y 14)

- **Parse Tree (Diapositiva 12)**: Es el árbol sintáctico concreto generado por el parser. Conserva todos los no terminales (`expr`, `term`, `factor`) y tokens sintácticos para validar la gramática.
- **AST (Diapositiva 13)**: Es el árbol sintáctico abstracto. Elimina los no terminales intermedios y deja los operadores (`+`, `*`) como nodos y los números (`3`, `4`, `5`) como hojas. Es la estructura simplificada que se usa en etapas posteriores (evaluación y optimización).

---

## Ejecución del Punto 2

```bash
cd punto_2
source venv/bin/activate
ANTLR4_TOOLS_ANTLR_VERSION=4.13.2 antlr4 -Dlanguage=Python3 Expresiones.g4
python probar.py
```

---
---

# Punto 3. Gramatica Ambigua
El objetivo de este ejercicio es implementar en ANTLR4 la siguiente gramática:

    E → E + E
    E → E * E
    E → num

y comprobar por qué esta gramática es ambigua utilizando la cadena:

    2 + 3 * 4

Una gramática es ambigua cuando una misma cadena puede tener más de un árbol de derivación.


## Gramática utilizada

El archivo `Ambigua.g4` contiene:

## antlr
```
grammar Ambigua;

expr
    : expr '+' expr
    | expr '*' expr
    | NUM
    ;

NUM
    : [0-9]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
```

¿Por qué la gramática es ambigua?

La cadena que utilizamos para probar es:

`2 + 3 * 4`

Esta cadena puede interpretarse de dos formas diferentes.

Primera interpretación

Primero se realiza la suma:

(2 + 3) * 4

El árbol sería:

        *
       / \
      +   4
     / \
    2   3

La raíz es *.

Esto significa que primero se construye:

2 + 3

y posteriormente se multiplica por 4.

Segunda interpretación

Primero se realiza la multiplicación:

2 + (3 * 4)

El árbol sería:

        +
       / \
      2   *
         / \
        3   4

La raíz es +.

Esto significa que primero se construye:

3 * 4

y posteriormente se suma 2.

## ¿Dónde está la ambigüedad?

La gramática no establece ninguna regla que diga que * debe tener mayor prioridad que +.

Tenemos:

`E → E + E`
`E → E * E`

pero no tenemos ninguna regla que indique:

* tiene mayor precedencia que +

Por lo tanto, la cadena:

`2 + 3 * 4`

puede generar dos árboles diferentes:

`(2 + 3) * 4`

y:

`2 + (3 * 4)`

Por definición, esto hace que la gramática sea ambigua.

## Archivos del proyecto

El proyecto contiene:

- Ambigua.g4
- probar.py

Después de generar el parser aparecen archivos adicionales:

- AmbiguaLexer.py
- AmbiguaParser.py
- AmbiguaListener.py
- AmbiguaVisitor.py

Estos archivos son generados automáticamente por ANTLR.

## ¿Por qué ANTLR no muestra los dos árboles?

Aunque la gramática original es ambigua, ANTLR4 tiene un tratamiento especial para reglas recursivas por la izquierda.

La regla:

```
expr
    : expr '+' expr
    | expr '*' expr
    | NUM
    ;
```
es una regla recursiva por la izquierda porque `expr` aparece al principio de sus propias alternativas:

```
expr → expr + expr
expr → expr * expr
```

ANTLR4 transforma internamente este tipo de reglas para poder construir el parser.

Por este motivo, al ejecutar el programa ANTLR puede terminar seleccionando una interpretación concreta y producir solamente un árbol.

Esto no significa que la gramática original deje de ser ambigua.

## Diferencia entre la gramática y el parser generado

Es importante diferenciar:

```
Gramática original
E → E + E
E → E * E
E → num
```

Esta gramática es ambigua.

La cadena:

`2 + 3 * 4`

tiene dos árboles posibles.

Parser generado por ANTLR

En cambio ANTLR4 procesa la recursión izquierda y utiliza su mecanismo interno de análisis para poder reconocer las expresiones.

Por eso al ejecutar:

`python3 probar.py`

se obtiene una sola estructura:

`(expr (expr (expr 2) + (expr 3)) * (expr 4))`
