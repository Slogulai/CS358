# Christopher Sloggett
# CS 358 Fall 2024

from lark import Lark
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

if __name__ == "__main__":
    main()