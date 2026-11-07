# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## Implementation

### 1. Node Class

I implemented the `Node` class to represent individual elements in the Binary Search Tree. Each node stored a value and references to its left and right child nodes. Both child references were initially set to `None`, indicating that the node did not have any children when it was first created. This structure allowed each node to connect to other nodes and form the hierarchical organization of the tree.

### 2. Insertion Function

I implemented the `insert()` function using recursion to add values to the Binary Search Tree. The function first checked whether the current node was `None`. If it was, a new `Node` object was created and returned. Otherwise, the function compared the value being inserted with the current node's value. Smaller values were passed to the left subtree, while greater or equal values were passed to the right subtree. This allowed the tree to organize values according to the BST property without requiring them to be inserted in sorted order. Each comparison determined which subtree needed to be examined, reducing the search space for subsequent operations.

### 3. Search Function

I implemented the `search()` function using recursion to locate a specific value in the tree. The function compared the target value with the current node's value. If the values matched, it returned `True`. If the target was smaller, the search continued through the left subtree; otherwise, it continued through the right subtree. If the search reached a `None` node without finding a match, it returned `False`. This approach allowed the function to avoid examining nodes in the opposite subtree at each comparison.

### 4. In-Order Traversal

I implemented the `inorder()` function to display the values stored in the tree in ascending order. The recursive traversal visited the left subtree first, followed by the current node, and then the right subtree. Since smaller values were stored to the left and greater or equal values to the right, this sequence produced sorted output. The function collected the visited values in a list and returned the resulting sequence.

### 5. Tree Construction Demonstration

I created a Binary Search Tree using a dictionary containing nine historical records associated with different years. Each year served as the key, while its corresponding historical description was stored as the value. I inserted the years in an unsorted order using a `for` loop, displaying each year and its associated record as it was added. This demonstrated how the BST organized values through comparisons rather than requiring the original data to be sorted beforehand. The inserted values populated both the left and right subtrees of the root node.

### 6. In-Order Traversal Demonstration

I used the `inorder()` function to retrieve and display the historical records in ascending chronological order. The function returned the years in sorted order, which I then used to retrieve their corresponding descriptions from the original dictionary. This demonstrated how an in-order traversal could organize the records chronologically even though they had initially been inserted in an unsorted sequence.

### 7. Search Demonstrations

I tested the search function using two years that existed in the tree and two years that were not present. First, I searched for `1902` and `1939`, both of which returned `True`. I then searched for `1925` and `2000`, which returned `False` because neither year had been inserted. These tests demonstrated how the recursive search handled both successful and unsuccessful searches.

### 8. Edge-Case Testing

I tested an empty Binary Search Tree to examine how the search and traversal functions behaved when no nodes were present. I created a separate `BST` object without inserting any values and searched for the year `1900`. The search returned `False` because the tree had no root node to examine. I then performed an in-order traversal, which returned an empty list. This demonstrated that both operations handled an empty tree without producing an error.

### 9. Real-World Scenario

I created a historical records archive based on developments in Warsaw, using years as keys to organize the associated descriptions. This scenario demonstrated how a Binary Search Tree could be used to organize chronological information and retrieve individual records without requiring the original entries to be sorted. By combining insertion, searching, and in-order traversal, the program demonstrated how the same data structure could support adding records, locating specific years, and displaying the archive in chronological order.