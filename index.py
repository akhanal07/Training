class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} onto the stack.")

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


# Example usage:
stack = Stack()

while True:
    print("\nStack Menu:")
    print("1. Push")
    print("2. Peek")
    print("3. Pop")
    print("4. Delete")
    print("5. Exit")
    print("6. Display all the stack")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter item to push: ")
        stack.push(item)
    elif choice == '2':
        print("Top of the stack:", stack.peek())
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
    else:
        print("Invalid choice")