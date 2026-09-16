
---

# ANÃLISIS SINTÃCTICO

---
---

# PUNTO 1: IDENTIFICAR CADENAS VÃLIDAS DENTRO DE LA GRAMÃTICA

El objetivo es poder identificar / filtrar quÃ© cadenas acepta la gramÃ¡tica.

- GramÃ¡tica: 
```
expresiones_aritmeticas.g4
```
- Main:
```
main.py
```

## EjecuciÃ³n

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

2. Instalar paquete de compilaciÃ³n en el *venv*
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


# Punto 2. ComprobaciÃ³n del Parse Tree

El objetivo de este ejercicio es implementar la gramÃ¡tica de la **diapositiva 11** utilizando ANTLR4 con lenguaje objetivo Python, y comprobar la estructura del **Ãrbol de AnÃ¡lisis SintÃ¡ctico (Parse Tree)** mostrado en la **diapositiva 12** para la expresiÃ³n:

    3 + 4 * 5

---

## GramÃ¡tica utilizada

El archivo `punto_2/Expresiones.g4` contiene la gramÃ¡tica sin etiquetas ni visitor:

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

## Â¿CÃ³mo resuelve esta gramÃ¡tica la precedencia y la asociatividad?

1. **Precedencia de operadores**:
   La gramÃ¡tica estÃ¡ dividida en niveles (`expr`, `term`, `factor`). Como `term` estÃ¡ en un nivel inferior a `expr`, la multiplicaciÃ³n (`*`) se agrupa y se resuelve antes que la suma (`+`). Por esto, la multiplicaciÃ³n queda mÃ¡s abajo en el Ã¡rbol sintÃ¡ctico.

2. **Asociatividad por la izquierda**:
   Las reglas `expr : expr '+' term` y `term : term '*' factor` son recursivas por la izquierda, lo que asegura que las operaciones de igual jerarquÃ­a se resuelvan de izquierda a derecha.

---

## ComprobaciÃ³n del Parse Tree

Al ejecutar `python probar.py` con la cadena `3 + 4 * 5`, el parser genera la siguiente estructura:

### RepresentaciÃ³n textual (LISP)
```text
(expr (expr (term (factor 3))) + (term (term (factor 4)) * (factor 5)))
```

### RepresentaciÃ³n jerÃ¡rquica
```text
expr
â”œâ”€â”€ expr
â”‚   â””â”€â”€ term
â”‚       â””â”€â”€ factor
â”‚           â””â”€â”€ '3'
â”œâ”€â”€ '+'
â””â”€â”€ term
    â”œâ”€â”€ term
    â”‚   â””â”€â”€ factor
    â”‚       â””â”€â”€ '4'
    â”œâ”€â”€ '*'
    â””â”€â”€ factor
        â””â”€â”€ '5'
```

### InterpretaciÃ³n del Ã¡rbol:
- La multiplicaciÃ³n `4 * 5` se agrupa dentro del subÃ¡rbol `term`.
- La suma `+` une en la raÃ­z `expr` al nÃºmero `3` con el resultado de `4 * 5`.
- Esto comprueba formal y visualmente el Ã¡rbol de la **diapositiva 12**.

---

## Parse Tree vs. AST (Diapositivas 12, 13 y 14)

- **Parse Tree (Diapositiva 12)**: Es el Ã¡rbol sintÃ¡ctico concreto generado por el parser. Conserva todos los no terminales (`expr`, `term`, `factor`) y tokens sintÃ¡cticos para validar la gramÃ¡tica.
- **AST (Diapositiva 13)**: Es el Ã¡rbol sintÃ¡ctico abstracto. Elimina los no terminales intermedios y deja los operadores (`+`, `*`) como nodos y los nÃºmeros (`3`, `4`, `5`) como hojas. Es la estructura simplificada que se usa en etapas posteriores (evaluaciÃ³n y optimizaciÃ³n).

---

## EjecuciÃ³n del Punto 2

```bash
cd punto_2
source venv/bin/activate
ANTLR4_TOOLS_ANTLR_VERSION=4.13.2 antlr4 -Dlanguage=Python3 Expresiones.g4
python probar.py
```

---
---

# PUNTO 3: GRAMÃTICA AMBIGUA

El objetivo de este ejercicio es implementar en ANTLR4 la siguiente gramÃ¡tica:

    E â†’ E + E
    E â†’ E * E
    E â†’ num

y comprobar por quÃ© esta gramÃ¡tica es ambigua utilizando la cadena:

    2 + 3 * 4

Una gramÃ¡tica es ambigua cuando una misma cadena puede tener mÃ¡s de un Ã¡rbol de derivaciÃ³n.


## GramÃ¡tica utilizada

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

Â¿Por quÃ© la gramÃ¡tica es ambigua?

La cadena que utilizamos para probar es:

`2 + 3 * 4`

Esta cadena puede interpretarse de d


