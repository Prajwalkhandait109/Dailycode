'''
Segregate Even and Odd numbers
Difficulty: BasicAccuracy: 42.11%Submissions: 37K+Points: 1
Given an array arr, write a program segregating even and odd numbers. The program should put all even numbers first in sorted order, and then odd numbers in sorted order.

Note:- You don't have to return the array, you have to modify it in-place.

Example:

Input: arr[] = [12, 34, 45, 9, 8, 90, 3]
Output: [8, 12, 34, 90, 3, 9, 45]
Explanation: Even numbers are 12, 34, 8 and 90. Rest are odd numbers.
Input: arr[] = [0, 1, 2, 3, 4]
Output: [0, 2, 4, 1, 3]
Explanation: 0 2 4 are even and 1 3 are odd numbers.
Input: arr[] = [10, 22, 4, 6]
Output: [10, 22, 4, 6]
Explanation: Here all elements are even, so no need of segregataion
Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] <=105
'''

#Solution :
class Solution:
    def segregateEvenOdd(self, arr):
        even = [num for num in arr if num % 2 == 0]
        odd = [num for num in arr if num % 2 != 0]
        
        even.sort()            # Ascending order
        odd.sort() 
        
        # Overwrite original array
        for i in range(len(even)):
            arr[i] = even[i]
        for j in range(len(odd)):
            arr[len(even) + j] = odd[j]
        
        return arr