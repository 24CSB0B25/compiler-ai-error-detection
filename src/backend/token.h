#ifndef TOKEN_H
#define TOKEN_H

#include <string>

enum TokenType {
    KEYWORD,
    IDENTIFIER,
    OPERATOR,
    LITERAL,
    DELIMITER,
    MALICIOUS,
    UNKNOWN
};

struct Token {
    TokenType type;
    std::string value;
};

#endif
