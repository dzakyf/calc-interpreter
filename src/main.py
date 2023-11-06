# Token => object that has a type and value.
#
# EOF => token used to indicate that there is no more 
# input left for lexical analysis

INTEGER, PLUS, MINUS, MULTIPLY, DIVISION, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVISION', 'EOF'

class Token(object):
    def __init__(self, type, value):
        # INTEGER, PLUS, or EOF
        self.type = type
        # 0,1,2,3,4,...,9, '+', or None
        self.value = value 
    
    def __str__(self):
        return 'Token({type}, {value})'.format(type=self.type, value=repr(self.value))
    
    def __repr__(self):
        return self.__str__()

class Lexer(object):
    """ 
    Lexical analyzer,
    This method is responsible for breaking a sentence apart into tokens. 
    Then process one token at a time
    """
    def __init__(self, text):
        # String from input, e.g. "1+4"
        self.text = text
        # Index into self.text
        self.pos = 0
        # Current character pointed by self.pos
        self.current_char = self.text[self.pos]

    
    def error(self):
        raise Exception("Error parsing an input.")

    def move_forward(self):
        self.pos += 1

        if self.pos > len(self.text) - 1 :
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):    
        """
        advance to next character if current_char is whitespace and not None
        """
        while self.current_char is not None and self.current_char.isspace():
            self.move_forward()

    def parse_int(self):
        result = ''
        
        """
        append to result if self.current_char is numeric digit
        """
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.move_forward()

        return int(result)

    def get_next_token(self):
      
        while self.current_char is not None:
            
            # handle whitespace
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # handle integer
            if self.current_char.isdigit():
                token = Token(INTEGER, self.parse_int())
                self.move_forward()
                return token
            
            # handle basic arithmetic operations ('+' , '-' , '*', '/')
            if self.current_char == '+':
                self.move_forward()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.move_forward()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.move_forward()
                return Token(MULTIPLY, '*')
            
            if self.current_char == '/':
                self.move_forward()
                return Token(DIVISION, '/')
            
            self.error()

        return Token(EOF, None)


class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # Current token instance 
        self.current_token = None 
    
    def error(self):
        return Exception("Invalid syntax")

    def eat(self, token_type):
        """
        compare the current token with the passed token type, if they match assign next token
        to current self.current_token, otherwise raise an exception
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        """
        expected expr -> INTEGER PLUS INTEGER 
        """        

        """
        set current token to the first token taken from input
        """
        self.current_token = self.lexer.get_next_token()

        result = self.factor()

        """
        at this point INTEGER PLUS INTEGER sequence of tokens found,
        this method can just return the result of multiple operation on multiple number, 
        """
        while self.current_token.type in (PLUS, MINUS, MULTIPLY, DIVISION):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.factor()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.factor()
            elif token.type == MULTIPLY:
                self.eat(MULTIPLY)
                result = result * self.factor() 
            elif token.type == DIVISION:
                self.eat(DIVISION)
                result = result / self.factor() 
            else:
                self.error

        return result 



def main():
    while True:
        try:
            text = input("calculate> ")
        
        except EOFError:
            break

        if not text: 
            continue
        
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()