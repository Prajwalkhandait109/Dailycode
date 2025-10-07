'''Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

Examples:

Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
Output: false
Explanation: b[] is not a subset of a[]
Constraints:
1 <= a.size(), b.size() <= 105
1 <= a[i], b[j] <= 10'''

Solution 1 :
# solved most test cases but failed for some

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        for i in a:
            found = False
            for j in b:
                
                if i==j:
                    Found=True
                    break
           
            if not found:
                return False
                    
        return True
        
    
    
    
    
Solution 2 : #optimal solution


from collections import Counter

class Solution:
    # Function to check if b is a subset of a (frequency matters)
    def isSubset(self, a, b):
        count_a = Counter(a)
        count_b = Counter(b)
        
        for num in count_b:
            if count_b[num] > count_a.get(num, 0):
                return False
        return True
