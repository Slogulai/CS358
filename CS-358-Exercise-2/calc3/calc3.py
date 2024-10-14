# Christopher Sloggett
# CS 358 Fall 2024

from lark import Lark, v_args, Tree, Token
from lark.visitors import Interpreter

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
    
    def numNodes(self, tree):
        if isinstance(tree, Tree):
            return 1 + sum(self.numNodes(child) for child in tree.children)
        else:
            return 1

    def count1s(self, tree):
        if isinstance(tree, Tree):
            return sum(self.count1s(child) for child in tree.children)
        else:
            return 1 if tree == Token("NUM", "1") else 0
    
    def toList(self, tree):
        if isinstance(tree, Tree):
            return [tree.data] + [self.toList(child) for child in tree.children]
        else:
            return [str(tree)]
    
# Grammar for the calculator
grammar = """
    start: expr
    !?expr: (expr "+" term | expr "-" term)*
    !?term: (term "*" atom | term "/" atom)*
    !atom: "(" expr ")" | NUM
    NUM: /\d+/
    %ignore " "
"""  

# Create the parser
parser = Lark(grammar)

def main(): 
    
    while True:
        try:
            prog = input("\nEnter an expression: ")
            tree = parser.parse(prog)
            print(tree.pretty())
            print("tree.Eval() =", Eval().visit(tree))
            print("tree.numNodes() =", Eval().numNodes(tree))
            print("tree.count1s() =", Eval().count1s(tree))
            print("tree.toList() =", Eval().toList(tree))
            
        except EOFError:
            break
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
