class Solution:
    def countDigit(self, n):
        c= 0
        while(n>0):
            
            n = n//10
            c = c + 1
            
        return c
    
def main():
    n = 5
    sol = Solution()
    a= sol.countDigit(n)
    print(a)
if __name__=="__main__":
    main()