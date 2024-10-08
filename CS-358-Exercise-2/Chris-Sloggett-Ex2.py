# Christopher Sloggett
# CS 358 Fall 2024

from lark import Lark, v_args
from lark.visitors import Interpreter
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
    
grammar = """
    start: expr
    expr: expr "+" term -> add
        | term "-" term -> sub
        | term
    term: term "*" atom -> mul
        | term "/" atom -> div
        | atom
    atom: NUMBER -> number
        | "(" expr ")"
    %import common.NUMBER
"""  
parser = Lark(grammar , start='start')



def main(): 
    prog = "2*3-(1+4)"
    tree = parser.parse(prog)
    print(tree.pretty())
    
    prog2 = "2*3-(1+4)"
    tree2 = parser.parse(prog2)
    print(tree2.pretty())   

if __name__ == "__main__":
    main()