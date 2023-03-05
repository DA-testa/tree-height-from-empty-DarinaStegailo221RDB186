# 221RDB186 Darina Stegailo 7.grupa
# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    
    # Write this function
    h = n*[-1]
    
    def height(node):
        if h[node] != -1:
            return h[node]
        if parents[node] == -1:
             h[node] = 1
        else:
             h[node] = height(parents[node])+1
        return  h[node]
   
    max_height = 0
    
    # Your code here
    for root in range(n):
        max_height = max(max_height,height(root))
        
    return max_height


def main():
    
    # implement input form keyboard and from files
    text = input("Input from keyboard or from files: ")
    if "k" in text:
       n = int(input())
       parents = list(map(int, input().split()))
    elif "f" in text:
        file = input()
        test ='./test/'
        file = test+file
        
        # let user input file name to use, don't allow file names with letter a
        if "a" not in file:
            try:
                with open(file) as x:
                    n=int(x.readline())
                    parents=list(map(int,x.readline().split()))
            except Exception as y:
                print("Error",str(y))
                return
            
        # account for github input inprecision
        # input number of elements
        # input values in one variable, separate with space, split these values in an array
        else:
            print("Error")
            return    
    # call the function and output it's result
    print(compute_height(n,parents))    
    
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
