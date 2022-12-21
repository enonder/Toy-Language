import Lexer
from Parser import Parser
from Interpreter import Interpreter


def runLexer():
    while True:
        text = input('Input: ')
        result, error = Lexer.run(text)

        if error: print(error.as_string())
        else: return result

tokens = runLexer()

obj = Parser(tokens)
obj.run()
program = obj.readPrgram()

inter = Interpreter(program)
inter.run()
test = inter.read_values()
print(test)

