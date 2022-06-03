#User function Template for python3

def getMinMax( a, n):
    mini = 10000000000000000
    maxi = -10000000000000000
    for A in a:
        if A < mini:
            mini = A
        if A > maxi:
            maxi = A
    return mini, maxi
    
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends