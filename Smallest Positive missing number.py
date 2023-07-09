Smallest Positive missing number
You are given an array arr[] of N integers including 0. The task is to find the smallest positive number missing from the array.

Example 1:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing 
number is 6.
Example 2:

Input:
N = 5
arr[] = {0,-10,1,3,-20}
Output: 2
Explanation: Smallest positive missing 
number is 2.
Your Task:
The task is to complete the function missingNumber() which returns the smallest positive missing number in the array.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106
-106 <= arr[i] <= 106

CODE:
class Solution:
    def missingNumber(self, arr, n):
        # Create a HashSet to store the elements of the array
        num_set = set(arr)

        # Check for the smallest positive missing number
        for i in range(1, n + 1):
            if i not in num_set:
                return i

        # If no missing number is found, return n + 1
        return n + 1
