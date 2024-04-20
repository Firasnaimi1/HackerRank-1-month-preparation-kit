""" Given five positive integers, find the minimum and maximum values that can be calculated by 
summing exactly four of the five integers. Then print the respective minimum and maximum values 
as a single line of two space-separated long integers.  """

def miniMaxSum(arr) :
    
    ## Using the sorted() function to create a new sorted list from the elements of arr.
    sorted_arr = sorted(arr)
    ## Calculating the minimum sum by summing the first 4 elements. This operation ensures that we are summing only the smallest elements in the list. 
    min_sum = sum(sorted_arr[:4])
    ## Calculating the maximum sum by summing the last 4 elements. This operation ensures that we are summing only the largest elements in the list.
    max_sum = sum(sorted_arr[-4:])
    
    print(f"{min_sum} {max_sum}")        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
