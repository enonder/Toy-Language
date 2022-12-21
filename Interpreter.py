class Interpreter:
    def __init__(self, program):
        self.program = program
        self.input_line = {}
        self.values = []
        self.values_obj = {}
        self.notEnd = True
        self.index = 0

    def read_values(self):
        return self.values_obj

    def next_line(self):
        if self.index >= len(self.program):
            self.notEnd = False
        else:
            self.input_line = self.program[self.index]
            self.index += 1

    def run(self):
        self.next_line()
        if self.notEnd:
            self.interpret()

    def interpret(self):
        if self.input_line["type"] == "assign":
            return self.assign()
    
    def assign(self):
        identifier = self.input_line["left"]
        value = self.operator(self.input_line["right"])
        operator = self.input_line["operator"]

        self.values.append([identifier,operator,value])
        self.values_obj[identifier] = value
        self.run()

    def operator(self,calc):
        if type(calc) is dict:  
            if calc == {}: return None; 
            print(calc, calc["left"], calc["right"])     
            l = self.calculate(calc["left"])
            r = self.calculate(calc["right"])

            print(calc["value"],l,r)
            value = self.selectOperator(calc["value"],l,r)
            return value
        else:
            return self.calculate(calc)

    def calculate(self,slt):
        if type(slt) is not dict: 
            if slt.type == "Number":
                return slt.value
            elif slt.type == "Identifier":
                if(self.values_obj[slt.value]):
                    return self.values_obj[slt.value]
                else:
                    raise Exception('Identifier is not found')
        else:
            return self.operator(slt)

    def selectOperator(self,operator,l,r):
        if l == None: l = 0
        if r == None: r = 0

        if operator == '+':
            return int(l) + int(r)
        if operator == '-':
            return int(l) - int(r)
        if operator == '*':
            return int(l) * int(r)
        else:
            return

