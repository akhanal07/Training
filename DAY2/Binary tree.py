class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node is not None
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def delete(self, value):
        self.root, deleted = self._delete_recursive(self.root, value)
        return deleted

    def _delete_recursive(self, node, value):
        if node is None:
            return node, False

        if value < node.value:
            node.left, deleted = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right, deleted = self._delete_recursive(node.right, value)
        else:
            deleted = True
            if node.left is None:
                return node.right, deleted
            elif node.right is None:
                return node.left, deleted

            min_larger_node = self._get_min(node.right)
            node.value = min_larger_node.value
            node.right, _ = self._delete_recursive(node.right, min_larger_node.value)

        return node, deleted

    def _get_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node is not None:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

def menu():
    tree = BinaryTree()
    while True:
        print("\nMenu:")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. In-order Traversal")
        print("5. Pre-order Traversal")
        print("6. Post-order Traversal")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                value = int(input("Enter value to insert: "))
                tree.insert(value)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        elif choice == '2':
            try:
                value = int(input("Enter value to search: "))
                found = tree.search(value)
                if found:
                    print(f"{value} is in the tree.")
                else:
                    print(f"{value} is not in the tree.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        elif choice == '3':
            try:
                value = int(input("Enter value to delete: "))
                deleted = tree.delete(value)
                if deleted:
                    print(f"{value} was deleted from the tree.")
                else:
                    print(f"{value} was not found in the tree.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        elif choice == '4':
            print("In-order Traversal:", tree.inorder_traversal())
        
        elif choice == '5':
            print("Pre-order Traversal:", tree.preorder_traversal())
        
        elif choice == '6':
            print("Post-order Traversal:", tree.postorder_traversal())
        
        elif choice == '7':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
