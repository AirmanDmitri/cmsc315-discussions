"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, item):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        # Adding items to the end of items ensures that the most recently added item is removed first
        self.items.append(item)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # If the stack is empty, the method catches the IndexError and returns None 
        # instead of allowing the exception to interrupt the program
        try:
            return self.items.pop()
        except IndexError:
            return None 
        
    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        # Returns the top item without removing it from the stack
        # Also returns None if stack is empty
        try:
            return self.items[-1]
        except IndexError:
            return None

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, item):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        
        # Adding items to the back ensures that the first item added is the first item removed
        self.items.append(item)


    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        
        # If the queue is empty, the method catches the IndexError and returns None
        # instead of allowing the exception to interrupt the program.
        try:
            return self.items.popleft()
        except IndexError:
            return None

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        
        # Returns the first item without removing it from the queue.
        # Also returns None if the queue is empty.
        try:
            return self.items[0]
        except IndexError:
            return None

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")

    # Demonstrate LIFO with four files waiting to be processed.
    print("\n=== FILE PROCESSING STACK ===")
    file_stack = Stack()

    file_stack.push("essay.docx")
    file_stack.push("budget.xlsx")
    file_stack.push("assignment.py")
    file_stack.push("README.md")

    print("Four files added to the stack.")
    print("Current stack:", file_stack.items)
    print("Next file to process:", file_stack.peek())

    print("\nProcessing files in LIFO order:")
    while not file_stack.is_empty():
        print("Processing:", file_stack.pop())

    print("Is the file stack empty?", file_stack.is_empty())

    # Demonstrate a stack-based depth-first file-system search.
    print("\n=== FILE SYSTEM SEARCH ===")
    file_system = {
        "Documents": ["essay.docx", "University", "budget.xlsx"],
        "University": ["CMSC315", "GERM314"],
        "CMSC315": ["assignment.py", "README.md"],
        "GERM314": ["discussion.docx"]
    }

    folder_stack = Stack()
    folder_stack.push("Documents")

    target_file = "assignment.py"
    found = False

    print(f"Searching for '{target_file}'...\n")

    while not folder_stack.is_empty():
        current_folder = folder_stack.pop()
        print(f"Searching folder: {current_folder}")

        for item in file_system[current_folder]:
            if item == target_file:
                print(f"Found '{target_file}' inside {current_folder}!")
                found = True
                break

            if item in file_system:
                folder_stack.push(item)
                print(f"Discovered subfolder: {item}")
                print("Search stack:", folder_stack.items)

        if found:
            break

    if not found:
        print(f"'{target_file}' was not found.")

    print("Search complete.")
    print("Is the search stack empty?", folder_stack.is_empty())

    # Test pop() and peek() on an empty stack.
    print("\n=== EMPTY-STACK TEST ===")
    empty_stack = Stack()
    print("Trying to remove an item:", empty_stack.pop())
    print("Trying to inspect the top item:", empty_stack.peek())
    print("Is the stack empty?", empty_stack.is_empty())

    # Test removing the only item from a stack.
    print("\n=== SINGLE-ITEM TEST ===")
    single_item_stack = Stack()
    single_item_stack.push("Downloads")
    print("Item at the top:", single_item_stack.peek())
    print("Removing the item:", single_item_stack.pop())
    print("Is the stack empty now?", single_item_stack.is_empty())


# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    print("\n=== KARAOKE SIGN-UP QUEUE ===")

    # Create a queue of people waiting to sing.
    karaoke_queue = Queue()

    # Add five singers to the back of the queue.
    karaoke_queue.enqueue("Dima")
    karaoke_queue.enqueue("Paweł")
    karaoke_queue.enqueue("Marta")
    karaoke_queue.enqueue("Aleks")
    karaoke_queue.enqueue("Gabriela")

    print(f"{len(karaoke_queue.items)} singers have signed up for karaoke.")
    print("The next performer is:", karaoke_queue.front())
    print("Current queue:", karaoke_queue.items)

    # Singers perform in the order they signed up (FIFO).
    while not karaoke_queue.is_empty():
        singer = karaoke_queue.dequeue()
        print(f"\n{singer} has finished singing.")
        print("Singers left in the queue:", len(karaoke_queue.items))
        print("Current queue:", karaoke_queue.items)

        if not karaoke_queue.is_empty():
            print("The next performer is:", karaoke_queue.front())
        else:
            print("There are no singers left in the queue.")

    # Test dequeue() and front() on an empty queue.
    print("\n=== EMPTY-QUEUE TEST ===")
    print("Trying to remove the next singer:", karaoke_queue.dequeue())
    print("Checking the next singer:", karaoke_queue.front())
    print("Is the karaoke queue empty?", karaoke_queue.is_empty())

    # Test a queue containing only one singer.
    print("\n=== SINGLE-SINGER TEST ===")
    solo_queue = Queue()
    solo_queue.enqueue("Dima")

    print("The only performer is:", solo_queue.front())
    print("After singing, the performer leaves:", solo_queue.dequeue())
    print("Is the queue empty now?", solo_queue.is_empty())


if __name__ == "__main__":
    main()
