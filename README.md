---

# ANÁLISIS SINTÁCTICO

---
---

# PUNTO 1: IDENTIFICAR CADENAS VÁLIDAS DENTRO DE LA GRAMÁTICA

El objetivo es poder identificar / filtrar qué cadenas acepta la gramática.

- Gramática: 
```
expresiones_aritmeticas.g4
```
- Main:
```
main.py
```

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

3.  Generar los archivos de Python desde el archivo *expresiones_aritmeticas.g4*
  ```
  ANTLR4_TOOLS_ANTLR_VERSION=4.13.2 antlr4 -Dlanguage=Python3 expresiones_aritmeticas.g4
  ```

<img width="677" height="545" alt="image" src="https://github.com/user-attachments/assets/9af7a079-6e61-4c22-ada1-2dc3b61250bc" />

4. Ejecutar *main.py*, junto con el archivo *ejemplos.txt* como argumento
 ```
  python main.py ejemplos.txt
  ```
<img width="673" height="525" alt="image" src="https://github.com/user-attachments/assets/4370f7da-78c8-4320-a221-c073607a5ae2" />


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

3. **Uso de paréntesis**:
   La regla `factor : '(' expr ')'` permite reiniciar el ciclo de expresiones dentro de paréntesis, alterando el orden de evaluación natural cuando es necesario.

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

| Característica | Parse Tree / CST (Diapositiva 12) | AST / Árbol Sintáctico Abstracto (Diapositiva 13) |
| :--- | :--- | :--- |
| **Definición** | Árbol sintáctico concreto que representa cada producción gramatical aplicada. | Árbol simplificado que representa únicamente la semántica de la expresión. |
| **Nodos presentes** | Conserva todos los símbolos no terminales (`expr`, `term`, `factor`) y los símbolos de puntuación. | Elimina los no terminales intermedios; los operadores (`+`, `*`) se convierten en los nodos internos y los valores en hojas. |
| **Rol en el compilador** | Generado directamente por el **Parser** para validar la gramática de la entrada. | Generado en fases posteriores (por ejemplo, mediante Visitor o Listener) para evaluación, optimización y generación de código. |
| **Complejidad para `3 + 4 * 5`** | Estructura completa de 14 nodos entre reglas y hojas terminales. | Estructura compacta de solo 5 nodos: raíz `+`, hijo izquierdo `3`, hijo derecho `*` con hijos `4` y `5`. |

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

# PUNTO 3: GRAMÁTICA AMBIGUA

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

Esta cadena puede interpretarse de d
