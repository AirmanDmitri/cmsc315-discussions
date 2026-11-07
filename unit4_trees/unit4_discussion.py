"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Insertion depends on whether the value is smaller or larger 
        # because a BST maintains a strict ordering property: 
        # smaller values go left, and larger values go right. 
        # This structure ensures the tree remains organized, allowing 
        # future insertions and searches to quickly narrow down the path 
        # instead of looking at every single node.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: If None, the empty spot for the new node is found
        if node is None:
            return Node(value)
            
        # If the value is smaller than the current node's value, continues down the left branch.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
            
        # If the value is larger (or equal), continues down the right branch.
        else:
            node.right = self._insert_recursive(node.right, value)

        # Returns the updated node reference back up the chain so parent pointers stay connected
        return node
        
    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search is much more efficient than a linear search (O(log n) vs O(n))
        # because the tree's strict ordering property allows us to eliminate 
        # half of the remaining search space at every single step. 
        # Instead of checking every node one by one, we compare the target value 
        # to the current node and immediately discard an entire subtree (left or right).
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base case 1: If None, the value is not in the tree
        if node is None:
            return False
            
        # Base case 2: The value is found
        if node.value == value:
            return True   
            
        # If the target value is smaller, looks down the left subtree
        if value < node.value:
            return self._search_recursive(node.left, value)
            
        # If the target value is larger, looks down the right subtree
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # Why this produces sorted output:
        # In a BST, the structural property dictates that every node in the left subtree 
        # is smaller and every node in the right subtree is larger. By recursively diving 
        # all the way down to the smallest leaf on the left first, then recording the parent, 
        # and then moving to the right, we naturally process and collect all elements in 
        # ascending, sorted order.
        if node is not None:
            # 1. Visit the left subtree first (contains all values smaller than the current node)
            self._inorder_recursive(node.left, values)
            
            # 2. Visit the current node (add its value to our list)
            values.append(node.value)
            
            # 3. Visit the right subtree last (contains all values larger than the current node)
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")



if __name__ == "__main__":
    main()