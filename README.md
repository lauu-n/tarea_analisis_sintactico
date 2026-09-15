# ANÁLISIS SINTÁCTICO

---

## Ejecución

0. Requisitos
- Java
  ```
  sudo apt install default-jdk
  ```
- Instalar runtime de ANTLR para Python
  ```
   pip install antlr4-tools antlr4-python3-runtime
  ```
  
1. Crear venv
```
python -m venv venv
```
```
source .venv/bin/activate
```

2. Instalar paquete de compilación en el *venv*
 ```
   pip install antlr4-tools
  ```

3.  Generar los archivos de Python desde el archivo .g4
  ```
  ANTLR4_TOOLS_ANTLR_VERSION=4.13.2 antlr4 -Dlanguage=Python3 expresiones_aritmeticas.g4
  ```

---
---

Punto 3. Gramatica Ambigua
El objetivo de este ejercicio es implementar en ANTLR4 la siguiente gramática:

    E → E + E
    E → E * E
    E → num

y comprobar por qué esta gramática es ambigua utilizando la cadena:

    2 + 3 * 4

Una gramática es ambigua cuando una misma cadena puede tener más de un árbol de derivación.


# Gramática utilizada

El archivo `Ambigua.g4` contiene:

# antlr
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

# ¿Dónde está la ambigüedad?

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

# Archivos del proyecto

El proyecto contiene:

- Ambigua.g4
- probar.py

Después de generar el parser aparecen archivos adicionales:

- AmbiguaLexer.py
- AmbiguaParser.py
- AmbiguaListener.py
- AmbiguaVisitor.py

Estos archivos son generados automáticamente por ANTLR.

# ¿Por qué ANTLR no muestra los dos árboles?

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

# Diferencia entre la gramática y el parser generado

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
