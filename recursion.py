# print numbers in reverse order
def traditional(n):
    for i in range(n-1,-1,-1):
        print(i)
    
def count(n):
    if n == 3:
        return
    #print(n) # this is executed before function call 
    count(n + 1)
    print(n) # this is executed after the base condition so every function call in stack gets out the print statement will be executed

def main():
    count(0)
    traditional(3)

if __name__ == "__main__":
    main()