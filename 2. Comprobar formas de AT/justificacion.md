# Justificación y Comprobación del Punto 2

## 1. Objetivo del Ejercicio
El objetivo de este punto es implementar la gramática clásica para expresiones aritméticas presentada en la **diapositiva 11** utilizando ANTLR4 con lenguaje objetivo Python, y comprobar la estructura del **Árbol de Análisis Sintáctico (Parse Tree)** mostrado en la **diapositiva 12** para la expresión:

$$3 + 4 * 5$$

---

## 2. Gramática Utilizada (`Expresiones.g4`)
La gramática formal de la diapositiva 11 se define como:

$$E \to E + T \mid T$$
$$T \to T * F \mid F$$
$$F \to \text{id} \mid \text{num} \mid (E)$$

En ANTLR4, esta gramática se implementa directamente sin etiquetas y sin visitor:

```antlr
grammar Expresiones;

// Reglas sintácticas (Parser)
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

// Reglas léxicas (Lexer)
ID  : [a-zA-Z_][a-zA-Z0-9_]* ;
NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
```

### ¿Cómo garantiza esta gramática la precedencia y la asociatividad?
1. **Precedencia de Operadores**:
   - La gramática está construida en niveles jerárquicos.
   - Las reglas que se encuentran en niveles inferiores (`term` y `factor`) se derivan y agrupan más profundamente en el árbol.
   - Por esta razón, el operador de multiplicación (`*`), definido dentro de la regla `term`, se evalúa y agrupa con mayor prioridad que el operador de suma (`+`), el cual reside en el nivel superior `expr`.
2. **Asociatividad por la Izquierda**:
   - Las reglas `expr : expr '+' term` y `term : term '*' factor` utilizan recursividad por la izquierda directa. Esto asegura que operaciones con la misma precedencia se agrupen de izquierda a derecha.
3. **Uso de Paréntesis**:
   - La regla `factor : '(' expr ')'` permite reiniciar el ciclo de expresiones dentro de paréntesis, permitiendo alterar el orden de evaluación natural.

---

## 3. Comprobación del Parse Tree (Diapositiva 12)
Al ejecutar el análisis sintáctico sobre la cadena `3 + 4 * 5`, se obtienen las siguientes comprobaciones:

### Comprobación 1: Formato Textual (LISP)
```text
(expr (expr (term (factor 3))) + (term (term (factor 4)) * (factor 5)))
```

### Comprobación 2: Estructura Jerárquica del Parse Tree
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

### Análisis del Resultado:
- El subárbol derecho es `term`, compuesto por `term '*' factor`, el cual agrupa a los operandos `'4'` y `'5'`.
- El término izquierdo es `expr`, que se reduce a `'3'`.
- La raíz `expr` une mediante el operador `'+'` al `3` con el producto resultante de `4 * 5`.
- Esta estructura reproduce con exactitud el árbol de derivación de la **diapositiva 12**.

---

## 4. Comparación: Parse Tree vs. AST (Diapositivas 12, 13 y 14)

| Característica | Parse Tree / CST (Diapositiva 12) | AST / Árbol Sintáctico Abstracto (Diapositiva 13) |
| :--- | :--- | :--- |
| **Definición** | Árbol sintáctico concreto que representa cada producción gramatical aplicada. | Árbol simplificado que representa únicamente la semántica de la expresión. |
| **Nodos presentes** | Conserva todos los símbolos no terminales (`expr`, `term`, `factor`) y los símbolos de puntuación. | Elimina los no terminales intermedios; los operadores (`+`, `*`) se convierten en los nodos internos y los valores en hojas. |
| **Rol en el Compilador** | Generado directamente por el **Parser** para validar la gramática de la entrada. | Generado en fases posteriores (por ejemplo, mediante Visitor o Listener) para evaluación, optimización y generación de código. |
| **Complejidad para `3 + 4 * 5`** | Estructura completa de 14 nodos entre reglas y hojas terminales. | Estructura compacta de solo 5 nodos: raíz `+`, hijo izquierdo `3`, hijo derecho `*` con hijos `4` y `5`. |

---

## 5. Instrucciones de Ejecución en el Entorno Virtual

1. Activar el entorno virtual de Python:
   ```bash
   source venv/bin/activate
   ```
2. Compilar la gramática con ANTLR4:
   ```bash
   ANTLR4_TOOLS_ANTLR_VERSION=4.13.2 antlr4 -Dlanguage=Python3 Expresiones.g4
   ```
3. Ejecutar las pruebas:
   ```bash
   python probar.py
   ```
