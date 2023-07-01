Number of 1 Bits
This repository contains a Python solution for the "Number of 1 Bits" problem. Given a positive integer N, the task is to count the number of set bits (bits with a value of 1) in its binary representation.

Problem Description
Given a positive integer N, we need to find the count of set bits in its binary representation. For example, if N is 6, its binary representation is '110', and the count of set bits is 2.

Solution
The solution is implemented in Python and consists of a class Solution with a method setBits(N) that takes a positive integer N as input and returns the count of set bits. The solution uses bitwise operations to iterate through each bit of the number and count the set bits.

Usage
To use the solution, create an instance of the Solution class and call the setBits(N) method with the desired input value. The method will return the count of set bits in the binary representation of N.

CODE:
class Solution:
    def setBits(self, N):
        count = 0
        while N > 0:
            count += N & 1
            N >>= 1
        return count

