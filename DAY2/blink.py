class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def delete(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:  # If the list becomes empty
                self.tail = None
            self.length -= 1
            return

        prev_node = self.head
        current_node = self.head.next
        while current_node is not None:
            if current_node.value == value:
                prev_node.next = current_node.next
                if current_node.next is None:  # If the deleted node was the tail
                    self.tail = prev_node
                self.length -= 1
                return
            prev_node = current_node
            current_node = current_node.next

    def search(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

def menu():
    linked_list = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Append")
        print("2. Prepend")
        print("3. Delete")
        print("4. Search")
        print("5. Display List")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                value = int(input("Enter value to append: "))
                linked_list.append(value)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        elif choice == '2':
            try:
                value = int(input("Enter value to prepend: "))
                linked_list.prepend(value)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        elif choice == '3':
            try:
                value = int(input("Enter value to delete: "))
                linked_list.delete(value)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        elif choice == '4':
            try:
                value = int(input("Enter value to search: "))
                found = linked_list.search(value)
                if found:
                    print(f"{value} is in the list.")
                else:
                    print(f"{value} is not in the list.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        elif choice == '5':
            print("Linked List:", linked_list)
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
