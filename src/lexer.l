%option noyywrap
%option yylineno

%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE *mlfile;

/* function to send token to ML detector */
void run_ml_detector(const char *token)
{
    char cmd[256];

    /* skip symbols that break shell */
    if(strcmp(token,"(")==0 || strcmp(token,")")==0 ||
       strcmp(token,"{")==0 || strcmp(token,"}")==0 ||
       strcmp(token,";")==0)
        return;

    sprintf(cmd,"../venv/bin/python ../phase9/ml_token_detector.py \"%s\"",token);
    system(cmd);
}

void log_token(const char *token,
               const char *type,
               int label,
               int line)
{
    if (mlfile) {
        fprintf(mlfile,"%s,%s,%d,%d\n",
                token,type,label,line);
    }

    /* Week-9 ML detection (does NOT affect dataset) */
    run_ml_detector(token);
}
%}

DIGIT      [0-9]
ID         [a-zA-Z_][a-zA-Z0-9_]*
NUMBER     {DIGIT}+

%%

^[ \t]*#.* ;

(gets|system) {
    printf("Unsafe function '%s' at line %d\n", yytext, yylineno);
    log_token(yytext,"unsafe_function",1,yylineno);
}

char[ \t]+{ID}[ \t]*\[[ \t]*{NUMBER}[ \t]*\] {
    printf("Buffer declaration at line %d\n", yylineno);
    log_token("buffer_decl","buffer",1,yylineno);
}

(int|float|char|return) {
    log_token(yytext,"keyword",0,yylineno);
}

{ID} {
    log_token(yytext,"identifier",0,yylineno);
}

{NUMBER} {
    log_token(yytext,"number",0,yylineno);
}

";" { log_token(";","symbol",0,yylineno); }
"(" { log_token("(","symbol",0,yylineno); }
")" { log_token(")","symbol",0,yylineno); }
"{" { log_token("{","symbol",0,yylineno); }
"}" { log_token("}","symbol",0,yylineno); }

[ \t\r]+ ;
\n ;
. ;

%%

int main(int argc, char **argv)
{
    if (argc < 2) {
        printf("Usage: ./compiler <file.c>\n");
        return 1;
    }

    yyin = fopen(argv[1], "r");
    if (!yyin) {
        printf("Cannot open input file\n");
        return 1;
    }

    mlfile = fopen("datasets/lexical/tokens.csv","a");
    if (!mlfile) {
        mlfile = fopen("../datasets/lexical/tokens.csv","a");
    }
    if (!mlfile) {
        printf("Cannot open tokens.csv\n");
        return 1;
    }

    yylex();

    fclose(mlfile);
    fclose(yyin);
    return 0;
}
