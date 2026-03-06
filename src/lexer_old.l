%option noyywrap
%option yylineno

%{

#include <stdio.h>
#include <string.h>
#include "parser.tab.h"

FILE *mlfile;
extern FILE *yyin;
%}

%%

char[ \t]+[a-zA-Z_][a-zA-Z0-9_]*\[.*\] {
    printf("Buffer declared at line %d\n", yylineno);
}

gets[ \t]*\([a-zA-Z_][a-zA-Z0-9_]*\) {
    printf("Buffer overflow risk at line %d\n", yylineno);
}

system {
    printf("System call detected at line %d\n", yylineno);
}

"int"      { return INT; }
"float"    { return FLOAT; }
"return"   { return RETURN; }

[a-zA-Z_][a-zA-Z0-9_]* { return IDENTIFIER; }
[0-9]+ { return NUMBER; }

";" { return SEMICOLON; }
"(" { return LPAREN; }
")" { return RPAREN; }
"{" { return LBRACE; }
"}" { return RBRACE; }

[ \t\r]+ ;
\n ;
. ;

%%

int main()
{
    yylex();
    return 0;
}
