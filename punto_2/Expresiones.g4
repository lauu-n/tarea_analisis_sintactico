grammar Expresiones;

// Reglas sintácticas (Parser) - Diapositiva 11
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
ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

NUM
    : [0-9]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
