# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.


## Implementation

### 1. Stack Class

I implemented the `Stack` class using a Python list. The `push()` method added items to the end of the list, while `pop()` removed and returned the last item, following LIFO behavior. The `peek()` method returned the top item without removing it, and `is_empty()` checked whether the stack contained any items. I also used `try` and `except` to handle empty-stack operations, returning `None` when no item was available.

### 2. Queue Class

I implemented the `Queue` class using `deque` from the `collections` module. The `enqueue()` method added items to the back of the queue, while `dequeue()` removed and returned the item at the front, following FIFO behavior. The `front()` method inspected the next item without removing it, and `is_empty()` checked whether the queue contained any items. As with the stack, I used exception handling to return `None` when the queue was empty.

### 3. Stack Demonstrations

I created two stack scenarios. The first added four files to a stack and processed them in reverse order, demonstrating how the most recently added file was removed first.

The second simulated a file-system search using a dictionary to represent folders and their contents. The program used a stack to implement depth-first search (DFS), adding discovered subfolders to the stack and searching them before returning to previously discovered folders. The search stopped when it found `assignment.py` or determined that the target was not present.

### 4. Queue Demonstration

I created a karaoke sign-up queue containing five singers: Dima, Paweł, Marta, Aleks, and Gabriela. The program displayed the queue, identified the next performer using `front()`, and removed singers one at a time using `dequeue()`. This demonstrated how FIFO preserved the original sign-up order as each singer finished performing.

### 5. Edge-Case Testing

I tested both classes with empty and single-item structures. For empty structures, `pop()`, `peek()`, `dequeue()`, and `front()` returned `None`, while `is_empty()` returned `True`. For single-item structures, I verified that `peek()` and `front()` could inspect the item before it was removed and that the structures became empty afterward.