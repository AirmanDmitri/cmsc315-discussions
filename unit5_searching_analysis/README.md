# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.


## Implementation

### 1. Linear Search Function

I implemented the `linear_search()` function to locate a target value in a list by examining its elements sequentially. The function iterates through the list from beginning to end using a `for` loop and compares each element with the target value. If a match is found, the function returns the index of that element. If the target is not present, the function returns -1 after examining the entire list. This approach has O(n) time complexity because, in the worst-case scenario, every element must be examined. As the dataset grows, the number of comparisons increases proportionally to the number of elements.

### 2. Binary Search Function

I implemented the `binary_search()` function to locate a target value in an already sorted list by repeatedly reducing the search space by half. The function initializes two variables, `left` and `right`, to represent the boundaries of the active search range. During each iteration, it calculates the middle index and compares the corresponding element with the target. If the target is greater than the middle element, the search continues through the right half. If it is smaller, the search continues through the left half. This process continues until the target is found or the search range becomes empty. The function returns the target's index if found or -1 otherwise. Since each iteration eliminates approximately half of the remaining elements, binary search has O(log n) time complexity.

### 3. Comparison Counting

I added a comparison counter to both search functions to measure how many elements each algorithm examined during a search. The counter increases each time an element is examined in linear search or a middle element is evaluated in binary search. The program prints the total number of comparisons before returning the search result. This allows me to observe the difference in search efficiency between the two algorithms using actual comparison counts rather than relying only on their theoretical time complexities.

### 4. Small Dataset Demonstration

I created a small, sorted dataset containing ten passenger boarding pass numbers. I tested both search algorithms using a boarding pass number that existed in the list and another number that was not present. Both algorithms successfully located the existing boarding pass at index 4 and returned -1 for the missing value. I also compared their number of comparisons. Linear search required five comparisons to find the existing value and ten comparisons to establish that the missing value was not present. Binary search required only three and four comparisons, respectively. This demonstrated how binary search could locate values more efficiently even in a relatively small dataset.

### 5. Large Dataset Demonstration

I created a larger sorted dataset containing 10,000 consecutive numbers using Python's `range()` function. I tested both algorithms with an existing boarding pass number near the end of the dataset and a number that was not present. Both algorithms located the existing value at index 9850 and returned -1 for the missing value. However, their comparison counts differed significantly. Linear search required 9,851 comparisons to find the existing value and 10,000 comparisons to establish that the missing value was not present. Binary search required only 13 and 14 comparisons, respectively. This demonstrated how the difference in efficiency becomes much more noticeable as the dataset grows.

### 6. Edge-Case Testing

I tested four edge cases to examine how both algorithms behaved under different conditions. First, I searched an empty list, which caused both algorithms to return -1 without performing any comparisons. Second, I tested a list containing only one element. Both algorithms successfully located the target at index 0 using one comparison. I then searched for the first and last elements of the original ten-element dataset. Linear search found the first element immediately but required ten comparisons to find the last one. Binary search required four comparisons for each search. These tests demonstrated how the position of a target and the size of a dataset can affect the number of comparisons required by each algorithm.

### 7. Real-World Scenario

I used passenger boarding pass numbers as a real-world example to demonstrate how search algorithms could be applied in an airport environment. Each number represented an individual passenger's boarding pass and served as the value being searched for. This scenario illustrated how an airport system could locate a passenger's boarding pass number within a collection of records. Linear search could be used when working with a small or unsorted collection, while binary search could provide faster retrieval when the boarding pass numbers were stored in sorted order. The demonstrations showed how choosing an appropriate search algorithm could improve the efficiency of retrieving information as the number of passenger records increases.