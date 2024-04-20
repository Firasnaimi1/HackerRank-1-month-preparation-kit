""" Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with places after the decimal. """

def plusMinus(arr) :
    
   ## Initializing variables to count the number of positive, negative, and zero integers
    positives = 0
    negatives = 0
    zeros = 0
    
    ## Counting the number of positive, negative, and zero integers in the array
    for i in arr:
        if i > 0:
            positives += 1
        elif i < 0:
            negatives += 1
        elif i == 0:
            zeros += 1
            
    ## Calculating the ratios of positive, negative, and zero integers to the total number of elements
    qt1 = "{:.6f}".format(positives / len(arr))
    qt2 = "{:.6f}".format(negatives / len(arr))
    qt3 = "{:.6f}".format(zeros / len(arr))
    
    print(qt1)
    print(qt2)
    print(qt3)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
