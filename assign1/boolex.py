# Christopher Sloggett
#

# CS358 Fall'24 Assignment 1 (Part A)
#
# BoolEx - a Boolean expression language

from lark import Lark, v_args
from lark.visitors import Interpreter

# 1. Grammar
#
grammar = """
    ?orex: orex "or" andex -> orop
        | andex
    ?andex: andex "and" atom -> andop
        | atom
    ?atom: "not" atom -> notop
        | "(" orex ")" 
        | "True" -> truev
        | "False" -> falsev
    %import common.WS -> WS
    %import common.CNAME -> NAME
    %ignore WS
"""
# Parser
#
# E.g. (True or not False) and True
#      => andop  
#           orop
#             truev
#             notop
#               falsev
#           truev
#
parser = Lark(grammar, start='orex', parser='lalr')

# 2. Interpreter
#
# E.g. (for the above example)
#      => True
#
@v_args(inline=True)
class Eval(Interpreter):
    def andop(self, left, right):
        return self.visit(left) and self.visit(right)
    def orop(self, left, right):
        return self.visit(left) or self.visit(right)
    def notop(self, value):
        return not self.visit(value)
    def truev(self):
        return True
    def falsev(self):
        return False

# 3. Convert the AST to a list form
#
# E.g. (for the above example)
#      => ['and', ['or', 'True', ['not', 'False']], 'True']
#
@v_args(inline=True)
class toList(Interpreter):
    def orop(self, left, right):
        return ['or', self.visit(left), self.visit(right)]
    def andop(self, left, right):
        return ['and', self.visit(left), self.visit(right)]
    def notop(self, value):
        return ['not', self.visit(value)]
    def truev(self):
        return 'True'
    def falsev(self):
        return 'False'

# 4. Convert a nested list to a string form
#
# E.g. (for the above example)
#      => (and (or True (not False)) True)
#
def strForm(lst):
    if isinstance(lst, list):
        return f"({lst[0]} {' '.join(strForm(x) for x in lst[1:])})"
    else:
        return lst

def main():
    while True:
        try:
            expr = input("Enter a bool expr: ")
            tree = parser.parse(expr)
            lst = toList().visit(tree)
            print(expr)
            print(tree.pretty(), end="")
            print("tree.Eval() =", Eval().visit(tree))
            print("tree.toList() =", lst)
            print("strForm() =", strForm(lst))
            print()
        except EOFError:
            break
        except Exception as e:
            print("***", e)

if __name__ == '__main__':
    main()
