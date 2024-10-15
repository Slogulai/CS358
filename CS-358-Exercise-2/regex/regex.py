# Christopher Sloggett
# CS 358 Fall 2024

from lark import Lark, v_args, Tree
from lark.visitors import Interpreter

grammar = """
    ?start: alt
    ?alt: seq ("|" seq)*
    ?seq: rep+
    ?rep: atom "*"
        | atom
    ?atom: "(" alt ")"
         | LETTER

    %import common.LETTER -> LETTER
    %import common.WS
    %ignore WS
"""

parser = Lark(grammar, start='start')

class RegexVisitor(Interpreter):
    def alt(self, tree):
        if len(tree.children) == 1:
            return self.visit(tree.children[0])
        print("alt")
        for child in tree.children:
            self.visit(child)
    
    def seq(self, tree):
        if len(tree.children) == 1:
            return self.visit(tree.children[0])
        print("seq")
        for child in tree.children:
            self.visit(child)
    
    def rep(self, tree):
        if len(tree.children) == 2:
            if isinstance(tree.children[0], Tree):
                print("rep", tree.children[0].value)
            else:
                print("rep", tree.children[0].value)
        else:
            self.visit(tree.children[0].value)
    
    def atom(self, tree):
        if len(tree.children) == 1:
            if isinstance(tree.children[0], Tree):
                self.visit(tree.children[0])
            else:
                print(tree.children[0])
        else:
            self.visit(tree.children[1])

    def LETTER(self, token):
        print(token)

def main():
    while True:
        try:
            expression = input("Enter an RE: ")
            tree = parser.parse(expression)
            visitor = RegexVisitor()
            visitor.visit(tree)
        except EOFError:
            break
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()