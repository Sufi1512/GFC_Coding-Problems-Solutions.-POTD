Given an array arr[] of n positive integers. The task is to find the maximum of j - i subjected to the constraint of arr[i] <= arr[j].

Example 1:

Input:
n = 9
arr[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}
Output: 
6
Explanation: 
In the given array arr[1] < arr[7]  satisfying 
the required condition (arr[i] <= arr[j])  thus 
giving the maximum difference of j - i which is
6(7-1).
Example 2:

Input:
N = 2
arr[] = {18, 17}
Output: 
0
Explanation: 
We can either take i and j as 0 and 0 
or we cantake 1 and 1 both give the same result 0.
Your Task:
Complete the function maxIndexDiff() which takes array arr and size n, as input parameters and returns an integer representing the answer. You don't to print answer or take inputs. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 106
0 ≤ Arr[i] ≤ 109

CODE:
class Solution:
    def maxIndexDiff(self, arr, n):
        maxDiff=0
        minleft=[float('inf')]*n
        maxright=[float('-inf')]*n
        
        minleft[0]=arr[0]
        for i in range (1,n):
            minleft[i]=min(minleft[i-1],arr[i])
        maxright[n-1]=arr[n-1]
        for i in range(n-2,-1,-1):
            maxright[i]=max(maxright[i+1],arr[i])
            
        i=0
        j=0
        while i<n and j<n:
            if minleft[i]<=maxright[j]:
                maxDiff=max(maxDiff,j-i)
                j+=1
                
            else:
                i+=1
        return maxDiff
