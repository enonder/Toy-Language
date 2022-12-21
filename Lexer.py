# Errors

class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}'
        return result 

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)


# # Tokens
Identifier = 'Identifier'
Number = 'Number'
Plus = 'Plus'
Minus = 'Minus'
Mul = 'Multiplacation'
Equal = 'Equal'
RightPar = 'Right Paranthesis'
LeftPar = 'Left Paranthesis'
Semicolon = 'Semicolon'

class Token:
    def __init__(self, type_, value=None):
     
        self.type = type_
        self.value = value
    
    def __repr__(self):
        return f'{self.type}:{self.value}'
  
#Lexer

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char.isalpha() or self.current_char == "_":
                tokens.append(self.make_identifier())
            elif self.current_char.isdigit():
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(Plus, self.current_char))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(Minus, self.current_char))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(Mul, self.current_char))
                self.advance()
            elif self.current_char == '=':
                tokens.append(Token(Equal, self.current_char))
                self.advance()           
            elif self.current_char == '(':
                tokens.append(Token(LeftPar, self.current_char))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(RightPar, self.current_char))
                self.advance()
            elif self.current_char == ';':
                tokens.append(Token(Semicolon, self.current_char))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char + "'")

        return tokens, None

    def make_identifier(self):
        id_str = ''
        while self.current_char != None and (self.current_char.isalpha() or self.current_char == "_"):
            id_str += self.current_char
            self.advance()
        while self.current_char != None and (self.current_char.isalnum() or self.current_char == "_") and len(id_str) >1 :
            id_str += self.current_char
            self.advance()
        return Token(Identifier, id_str)

    def make_number(self):
        num_str = ''
        while self.current_char != None and self.current_char.isdigit():
            num_str += self.current_char
            self.advance()

            if num_str == '0' and self.current_char.isdigit():
                raise Exception('Invalid Character')

            if self.current_char.isalpha():
                raise Exception('Invalid Character: ', num_str + self.current_char)

        return Token(Number, num_str)


def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error