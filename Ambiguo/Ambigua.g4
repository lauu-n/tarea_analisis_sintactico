grammar Ambigua;

// REGLA DEL PARSER

expr
    : expr '+' expr
    | expr '*' expr
    | NUM
    ;


// REGLAS DEL LEXER

NUM
    : [0-9]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
