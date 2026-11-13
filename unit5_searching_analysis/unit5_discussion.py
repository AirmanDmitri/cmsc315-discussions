"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    comparisons = 0

    # Iterate through every element in the list sequentially
    for i in range(len(lst)):
        comparisons += 1
        if lst[i] == target:
            print("Comparisons:", comparisons)
            return i  # Target found, return its index

    # Linear search checks each element one by one from start to finish.
    # In the worst-case scenario (when the target is at the very end or
    # not in the list at all), the algorithm must inspect all 'n' elements.
    # Because the number of operations grows directly proportional to the size
    # of the dataset, its time complexity is O(n).
    print("Comparisons:", comparisons)
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    left = 0
    right = len(lst) - 1
    comparisons = 0

    while left <= right:
        # Find the middle index of the current active search space
        mid = (left + right) // 2
        comparisons += 1

        # Check if the target is at the middle index
        if lst[mid] == target:
            print("Comparisons:", comparisons)
            return mid

        # If the target is greater than the middle element,
        # it must be in the right half of the remaining elements.
        elif lst[mid] < target:
            left = mid + 1
            # By setting left = mid + 1, we discard the entire left half
            # and the middle element itself, cutting the remaining search space roughly in half.

        # If the target is smaller than the middle element,
        # it must be in the left half.
        else:
            right = mid - 1
            # By setting right = mid - 1, we discard the entire right half
            # and the middle element itself, cutting the remaining search space roughly in half.

    # Target is not in the list
    print("Comparisons:", comparisons)
    return -1

def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # Create a small, sorted dataset containing 10 passenger
    # boarding pass numbers.
    small_dataset = [
        104582, 218394, 325671, 437829, 546193,
        658214, 763921, 875430, 921567, 986321
    ]

    print("Passenger boarding pass numbers:", small_dataset)

    # Test 1: Search for an existing boarding pass.
    existing_target = 546193

    print("\nSearching for existing boarding pass:", existing_target)

    print("\nLinear Search:")
    linear_result = linear_search(small_dataset, existing_target)
    print("Result index:", linear_result)

    print("\nBinary Search:")
    binary_result = binary_search(small_dataset, existing_target)
    print("Result index:", binary_result)

    # Both algorithms find the boarding pass at index 4.
    # Linear search examines the elements sequentially,
    # while binary search reduces the search space by half.

    # Test 2: Search for a nonexistent boarding pass.
    missing_target = 700000

    print("\nSearching for nonexistent boarding pass:", missing_target)

    print("\nLinear Search:")
    linear_result = linear_search(small_dataset, missing_target)
    print("Result index:", linear_result)

    print("\nBinary Search:")
    binary_result = binary_search(small_dataset, missing_target)
    print("Result index:", binary_result)

    # Both algorithms return -1 because the boarding pass
    # is not present in the dataset.


    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    
    # Generate a sorted dataset containing 10,000 passenger
    # boarding pass numbers.
    large_dataset = list(range(100000, 110000))

    print("Number of boarding passes:", len(large_dataset))

    # Test 1: Search for an existing boarding pass near the end.
    existing_target = 109850

    print("\nSearching for existing boarding pass:", existing_target)

    print("\nLinear Search:")
    linear_result = linear_search(large_dataset, existing_target)
    print("Result index:", linear_result)

    print("\nBinary Search:")
    binary_result = binary_search(large_dataset, existing_target)
    print("Result index:", binary_result)

    # Both algorithms find the boarding pass at index 9850.
    # Linear search examines all preceding elements,
    # while binary search repeatedly divides the search space.

    # Test 2: Search for a nonexistent boarding pass.
    missing_target = 115000

    print("\nSearching for nonexistent boarding pass:", missing_target)

    print("\nLinear Search:")
    linear_result = linear_search(large_dataset, missing_target)
    print("Result index:", linear_result)

    print("\nBinary Search:")
    binary_result = binary_search(large_dataset, missing_target)
    print("Result index:", binary_result)

    # Both algorithms return -1 because the boarding pass
    # is not present in the dataset.


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    
    # Test 1: Empty list
    empty_dataset = []
    target = 104582

    print("\nTest 1: Searching an empty list")

    print("\nLinear Search:")
    linear_result = linear_search(empty_dataset, target)
    print("Result index:", linear_result)

    print("\nBinary Search:")
    binary_result = binary_search(empty_dataset, target)
    print("Result index:", binary_result)

    # Both algorithms return -1 because there are no elements
    # to search. Neither algorithm performs any comparisons.

    # Test 2: Single-element list
    single_dataset = [546193]
    target = 546193

    print("\nTest 2: Searching a single-element list")

    print("\nLinear Search:")
    linear_result = linear_search(single_dataset, target)
    print("Result index:", linear_result)

    print("\nBinary Search:")
    binary_result = binary_search(single_dataset, target)
    print("Result index:", binary_result)

    # Both algorithms find the target at index 0.
    # Each algorithm only needs one comparison.

    # Test 3: Target at the first position
    target = small_dataset[0]

    print("\nTest 3: Searching for the first element:", target)

    print("\nLinear Search:")
    linear_result = linear_search(small_dataset, target)
    print("Result index:", linear_result)

    print("\nBinary Search:")
    binary_result = binary_search(small_dataset, target)
    print("Result index:", binary_result)

    # Linear search finds the target immediately because it
    # starts at the beginning of the list.
    # Binary search needs to examine the middle elements first.

    # Test 4: Target at the last position
    target = small_dataset[-1]

    print("\nTest 4: Searching for the last element:", target)

    print("\nLinear Search:")
    linear_result = linear_search(small_dataset, target)
    print("Result index:", linear_result)

    print("\nBinary Search:")
    binary_result = binary_search(small_dataset, target)
    print("Result index:", binary_result)

    # Linear search examines every element before reaching the target.
    # Binary search reduces the search space until it reaches the last element.

    # Edge Case 5: Unsorted list
    unsorted_dataset = [546193, 104582, 986321, 218394, 763921, 437829, 658214, 875430, 325671, 921567]
    target = 325671

    print("\nTest 5: Unsorted List\n")
    print(unsorted_dataset)

    print("\nLinear Search:", target)
    result = linear_search(unsorted_dataset, target)
    print("Result index:", result)

    print("\nBinary Search:", target)
    result = binary_search(unsorted_dataset, target)
    print("Result index:", result)

    # Linear search finds the target at index 8 because it examines
    # each element sequentially, regardless of the list's order.

    # Binary search returns -1 in this example, even though the target
    # exists in the list. Its result is unreliable because the list
    # is not sorted, which is a requirement for binary search.


if __name__ == "__main__":
    main()