# Token => object that has a type and value.
#
# EOF => token used to indicate that there is no more 
# input left for lexical analysis

INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

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


class Interpreter(object):
    def __init__(self, text):
        # String from input, e.g. "1+4"
        self.text = text
        # Index into self.text
        self.pos = 0
        # Current token instance 
        self.current_token = None 
    
    def error(self):
        raise Exception("Error parsing an input.")
    
    def get_next_token(self):
        """ 
        Lexical analyzer",
        This method is responsible for breaking a sentence apart into tokens. 
        Then process one token at a time
        """
        text = self.text

        """
        return EOF if self.pos is past the end of text
        """
        if self.pos > len(text) - 1:
            return Token(EOF, None)
        
        """
        get a character at the position self.pos. Then decide what token 
        to created based on this single character.
        """
        current_char = text[self.pos]

        """
        check the character, if it is digit then create an INTEGER token, increment 
        self.pos to next character. Then return the INTEGER token 
        """
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token
        
        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        self.error()
    
    def eat(self, token_type):
        """
        compare the current token with the passed token type, if they match assign next token
        to current self.current_token, otherwise raise an exception
        """
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """
        expected expr -> INTEGER PLUS INTEGER 
        """        

        """
        set current token to the first token taken from input
        """
        self.current_token = self.get_next_token()

        """
        expected single digit integer 
        """
        left = self.current_token
        self.eat(INTEGER)


        """
        expected '+' token
        """
        opr = self.current_token
        self.eat(PLUS)

        """
        expected single digit integer 
        """
        right = self.current_token
        self.eat(INTEGER)


        """
        at this point INTEGER PLUS INTEGER sequence of tokens found,
        this method can just return the result of adding two integers, 
        """
        result = left.value + right.value 
        return result 



def main():
    while True:
        try:
            text = input("calculate> ")
        
        except EOFError:
            break

        if not text: 
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()