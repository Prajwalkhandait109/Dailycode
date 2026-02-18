# Complete the function below to check if n is a prime number
def isPrime(n):
    # Your code here
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True

def main():
    # Test Case 1: Prime
    print(isPrime(13))   # Expected: True
    
    # Test Case 2: Non-prime
    print(isPrime(15))   # Expected: False
    
    # Test Case 3: 2 (only even prime)
    print(isPrime(2))    # Expected: True
    
    # Test Case 4: 1 (not prime)
    print(isPrime(1))    # Expected: False
    
    # Test Case 5: Larger prime
    print(isPrime(97))   # Expected: True
    
    # Test Case 6: Perfect square
    print(isPrime(49))   # Expected: False

if __name__ == "__main__":
    main()
