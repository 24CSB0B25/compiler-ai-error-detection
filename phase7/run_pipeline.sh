#!/bin/bash

echo "=============================="
echo "Week 7 Secure Lexer Pipeline"
echo "=============================="

echo "🔧 Building lexer..."
cd src
rm -f lex.yy.c compiler
flex lexer.l
g++ lex.yy.c -o compiler -lfl
cd ..

echo "🧹 Preparing dataset..."
mkdir -p datasets/lexical
> datasets/lexical/tokens.csv

echo "📊 Processing SAFE samples..."
for f in datasets/safe/*.c; do
    [ -f "$f" ] && src/compiler "$f"
done

echo "🚨 Processing UNSAFE samples..."
for f in datasets/unsafe/*.c; do
    [ -f "$f" ] && src/compiler "$f"
done

echo "✅ Week-7 token dataset ready"
