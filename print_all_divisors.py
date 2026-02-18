# Complete the function below to print all divisors of n in ascending order
def printDivisors(n):
    # Your code here
    # for i in range(1,n+1):
    #     if n % i == 0:
    #         print(i)
    for i in range(1,int(n ** 0.5) +1):
        if (n % i == 0):
            print(i)
            if n//i != i:
                print(n//i)
    

def main():
    # Test Case 1: Perfect number
    printDivisors(6)     # Expected: 1 2 3 6
    
    print()  # Blank line
    
    # Test Case 2: Prime number
    printDivisors(13)    # Expected: 1 13
    
    print()
    
    # Test Case 3: 1
    printDivisors(1)     # Expected: 1
    
    print()
    
    # Test Case 4: Perfect square
    printDivisors(36)    # Expected: 1 2 3 4 6 9 12 18 36

if __name__ == "__main__":
    main()
