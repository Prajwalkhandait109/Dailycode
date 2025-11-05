'''
You are given an array arr[] having unique elements. Your task is to return the type of array.
Note: The array can be categorized into ascending, descending, descending rotated and ascending rotated followed by:

Return 1 if the array is in ascending order
Return 2 if the array is in descending order
Return 3 if the array is in descending rotated order
Return 4 if the array is in ascending rotated order
Examples:

Input: arr[] = [2, 1, 5, 4, 3]
Output: 3
Explanation: Descending rotated, rotate 2 times left.
Input: arr[] = [3, 4, 5, 1, 2]
Output: 4
Explanation: Ascending rotated, rotate 2 times right. 
Constraints:
3 <= arr.size() <= 105
1 <= arr[i] <= 106


'''

#solution :
#User function Template for python3

class Solution:
    def maxNtype(self , arr):
        #code here.
        case1 = all(arr[i] < arr[i+1] for i in range(len(arr) - 1))
        
        case2 = all(arr[i] > arr[i+1] for i in range(len(arr) - 1))
        
        
        if case1:
            return 1
        elif case2:
            return 2
            
        count = 0
        def case3(arr):
            count = 0
            for i in range(len(arr)-1):
                if arr[i] < arr[i+1]:
                    count += 1
            if arr[-1] < arr[0]:  # Also check circular break for rotation
                count += 1
            return count
            
            
        def case4(arr):
            count = 0
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    count += 1
            if arr[-1] > arr[0]:
                count += 1
            return count
            
        
        if case3(arr) == 1:
            return 3
        if case4(arr) == 1:
            return 4