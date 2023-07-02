Given two numbers X and Y, and a range [L, R] where 1 <= L <= R <= 31. You have to copy the set bits of 'Y' in the range L to R in 'X'. Return this modified X.

Note: Range count will be from Right to Left & start from 1.

Example 1:

Input: 
X = 44, Y = 3 
L = 1,  R = 5
Output: 
47
Explaination: 
Binary represenation of 44 and 3 is 101100 and 000011. So in the range 1 to 5 there are two set bits of 3 (1st & 2nd position). If those are set in 44 it will become 101111 which is 47.
Example 2:

Input: 
X = 16, Y = 2
L = 1,  R = 3
Output: 18
Explaination: Binary represenation of 16 and 2 is 10000 and 10. If the mentioned conditions are applied then 16 will become 10010 which is 18.
Your Task:
You do not need to read input or print anything. Your task is to complete the function setSetBit() which takes the numbers X, Y, L and R as input parameters and returns the modified value of X.

Expected Time Complexity: O(R - L)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ X, Y ≤ 109
1 ≤ L ≤ R ≤ 32

CODE:
  class Solution:
    def setSetBit(self,x, y, l, r):
   
    # l and r must be between 1 to 32
    # (assuming ints are stored using
    # 32 bits)
        if (l < 1 or r > 32):
            return x;
 
    # Traverse in given range
        for i in range(l, r + 1):
       
        # Find a mask (A number whose
        # only set bit is at i'th position)
            mask = 1 << (i - 1);
 
        # If i'th bit is set in y, set i'th
        # bit in x also.
            if ((y & mask) != 0):
                x = x | mask;
        return x;
