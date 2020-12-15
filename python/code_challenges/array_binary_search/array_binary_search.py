# Recursive approach:

def get_high(arr):
    high = len(arr)-1
    return high

def binary_search_recursive(arr, x, high=0):
  """
  This function take in an ordered array and an integer and returns the index that the integer appears in the array. If the integer does not exist in the array, it will return -1.

  Arguments: An ordered array and an integer. Function has an optional argument that has a default value of 0 and acts as a placeholder. get_high(arr) will return the starting value of high. This value changes as the function calls itself.  

  Output: The index that they integer appears in the array, or -1 if it does not exist in the array. 
  """
  low = 0
  get_high(arr)
  if x not in arr:
    return -1
  if high >= low: 
    mid = (high + low) // 2
    if arr[mid] == x: 
      return mid 
    elif arr[mid] > x: 
      return binary_search_recursive(arr, x, high - 1) 
    else:
      return binary_search_recursive(arr, x, high + 1) 
    
# Iterative approach:

def binary_search_iterative(arr, x): 
  """
  This function take in an ordered array and an integer and returns the index that the integer appears in the array. If the integer does not exist in the array, it will return -1.

  Arguments: An ordered array and an integer 

  Output: The index that they integer appears in the array, or -1 if it does not exist in the array. 
  """
  low = 0
  mid = 0
  high = len(arr) - 1
  while low <= high: 
    mid = (high + low) // 2
    if arr[mid] < x: 
      low = mid + 1
    elif arr[mid] > x: 
      high = mid - 1
    else: 
      return mid 
  else:
    return -1
