Rearrange an Array with O(1) Extra Space
This repository contains the solution to the problem of rearranging an array with O(1) extra space. The problem involves rearranging an array arr of size N such that the transformed array arrT satisfies the condition arrT[i] = arr[arr[i]].

Problem Description
You are given an array arr of size N, where every element is in the range from 0 to N-1. Your task is to rearrange the array arr in such a way that arr[i] becomes arr[arr[i]] for every index i.

Solution Approach
The solution to this problem can be achieved by using the concept of modulo arithmetic. We can encode two values in a single index by taking the modulo of the elements and storing them at the same index. The transformed value arrT[i] can be obtained as arrT[i] = arr[i] + arr[arr[i]] * N. To retrieve the original values, we can use the expression arr[i] = arrT[i] % N and arr[arr[i]] = arrT[i] // N.

The arrange function implements this approach. It takes the array arr and the size n as input and rearranges the array according to the specified transformation.


CODE:
class Solution:
    # Function to rearrange an array so that arr[i] becomes arr[arr[i]]
    # with O(1) extra space.
    def arrange(self, arr, n):
        # Modify the array in-place
        for i in range(n):
            arr[i] += (arr[arr[i]] % n) * n

        # Retrieve the original values
        for i in range(n):
            arr[i] //= n

        # Return the rearranged array
        return arr
