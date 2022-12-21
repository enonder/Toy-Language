class Parser1:
    def __init__(self, tokens):
        self.tokens = tokens
        self.program = []
        self.index = 0
        self.input_token = {}

    def next_token(self):
        if self.index >= len(self.tokens):
            self.input_token = '$'
        else:
            self.input_token = self.tokens[self.index]
            self.index += 1
            
    def match(self,expected_token):
        if self.input_token.value != expected_token:
            raise Exception('match error')
        self.next_token()

    def readPrgram(self):
        return self.program

    def run(self):
        self.next_token()
        if self.input_token != '$':
            self.parse()
        else:
            return self.program

    def parse(self):
        body = self.assignment()
        self.program.append(body)
        self.run()


    def assignment(self):
        identifier = self.identifier()
        operator = self.operator()
        exp = self.exp()

        body = {}
        body["left"] = identifier.value
        body["operator"] = operator.value
        body["right"]=exp
        body["type"]="assign"

        return body
    
    def exp(self):
        term = self.term()
        exp_prime = self.exp_prime()

        if term and exp_prime == None:
            return term
        
        body = {}
        if term != None:
            body["left"] = term

        if exp_prime != None:
            body["right"] = exp_prime[0]
            body["value"] = exp_prime[2].value
            body["type"] = exp_prime[2].type

        return body
    
    def exp_prime(self):
        current_token = self.input_token
        if self.input_token.value == '-' or self.input_token.value == '+':
            self.next_token()
            exp = self.exp()
            exp_prime = self.exp_prime()
            return [exp, exp_prime, current_token]
        else:
            return

    def term(self):
        factor = self.factor()
        term_prime = self.term_prime()

        if factor and term_prime == None:
            return factor
        
        body = {}
        if factor != None:
            body["left"] = factor

        if term_prime != None:
            body["right"] = term_prime[0]
            body["value"] = term_prime[2].value
            body["type"] = term_prime[2].type

        return body

    def term_prime(self):
        current_token = self.input_token
        if self.input_token.value == '*':
            self.next_token()
            term = self.term()
            term_prime = self.term_prime()
            return [term, term_prime, current_token]
        else:
            return
        
    def factor(self):
        current_token = self.input_token
        if self.input_token.type == 'Number':
            self.next_token()
            return current_token

        if self.input_token.type == 'Identifier':
            self.next_token()
            return current_token
        
        if self.input_token.type == 'Left Paranthesis':
            self.next_token()
            exp = self.exp()
            self.match(')')
            return exp

        if self.input_token.value == ';':
            return
 
    def identifier(self):
        if self.input_token.type == "Identifier":
            current_token = self.input_token
            self.next_token()
            return current_token

    def operator(self):
        if self.input_token.type == "Equal" and self.input_token.value == "=":
            current_token = self.input_token
            self.next_token()
            return current_token