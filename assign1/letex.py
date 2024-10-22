# <your name>
#

# CS358 Fall'24 Assignment 1 (Part B)
#
# LetEx - an expression language with let binding

from lark import Lark, v_args
from lark.visitors import Interpreter

# 1. Grammar
#
grammar = """
    ?expr0: "let" ID "=" expr0 "in" expr0 -> let
        | expr
    ?expr: expr "+" term -> add
        | expr "-" term -> sub
        | term
    ?term: term "*" atom -> mul
        | term "/" atom -> div
        | atom
    ?atom: "(" expr0 ")"
        | ID -> var
        | NUM -> num
    %import common.CNAME -> ID
    %import common.NUMBER -> NUM
    %import common.WS
    %ignore WS 
"""

# Parser
#
# E.g. let x=1 in x+1
#      => let
#           x
#           num   1
#           add
#             var x
#             num 1
#
parser = Lark(grammar, start='expr0', parser='lalr')

# 2. Variable environment
#
class Env(dict):
    def extend(self,x,v):
        if x in self:
            self[x].insert(0,v)
        else:
            self[x] = [v]
    def lookup(self,x): 
        vals = super().get(x)
        if not vals:
            raise Exception("Endefined variable: " + x)
        return vals[0]
    def retract(self,x):
        assert x in self, "Undefined variable: " + x
        self[x].pop(0)

env = Env()

# 3. Interpreter
#
# E.g. (for the above example)
#      => 2
#
@v_args(inline=True)
class Eval(Interpreter):
    def let(self, name, value_expr, body_expr):
        value = self.visit(value_expr)
        env.extend(name, value)
        result = self.visit(body_expr)
        env.retract(name)
        return result
    def add(self, left, right):
        return self.visit(left) + self.visit(right)
    def sub(self, left, right):
        return self.visit(left) - self.visit(right)
    def mul(self, left, right):
        return self.visit(left) * self.visit(right)
    def div(self, left, right):
        return self.visit(left) / self.visit(right)
    def group(self, expr):
        return self.visit(expr)
    def var(self, name):
        return env.lookup(name)
    def num(self, value):
        return int(value)

def main():
    while True:
        try:
            expr = input("Enter a let expr: ")
            tree = parser.parse(expr)
            print(expr)
            print(tree.pretty(), end="")
            print("tree.Eval() =", Eval().visit(tree))
            print()
        except EOFError:
            break
        except Exception as e:
            print("***", e)

if __name__ == '__main__':
    main()
