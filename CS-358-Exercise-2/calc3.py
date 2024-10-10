# Christopher Sloggett
# CS 358 Fall 2024

from lark import Lark, v_args
from lark.visitors import Interpreter
@v_args(inline=True)

# Eval class that inherits from Interpreter
@v_args(inline=True)
class Eval(Interpreter):
    def num(self, val):
        return int(val)
    def add(self, left, right):
        return Eval().visit(left) + Eval().visit(right)
    def sub(self, left, right):
        return Eval().visit(left) - Eval().visit(right)
    def mul(self, left, right):
        return Eval().visit(left) * Eval().visit(right)
    def div(self, left, right):
        return Eval().visit(left) / Eval().visit(right)
    
# Grammar for the calculator
grammar = """
    start: expr
    expr: expr "+" term -> add
         | expr "-" term -> sub
         | term
    term: term "*" atom -> mul
         | term "/" atom -> div
         | atom
    atom: NUM -> num
         | "(" expr ")"
    %import common.NUM
    %import common.WS
    %ignore WS
"""  

# Create the parser
parser = Lark(grammar , start='start')



def main(): 

    while True:
        try:
            prog = input("Enter an expression: ")
            tree = parser.parse(prog)
            print(tree.pretty())
            print("tree.Eval() =", Eval().visit(tree))
        except EOFError:
            break
        except Exception as e:
            print(e)
            
    
#    prog = "2*3-(1+4)"
#    tree = parser.parse(prog)
#    print(tree.pretty())
#    
#    prog2 = "2*3-(1+4)"
#    tree2 = parser.parse(prog2)
#    print(tree2.pretty())   

if __name__ == "__main__":
    main()
