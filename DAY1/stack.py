#STACK UNCOUNTABLE
# # class Stack:
#     def __init__(self, max_size=10):
#         self.items = []
#         self.max_size = max_size

#     def push(self, item):
#         if not self.is_full():
#             self.items.append(item)
#             print(f"Pushed {item} onto the stack.")
#         else:
#             print("Stack is full. Cannot push.")

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             print("Stack is empty. Cannot peek.")

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             print("Stack is empty. Cannot pop.")

#     def delete(self):
#         self.items = []
#         print("Stack deleted.")

#     def display_all(self):
#         if not self.is_empty():
#             print("Stack contents:")
#             for item in reversed(self.items):
#                 print(item)
#         else:
#             print("Stack is empty.")

#     def is_empty(self):
#         return len(self.items) == 0

#     def is_full(self):
#         return len(self.items) >= self.max_size

# # Example usage:
# stack = Stack()

# while True:
#     print("\nStack Menu:")
#     print("1. Push")
#     print("2. Peek")
#     print("3. Pop")
#     print("4. Delete")
#     print("5. Exit")
#     print("6. Display all the stack")
#     print("7. Check if stack is empty")
#     print("8. Check if stack is full")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         item = input("Enter item to push: ")
#         stack.push(item)
#     elif choice == '2':
#         top_item = stack.peek()
#         if top_item is not None:
#             print("Top of the stack:", top_item)
#     elif choice == '3':
#         popped_item = stack.pop()
#         if popped_item is not None:
#             print("Popped item:", popped_item)
#     elif choice == '4':
#         stack.delete()
#     elif choice == '5':
#         print("Exiting...")
#         break
#     elif choice == '6':
#         stack.display_all()
#     elif choice == '7':
#         if stack.is_empty():
#             print("Stack is empty.")
#         else:
#             print("Stack is not empty.")
#     elif choice == '8':
#         if stack.is_full():
#             print("Stack is full.")
#         else:
#             print("Stack is not full.")
#     else:
#         print("Invalid choice")



#STACK SIZE = 5
class Stack:
    def __init__(self, max_size=5):  # Set default max_size to 5
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
            print(f"Pushed {item} onto the stack.")
        else:
            print("Stack is full. Cannot push.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek.")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")

    def delete(self):
        self.items = []
        print("Stack deleted.")

    def display_all(self):
        if not self.is_empty():
            print("Stack contents:")
            for item in reversed(self.items):
                print(item)
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.max_size

# Example usage:
stack = Stack(max_size=5)  # Create a stack with a maximum size of 5

while True:
    print("\nStack Menu:")
    print("1. Push")
    print("2. Peek")
    print("3. Pop")
    print("4. Delete")
    print("5. Exit")
    print("6. Display all the stack")
    print("7. Check if stack is empty")
    print("8. Check if stack is full")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter item to push: ")
        stack.push(item)
    elif choice == '2':
        top_item = stack.peek()
        if top_item is not None:
            print("Top of the stack:", top_item)
    elif choice == '3':
        popped_item = stack.pop()
        if popped_item is not None:
            print("Popped item:", popped_item)
    elif choice == '4':
        stack.delete()
    elif choice == '5':
        print("Exiting...")
        break
    elif choice == '6':
        stack.display_all()
    elif choice == '7':
        if stack.is_empty():
            print("Stack is empty.")
        else:
            print("Stack is not empty.")
    elif choice == '8':
        if stack.is_full():
            print("Stack is full.")
        else:
            print("Stack is not full.")
    else:
        print("Invalid choice")
        
        
        


