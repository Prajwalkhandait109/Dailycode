'''
Given an array of arr[] positive integers where all numbers occur even number of times except one number which occurs odd number of times. Return that number.

Examples:

Input:arr[] = [1, 2, 3, 2, 3, 1, 3]
Output: 3
Explaination: 3 occurs three times.
Input:arr[] = [5, 7, 2, 7, 5, 2, 5]
Output: 5
Explaination: 5 occurs three times.

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 106
'''
#Solution :
class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        result = 0
        for num in arr:
            result ^= num
        return result
    
#Solution :
from collections import Counter
class Solution:
    def getOddOccurance(self, arr):
        freq = Counter(arr)
        for num, count in freq.items():
            if count % 2 != 0:
                print(num)
        