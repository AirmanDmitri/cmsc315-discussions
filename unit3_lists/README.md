# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?


## Implementation

### 1. Insertion Function

I implemented the `insert_at()` function using Python's built-in `insert()` method. The function accepts a list, an index, and a value, then inserts the value at the specified position without replacing existing elements. When an item is inserted, the elements at and after that position shift one place to the right. I included comments explaining how insertion performance varies depending on the position. Inserting at the beginning requires shifting all existing elements, while inserting in the middle only shifts the elements after the insertion point. Inserting at the end does not require shifting existing elements.

### 2. Deletion Function

I implemented the `delete_at()` function using Python's `pop()` method. The function removes and returns the item at the specified index. I used `try` and `except` to handle invalid indices, returning `None` when the requested index does not exist. This is important because attempting to remove an item from an invalid position would otherwise raise an `IndexError` and interrupt the program. The function allows the program to handle unsuccessful deletion attempts safely while preserving the original list.

### 3. Search Function

I implemented the `search_value()` function using a linear search with Python's `enumerate()`. This allows the function to access both the current element and its index while checking the list sequentially. The search starts at the first element and continues until it finds a match or reaches the end of the list. For example, searching for `CFTR` in a list containing five genes returns index `2`, since Python uses zero-based indexing. Searching for a gene that does not exist returns `-1`. This approach is useful when searching through an unsorted list because it does not require the elements to be arranged in any particular order.

### 4. Insertion Demonstrations

I created an insertion scenario using a list of five example genetic findings: `BRCA1`, `CFTR`, `HBB`, `APOE`, and `TP53`. I first displayed the original list, then inserted three additional findings at different positions. The first finding, associated with `HBB`, was inserted at index `0`, moving all existing findings one position to the right. I then inserted an `APOE` finding at index `1`, demonstrating how an insertion in the middle affects only the elements following that position. Finally, I added a `TP53` finding using the list's length as the insertion index, placing it at the end. These examples demonstrate how the same operation can be used to add findings while preserving the existing entries and how the insertion position affects the amount of shifting required.

### 5. Deletion Demonstrations

I created a separate list containing five example genetic findings and tested deletion at three different positions. First, I removed the finding at index `0`, demonstrating how the remaining elements shift left to fill the empty position. Next, I removed the element at index `1`, which demonstrated deletion from the middle of the list. Finally, I removed the last element using `len(flagged_findings) - 1` as the index. After each operation, the program displayed both the removed finding and the updated list. Using a separate list for these tests made it possible to demonstrate each deletion without relying on the changes made during the insertion tests.

### 6. Search Demonstrations

I created a list containing five genes identified in parsed genetic data: `BRCA1`, `BRCA2`, `CFTR`, `HBB`, and `APOE`. I tested the search function with two different values. First, I searched for `CFTR`, which returned index `2`, confirming that the function could locate an existing gene and identify its position. I then searched for `EGFR`, which was not included in the list. In this case, the function returned `-1`, allowing the program to display a message indicating that the gene was not found. Together, these examples demonstrate both possible search outcomes and how the returned index can be used by the rest of the program.

### 7. Edge-Case Testing

I tested three edge cases to examine how the functions behave when the list or requested index presents an unusual situation. First, I attempted to delete an item at index `10` from a list containing only two findings. Since that index did not exist, the function returned `None` and left the original list unchanged. Second, I attempted to delete an item from an empty list. This also returned `None`, demonstrating that the exception handling works even when no elements are available. Finally, I inserted a `MYH7` finding into an empty list at index `0`. The operation completed successfully, demonstrating that insertion can initialize an empty list with its first element.

### 8. Real-World Scenario

I created a scenario simulating a user searching through parsed genetic data and flagging a specific finding for later reference. The program starts with a list of five parsed gene names and an initially empty list of flagged findings. It searches for `CFTR` using the `search_value()` function. If the gene is found, the program uses `insert_at()` to add its associated finding, `CFTR: Example variant B`, to the separate flagged-findings list. It then displays the resulting list. This demonstrates how searching and insertion can work together to locate specific information in a larger dataset and copy a selected finding into another list without modifying the original parsed gene data.