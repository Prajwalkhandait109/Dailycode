class solution:
    def armstrong(self,n):
        k = len(str(n))
        dup = n
        sum1 = 0
        while n > 0 :
            ld = n % 10
            sum1 = sum1 + (ld**k)
            n = n // 10
        if dup == sum1:
            print("True")
        else:
            print("False")
        
def main():
    n = 145
    sol = solution()
    sol.armstrong(n)
    
if __name__ == "__main__":
    main()
    
    