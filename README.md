## Overview 

This is an example of simple arithmetic interpreter.

## Currently supports: 
    - [x] handling whitespace from input
    - [x] support multidigit
    - [x] support basic operations ('+', '-', '/', '*') 
    - [x] interpret expression containing arbitrary operations and numbers (ex : 1 + 2 + 3 - 2)
    - [x] refactor lexical analyzer into Lexer and Interpreter (so it match grammars)
            expr = factor((ADD|SUBTR|MUL|DIV) factor)*
            factor = INTEGER
    - [x] handling associativity and precedence of operators ('+ and -', '* and /')
    - [x] handling parentheses
