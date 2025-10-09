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
            
        
    '''
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5

    '''        

    def pattern3(self,n):
        for i in range(n):
            for j in range(i+1):
                print(j+1,end = " ")
            print()
            
    '''
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    
    '''
    def pattern4(self,n):
        for i in range(n):
            for j in range (i+1):
                print(i+1,end = " ")
            print()
            
        
def main():
    n = 5  
    printer = patternPrinter()
    printer.pattern4(n)

if __name__ == "__main__":
    main()