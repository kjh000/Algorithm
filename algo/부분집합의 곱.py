# Python3 program to find product 
# of all subarray of an array 
  
# Function to find product of all subarrays 
def product_subarrays(arr, n): 
  
    # Variable to store the product 
    res = 1; 
  
    # Compute the product while 
    # traversing for subarrays 
    for i in range(n): 
        product = 1
        for j in range(i, n): 
            product *= arr[j]; 
            res = res * product 
  
    # Printing product of all subarray 
    print(res); 
  
# Driver code 
if __name__ == '__main__': 
    arr = [ 10, 3, 7 ]; 
  
    n = len(arr); 
  
    # Function call 
    product_subarrays(arr, n); 
  
# This code is contributed by Princi Singh 
