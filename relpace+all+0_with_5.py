'''
You are given an integer n. You need to convert all zeroes of n to 5.

Examples:

Input: n = 1004
Output: 1554
Explanation: There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.
Input: n = 121
Output: 121
Explanation: Since there are no zeroes in 121, the number remains as 121.
Constraints:
0 <= n <= 104


'''
#Solution 1 : 
class Solution:
    def convertFive(self, n):
        # Code here
        dup = 0
        i = 0
        
        while n>0:
            ld = n % 10
            n = n//10
            if ld == 0:
                ld = 5
            dup= (dup*10) + ld
        while dup>0:
            ld = dup % 10
            dup = dup//10
            i = (i*10) + ld
        if i==0:
            return 5
        else:
            return i
        
        
#solution 2 : optimal
class Solution:
    def convertFive(self, n):
        return int(str(n).replace('0', '5'))
