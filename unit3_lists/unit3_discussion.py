"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # Inserting a value shifts the existing elements at and after the specified
    # index one position to the right to make room for the new element.
    lst.insert(index, value)

    # Insertion at the beginning requires shifting all elements, while insertion
    # in the middle shifts only the elements after the insertion point.
    # Insertion at the end does not require shifting existing elements,
    # making it generally faster.


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Using try/except checks whether the index is valid before completing the deletion. 
    # This prevents the program from crashing if the index does not exist.
    try:
        return lst.pop(index)
    except IndexError:
        # Return None if the index is invalid so the program can continue safely.
        return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # enumerate() provides both the index and the current element.
    # A linear search checks each element sequentially, starting at the
    # beginning of the list and moving forward until a match is found.
    for index, item in enumerate(lst):
        if item == value:
            return index

    # If the loop finishes without finding a match, return -1.
    return -1    


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # Example findings already flagged by the user.
    flagged_findings = [
        "BRCA1: Example variant A",
        "CFTR: Example variant B"
    ]

    print("Original flagged findings:", flagged_findings)

    # Add a finding at the beginning.
    insert_at(flagged_findings, 0, "HBB: Example variant C")
    print("After insertion at beginning:", flagged_findings)

    # Add a finding in the middle.
    insert_at(flagged_findings, 1, "APOE: Example variant D")
    print("After insertion in middle:", flagged_findings)

    # Add a finding at the end.
    insert_at(flagged_findings, len(flagged_findings),
              "TP53: Example variant E")
    print("After insertion at end:", flagged_findings)


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # A separate list of findings currently flagged by the user.
    flagged_findings = [
        "BRCA1: Example variant A",
        "CFTR: Example variant B",
        "HBB: Example variant C",
        "APOE: Example variant D",
        "TP53: Example variant E"
    ]

    print("Original flagged findings:", flagged_findings)

    # Remove the first flagged finding.
    removed = delete_at(flagged_findings, 0)
    print("Removed finding:", removed)
    print("Updated list:", flagged_findings)

    # Remove a finding from the middle.
    removed = delete_at(flagged_findings, 1)
    print("Removed finding:", removed)
    print("Updated list:", flagged_findings)

    # Remove the last finding.
    removed = delete_at(flagged_findings, len(flagged_findings) - 1)
    print("Removed finding:", removed)
    print("Updated list:", flagged_findings)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Genes identified in the parsed genetic data.
    parsed_genes = ["BRCA1", "BRCA2", "CFTR", "HBB", "APOE"]

    print("Genes in parsed data:", parsed_genes)

    # Search for a gene that exists.
    target_gene = "CFTR"
    result = search_value(parsed_genes, target_gene)

    if result != -1:
        print(f"{target_gene} found at index {result}.")
    else:
        print(f"{target_gene} was not found.")

    # Search for a gene that does not exist.
    target_gene = "EGFR"
    result = search_value(parsed_genes, target_gene)

    if result != -1:
        print(f"{target_gene} found at index {result}.")
    else:
        print(f"{target_gene} was not found in the parsed data.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Attempt to remove a finding using an invalid index.
    test_findings = [
        "BRCA1: Example variant A",
        "CFTR: Example variant B"
    ]

    print("Original list:", test_findings)

    removed = delete_at(test_findings, 10)

    if removed is None:
        print("Cannot remove finding: index 10 is invalid.")
    else:
        print("Removed finding:", removed)

    print("List after attempted deletion:", test_findings)

    # Edge case 2: Attempt to remove a finding from an empty list.
    empty_findings = []

    removed = delete_at(empty_findings, 0)

    if removed is None:
        print("Cannot remove finding: the list is empty.")

    # Edge case 3: Insert a finding into an empty list.
    insert_at(empty_findings, 0, "MYH7: Example variant F")

    print("After inserting into empty list:", empty_findings)


    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD SCENARIO ===")

    # Simulate a user looking up a gene in parsed genetic data
    # and flagging an associated finding for later reference.
    parsed_genes = ["BRCA1", "BRCA2", "CFTR", "HBB", "APOE"]
    flagged_findings = []

    target_gene = "CFTR"
    finding = "CFTR: Example variant B"

    gene_index = search_value(parsed_genes, target_gene)

    if gene_index != -1:
        print(f"Gene {target_gene} found at index {gene_index}.")

        insert_at(flagged_findings, len(flagged_findings), finding)
        print("Finding added to flagged list.")

    else:
        print(f"Gene {target_gene} was not found.")

    print("Flagged findings:", flagged_findings)



if __name__ == "__main__":
    main()