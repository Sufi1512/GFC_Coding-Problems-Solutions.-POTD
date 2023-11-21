Exclusively for Freshers! Participate for Free on 21st November & Fast-Track Your Resume to Top Tech Companies

banner
Given a Binary Tree. Check whether it is Symmetric or not, i.e. whether the binary tree is a Mirror image of itself or not.

Example 1:

Input:
         5
       /   \
      1     1
     /       \
    2         2
Output: 
True
Explanation: 
Tree is mirror image of itself i.e. tree is symmetric
Example 2:

Input:
         5
       /   \
      10     10
     /  \     \
    20  20     30
Output: 
False
Your Task:
You don't need to read input or print anything. Your task is to complete the function isSymmetric() which takes the root of the Binary Tree as its input and returns True if the given Binary Tree is the same as the Mirror image of itself. Else, it returns False.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
0<=N<=105

Solution:

class Solution:
    def isSymmetric(self, root):
        # Helper function to check symmetry between two nodes
        def isSymmetricNodes(node1, node2):
            # Base case: Both nodes are None, indicating symmetry
            if not node1 and not node2:
                return True
            # If one node is None and the other is not, it's not symmetric
            elif not node1 or not node2:
                return False
            # If data of the nodes is not equal, it's not symmetric
            elif node1.data != node2.data:
                return False
            # Recursively check symmetry of subtrees
            return isSymmetricNodes(node1.left, node2.right) and isSymmetricNodes(node1.right, node2.left)

        # Check symmetry starting from the left and right subtrees of the root
        return True if not root else isSymmetricNodes(root.left, root.right)
