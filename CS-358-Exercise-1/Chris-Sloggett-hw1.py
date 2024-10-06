# Christopher Sloggett
# CS 358 Fall 2024

# This program is driven by a menu for all testing functionality. You will be prompted to enter a number
# to select for which function you would like to use. You will them enter on the command line the operation 
# or word for which to type and a return value will be used to determine if the operation was successful or not.

def main():
    menu()

    
def menu():
    while True:
        print("Please select an option from the following menu:")
        print("1. Palindrome Checker With String Operations")
        print("2. Palindrome Checker With Loop Operations")
        print("3. Stacks and Queues")
        print("4. Factorial")
        print("5. Exit")

        try:
            choice = int(input("Enter a number: "))
            if 1 <= choice <= 5:

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
                    print("\nWelcome to Stacks and Queues!")

                # Choice for the factorial
                elif choice == 4:
                    print("\nFactorial functionality is not implemented yet.")

                # Choice to exit the program
                elif choice == 5:
                    print("\nGoodbye!")
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
    cleaned_string = "".join(e for e in str if e.isalnum()).lower()

    length = len(cleaned_string)
    for i in range(length//2):
        if cleaned_string[i] != cleaned_string[length - i - 1]:
            return False
    return True

# Question 2: Stacks and queues!
# Create a stack and queue and the associated functions for said data structures:
# push(s,x) — push x to stack s, return the modified stack
# pop(s) — pop an item off stack s, return the item
# enqueue(q,x) — add x to the tail of queue q, return the modified queue
# dequeue(q) — remove an item from the head of queue q, return the item

class Stack:
    def __init__(self):
        self.stack = []
    
    #Add an item to the stack
    def push(self, x):
        self.stack.append(x)
    
    #Pop from the stack and error check in case its empty
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return IndexError("Stack is empty")

class Queue:
    def __init__(self):
        self.queue = []
    
    #Add an item to the end of the queue
    def enqueue(self, x):
        self.queue.append(x)
    
    #Remove an item from the front of the queue and error check in case its empty
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return IndexError("Queue is empty")
    

# Question 3: 
# Write two versions of a factorial function: 
# fac1(n) – implement with recursion
# fac2(n) – implement with a loop

def fac1(n):
    pass
def fac2(n):
    pass



if __name__ == "__main__":
    main()
    