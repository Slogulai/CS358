# Christopher Sloggett
# CS 358 Fall 2024

# This program is driven by a menu for all testing functionality. You will be prompted to enter a number
# to select for which function you would like to use. You will them enter on the command line the operation 
# or word for which to type and a return value will be used to determine if the operation was successful or not.

# All questions for assignment 1 are answered in this file. For questions that are just plain text, comment
# blocks are used

# I chose to go with a menu for simplicity and ease of running since there is one central file, rather than using Pytest


# Main function, which calls menu. Could have relly just put everything within menu within main.
def main():
    menu()
 
# This is where the meat of the running program happens. 
def menu():
    while True:
        print("Please select an option from the following menu:")
        print("1. Palindrome Checker With String Operations")
        print("2. Palindrome Checker With Loop Operations")
        print("3. Stacks and Queues")
        print("4. Factorial")
        print("5. AST and Reverse Operator Precedence Tree")
        print("6. Exit")

        try:
            choice = int(input("Enter a number: "))
            if 1 <= choice <= 6:

                # Choice for the string operation palindrom checker
                if choice == 1:
                    print("\n\nYou have selected the string operation Palindrome Checker")
                    to_check = input("Enter a string to check if it is a palindrome: ")
                    is_true = palindrome1(to_check)
                    if is_true:
                        print("\nThe string is a palindrome\n\n")
                    else:
                        print("\nThe string is not a palindrome\n\n")

                # Choice for the loop operation palindrome checker
                elif choice == 2:
                    print("\nYou have selected the loop Palindrome Checker")
                    to_check = input("Enter a string to check if it is a palindrome: ")
                    is_true = palindrome2(to_check)
                    if is_true:
                        print("\nThe string is a palindrome\n\n")
                    else:
                        print("\nThe string is not a palindrome\n\n")
                
                # Choice for the stacks and queues
                elif choice == 3:
                    print("\n\nWelcome to Stacks and Queues!")
                    print("1. Press 1 for stacks")
                    print("2. Press 2 for queues")

                    try: 
                        stack_queue_choice = int(input("Enter a number: "))
                        if stack_queue_choice == 1:
                            print("\n\nYou have selected stacks")
                            stack = newstack()
                            print("\n1. Press 1 to push an item onto the stack")
                            print("2. Press 2 to pop an item off the stack")
                            print("3. Press 3 to exit the stack")

                            while True:
                                stack_choice = int(input("\nEnter a number (1 - 3): "))
                                if stack_choice == 1:
                                    item = input("\nEnter an item to push onto the stack: ")
                                    stack = push(stack, item)
                                    print(f"\n{item} has been pushed onto the stack")
                                    print(f"\nCurrent stack: {stack}")
                                elif stack_choice == 2:
                                    item = pop(stack)
                                    print(f"\n{item} has been popped off the stack")
                                    print(f"\nCurrent stack: {stack}")
                                elif stack_choice == 3:
                                    print("\nExiting the stack")
                                    break
                                else:
                                    print("Invalid choice. Please enter a number between 1 and 3")

                        elif stack_queue_choice == 2:
                            print("\nYou have selected queues")
                            queue = newqueue()
                            print("\n1. Press 1 to enqueue an item onto the queue")
                            print("2. Press 2 to dequeue an item off the queue")
                            print("3. Press 3 to exit the queue")

                            while True:
                                queue_choice = int(input("\nEnter a number (1 - 3): "))
                                if queue_choice == 1:
                                    item = input("\nEnter an item to enqueue onto the queue: ")
                                    queue = enqueue(queue, item)
                                    print(f"\n{item} has been enqueued onto the queue")
                                    print(f"\nCurrent queue: {queue}")
                                elif queue_choice == 2:
                                    item = dequeue(queue)
                                    print(f"\n{item} has been dequeued off the queue")
                                    print(f"\nCurrent queue: {queue}")
                                elif queue_choice == 3:
                                    print("\nExiting the queue")
                                    break
                                else:
                                    print("Invalid choice. Please enter a number between 1 and 3")
                        else:
                            print("Invalid choice. Please enter a number between 1 and 2")
                    except ValueError:
                        print("Invalid choice. Please enter a number between 1 and 2")

                # Choice for the factorial
                elif choice == 4:
                    print("\nWelcome to the Factorial tester!")
                    print("1. Press 1 for recursive factorial")
                    print("2. Press 2 for loop factorial")

                    try:
                        factorial_choice = int(input("Enter a number: "))
                        if factorial_choice == 1:
                            n = int(input("Enter a number to find the factorial of: "))
                            result = fac1(n)
                            print(f"\nThe factorial of {n} is {result}\n")
                        elif factorial_choice == 2:
                            n = int(input("Enter a number to find the factorial of: "))
                            result = fac2(n)
                            print(f"\nThe factorial of {n} is {result}\n")
                        else:
                            print("Invalid choice. Please enter a number between 1 and 2")
                    except ValueError:
                        print("Invalid choice. Please enter a number between 1 and 2")


                # Choice for the AST and Reverse Operator Precedence Tree
                elif choice == 5:
                    print("\nWelcome to the AST and Reverse Operator Precedence Tree tester!")
                    print("Given the expression 1 + 2 * 3^4 - 5, we can represent this as an AST")
                    print("The AST would look like: ")

                    root = Node("-")
                    root.left = Node("+")
                    root.right = Node("5")
                    root.left.left = Node("1")
                    root.left.right = Node("*")
                    root.left.right.left = Node("2")
                    root.left.right.right = Node("^")
                    root.left.right.right.left = Node("3")
                    root.left.right.right.right = Node("4")

                    print("\n\nThe AST would look like: ")
                    print_tree(root)
                    print(root)

                    print("\n\nThe reversed operator precedence tree would look like: ")
                    reversed_root = Node("^")
                    reversed_root.left = Node("3")
                    reversed_root.right = Node("4")
                    reversed_root.left = Node("*")
                    reversed_root.left.left = Node("2")
                    reversed_root.left.right = Node("+")
                    reversed_root.left.right.left = Node("1")
                    reversed_root.left.right.right = Node("-")
                    reversed_root.left.right.right.right = Node("5")

                    print_tree(reversed_root)
                    print(reversed_root)

                    print("\nEnd of AST and Reverse Operator Precedence Tree tester\n\n")

                # Choice to exit the program
                elif choice == 6:
                    print("\nGoodbye!\n")
                    break

            # Else block checking for invalid choices
            else:
                print("Invalid choice. Please enter a number between 1 and 5")
        # Except block for invalid input
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5")


# Question 1: palindrome1 is a string operation function that checks if a string is a palindrome.
#            palindrome2 is a loop operation function that checks if a string is a palindome.

#This function checks for palindrome by returning whether or not the reverse of the 
#is equal to the original. All alphanumeric characters are removed and the original
#string is converted to lowercase. Since addition is associative, the reversed string
#will be equal to the original if it is a palindrome.
def palindrome1(str):
    #Creating a cleaned string for later reversal
    clean_string = "".join(e for e in str if e.isalnum()).lower()
    #Returning whether or not the cleaned string is equal to its reverse
    return clean_string == clean_string[::-1]


def palindrome2(str):
    #Creating a cleaned string for later reversal
    cleaned_string = "".join(e for e in str if e.isalnum()).lower()

    #Getting the length of the cleaned string for my loop
    length = len(cleaned_string)
    #Looping through the string to check if its a palindrome
    for i in range(length//2):
        if cleaned_string[i] != cleaned_string[length - i - 1]:
            return False #Return false if a character doenst match
    return True

# Question 2: Stacks and queues!
# Create a stack and queue and the associated functions for said data structures:
# push(s,x) — push x to stack s, return the modified stack
# pop(s) — pop an item off stack s, return the item
# enqueue(q,x) — add x to the tail of queue q, return the modified queue
# dequeue(q) — remove an item from the head of queue q, return the item

#Using a function and list for the stack, per the assignment
def newstack():
    return []

def push(stack, x):
    stack.append(x) #appending to the end with the stack
    return stack

def pop(stack):
    if stack:
        return stack.pop() #removing from the end of the stack
    else:
        raise IndexError("Stack is already empty")

#Using a function and list for the queue, per the assignment
def newqueue():
    return []

def enqueue(queue, x):
    queue.append(x) #Appending to the end of the queue
    return queue

def dequeue(queue):
    if queue:
        return queue.pop(0) #removing from the front of the queue given its structure
    else:
        raise IndexError("Queue is already empty")
    

# Question 3: 
# Write two versions of a factorial function: 
# fac1(n) – implement with recursion
# fac2(n) – implement with a loop

def fac1(n):
    if n == 0:
        return 1
    else:
        return n * fac1(n-1)

def fac2(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Question 4:
# Part a:
# Given the expression: 
# 1 + 2 * 3^4 - 5
# An AST for said expression would look like: 
#           -
#          /  \
#         +    5
#       /   \
#      1     *
#           /  \
#          2    ^
#              /  \
#             3    4
# Expressed in linear form : [ - [ +1 [ *2 [ ^3 4 ] 5 ]]

# Part b:
# The reversed operator precendence tree would look like: 
#         ^
#        / \
#       3   4
#       *
#      / \ 
#     2   +
#        / \
#       1   -
#            \ 
#             5
# Where the lowest precedence operator is at the top of the tree
# In Linear form: [ ^3 4 [ *2 [ +1 [-5] ]]]
# This expression would evaluate to 104,976. while the original expression evaluates to 158

# Question 5: 
# Define Python classes for the AST nodes (which should correspond to the operators in the above expression).
# Construct a tree object for each of the two ASTs

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"    

def print_tree(node, prefix="", is_left=True):
    if node is not None:
        print(prefix, "`- " if is_left else "+- ", node.value, sep="")
        new_prefix = prefix + ("|  " if is_left else "   ")
        print_tree(node.left, new_prefix, True)
        print_tree(node.right, new_prefix, False)

# Defining Main for running the program 
if __name__ == "__main__":
    main()
    