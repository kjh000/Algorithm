
# Python3 program to find the count  
# of subarrays of an Array having all 
# unique digits  
  
# Function to obtain  
# the mask for any integer  
def getmask(val): 
      
    mask = 0
      
    if val == 0: 
        return 1
  
    while (val):  
        d = val % 10;  
        mask |= (1 << d)  
        val = val // 10
  
    return mask 
  
# Function to count the number of ways  
def countWays(pos, mask, a, n): 
  
    # Subarray must not be empty  
    if pos == n :  
        if mask > 0: 
            return 1
        else: 
            return 0
  
    # If subproblem has been solved  
    if dp[pos][mask] != -1: 
        return dp[pos][mask] 
  
    count = 0
  
    # Excluding this element in the subarray  
    count = (count + 
             countWays(pos + 1, mask, a, n)) 
  
    # If there are no common digits  
    # then only this element can be included  
    if (getmask(a[pos]) & mask) == 0: 
  
        # Calculate the new mask  
        # if this element is included  
        new_mask = (mask | (getmask(a[pos]))) 
  
        count = (count + 
                 countWays(pos + 1,  
                           new_mask, 
                           a, n)) 
  
    # Store and return the answer  
    dp[pos][mask] = count 
    return count 
  
# Function to find the count of  
# subarray with all digits unique  
def numberOfSubarrays(a, n): 
      
    return countWays(0, 0, a, n) 
  
# Driver Code 
N = 4
A = [ 1, 12, 23, 34 ] 
  
rows = 5000
cols = 1100
  
# Initializing dp 
dp = [ [ -1 for i in range(cols) ] 
            for j in range(rows) ]  
              
print( numberOfSubarrays(A, N)) 
  
# This code is contributed by sarthak_eddy. 