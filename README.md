## Overview 

This is an example of simple arithmetic interpreter.

## Finished task: 
    - [x] handling whitespace from input
    - [x] support multidigit
    - [x] support basic operations ('+', '-', '/', '*') 
    - [x] interpret expression containing arbitrary operations and numbers (ex : 1 + 2 + 3 - 2)
    - [x] refactor lexical analyzer into Lexer and Interpreter (so it match grammars)
            expr = factor((ADD|SUBTR|MUL|DIV) factor)*
            factor = INTEGER
    - [x] handling associativity and precedence of operators ('+ and -', '* and /')
    - [x] refactor grammars so that it match these rules:
            expr = term((ADD|SUB) term)*
            term = factor((MUL|DIV) factor)*
            factor = INTEGER | L_PAREN expr R_PAREN
    - [x] handling parentheses
