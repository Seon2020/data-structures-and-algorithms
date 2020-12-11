import math

def insertShiftArray(arr, n):
  """
  When given a list (array) as an argument, along with a single value as a second argument, we want to be able to insert that value in the middle of the array without removing any pre-existing values in the array. We want to shift the existing values to the right of where the new value is being placed (the middle).
  """
  position = len(arr)/2
  position = math.ceil(position)
  arr.insert(position, n)
  return arr

