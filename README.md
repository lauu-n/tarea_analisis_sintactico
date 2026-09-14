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

