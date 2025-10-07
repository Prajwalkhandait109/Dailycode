'''

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
class patternPrinter:
    def pattern1(self,n):
        for i in range(n):
            for j in range(n):
                print("*",end = "")
            print()
      
#Pattern 2     
'''
*
* *
* * *
* * * *
* * * * *

''' 
def pattern2(self,n):
    for i in range(n):
        for j in range(i+1):
            print("*",end = " ") 
        print()    
        
def main():
    n = 5  
    printer = patternPrinter()
    printer.pattern2(n)

if __name__ == "__main__":
    main()