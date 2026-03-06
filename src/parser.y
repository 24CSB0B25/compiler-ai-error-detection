%{
#include <stdio.h>
#include <stdlib.h>
int yylex(void);
void yyerror(const char *s);
%}

%token INT FLOAT CHAR DOUBLE
%token IF ELSE WHILE FOR RETURN
%token NUMBER IDENTIFIER
%token EQ NEQ LE GE LT GT
%token ASSIGN PLUS MINUS MUL DIV
%token SEMICOLON LPAREN RPAREN LBRACE RBRACE

%start program

%%

program:
    statements
;

statements:
    statements statement
  | statement
;

statement:
    declaration SEMICOLON
  | assignment SEMICOLON
;

declaration:
    type IDENTIFIER
;

assignment:
    IDENTIFIER ASSIGN expression
;

expression:
    expression PLUS term
  | expression MINUS term
  | term
;

term:
    term MUL factor
  | term DIV factor
  | factor
;

factor:
    NUMBER
  | IDENTIFIER
  | LPAREN expression RPAREN
;

type:
    INT
  | FLOAT
  | CHAR
  | DOUBLE
;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Syntax Error: %s\n", s);
}
