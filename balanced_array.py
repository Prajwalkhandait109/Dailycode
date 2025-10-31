'''
Given an array arr of even size, the task is to find a minimum value that can be added to an element so that the array becomes balanced. An array is balanced if the sum of the left half of the array elements is equal to the sum of the right half.

Examples :

Input: arr = [1, 5, 3, 2]
Output: 1
Explanation: Sum of first 2 elements is 1 + 5  = 6, Sum of last 2 elements is 3 + 2  = 5, To make the array balanced you can add 1.
Input: arr = [1, 2, 1, 2, 1, 3]
Output: 2
Explanation: Sum of first 3 elements is 1 + 2 + 1 = 4, Sum of last three elements is 2 + 1 + 3 = 6, To make the array balanced you can add 2.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
2<=arr.size()<=107 where arr.size() is even.
1<=arr[i]<=105
'''

#Solution :
#User function Template for python3


class Solution:
    # Function to find the minimum value required to balance the array.
    def min_value_to_balance(self, arr):
        # code here
        mid = len(arr)//2
        
        lefth = arr[:mid]
        left_sum = 0
        for i in lefth:
            left_sum += i
            
        right_sum =  0   
        righth = arr[mid:]
        for i in righth:
            right_sum += i
            
        if right_sum >= left_sum:
            return right_sum - left_sum
        else:
            return left_sum - right_sum