#include <iostream>
#include <cstdio>

extern int yylex();
extern FILE* yyin;

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cout << "Usage: ./lexer <source_file>" << std::endl;
        return 1;
    }

    yyin = fopen(argv[1], "r");
    if (!yyin) {
        std::cerr << "Error opening file" << std::endl;
        return 1;
    }

    yylex();

    fclose(yyin);
    return 0;
}
