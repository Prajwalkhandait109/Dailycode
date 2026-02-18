# Complete the function below to find GCD of a and b
def gcd(a, b):
    # Your code here
    result = 1
    n = min(a,b)
    if n == 0 and a > b:
        return a
    elif n == 0 and a<b:
        return b
    for i in range(1,n+1):
        if(a % i == 0 and b % i == 0): 
            result = i
    return result

def main():
    # Test Case 1: Basic
    print(gcd(48, 18))   # Expected: 6
    
    # Test Case 2: Prime numbers
    print(gcd(13, 17))   # Expected: 1
    
    # Test Case 3: One is multiple
    print(gcd(100, 25))  # Expected: 25
    
    # Test Case 4: Same numbers
    print(gcd(7, 7))     # Expected: 7
    
    # Test Case 5: 1 and any
    print(gcd(1, 100))   # Expected: 1
    
    # Test Case 6: 0 edge case
    print(gcd(5, 0))     # Expected: 5

if __name__ == "__main__":
    main()
