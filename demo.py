
'''
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''
class Solution:
    def pattern(self,n):
        for i in range(n): 
            for j in range(n-i):
                print("*",end = "")
            for k in range(2*i):
                print(" ", end = "")
            for j in range(n-i):
                print("*",end = "")
                
            print()
        for i in range(n-1,-1,-1): 
            for j in range(n-i):
                print("*",end = "")
            for k in range(2*i):
                print(" ", end = "")
            for j in range(n-i):
                print("*",end = "")
            print()
            
        
        
        
        
def main():
    n = 5 
    #m = 5 
    printer = Solution()
    printer.pattern(n)

if __name__ == "__main__":
    main()