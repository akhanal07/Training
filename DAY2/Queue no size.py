class Queue:
    def __init__(self, max_size=5):  # Set default max_size to 5
        self.items = []
        self.max_size = max_size

    def enqueue(self, item):
        if not self.is_full():
            self.items.append(item)
            print(f"Enqueued {item} into the queue.")
        else:
            print("Queue is full. Cannot enqueue.")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty. Cannot peek.")

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty. Cannot dequeue.")

    def delete(self):
        self.items = []
        print("Queue deleted.")

    def display_all(self):
        if not self.is_empty():
            print("Queue contents:")
            for item in self.items:
                print(item)
        else:
            print("Queue is empty.")

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.max_size

queue = None

while True:
    print("\nQueue Menu:")
    print("1. Create Queue")
    print("2. Enqueue")
    print("3. Peek")
    print("4. Dequeue")
    print("5. Delete")
    print("6. Display all the queue")
    print("7. Check if queue is empty")
    print("8. Check if queue is full")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        max_size = int(input("Enter the maximum size of the queue: "))
        queue = Queue(max_size=max_size)
        print(f"Created a queue with maximum size {max_size}.")
    elif choice == '2':
        if queue:
            item = input("Enter item to enqueue: ")
            queue.enqueue(item)
        else:
            print("Queue not created yet. Please create a queue first.")
    elif choice == '3':
        if queue:
            front_item = queue.peek()
            if front_item is not None:
                print("Front of the queue:", front_item)
        else:
            print("Queue not created yet. Please create a queue first.")
    elif choice == '4':
        if queue:
            dequeued_item = queue.dequeue()
            if dequeued_item is not None:
                print("Dequeued item:", dequeued_item)
        else:
            print("Queue not created yet. Please create a queue first.")
    elif choice == '5':
        if queue:
            queue.delete()
        else:
            print("Queue not created yet. Please create a queue first.")
    elif choice == '6':
        if queue:
            queue.display_all()
        else:
            print("Queue not created yet. Please create a queue first.")


    elif choice == '7':
        if queue:
            if queue.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")
        else:
            print("Queue not created yet. Please create a queue first.")
    elif choice == '8':
        if queue:
            if queue.is_full():
                print("Queue is full.")
            else:
                print("Queue is not full.")
        else:
            print("Queue not created yet. Please create a queue first.")
    elif choice == '9':
        print("Exiting...")
        break
    else:
        print("Invalid choice")

            
   
        