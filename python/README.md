# Data Structures and Algorithms

## Language: `Python`

# Table of Contents Code 401

# Reverse an Array
[Code For Array Reverse Challenge](code_challenges/array_reverse/array_reverse.py)

## Challenge
Take list as an argument and reverse it without using any built-in Python reverse functions. 

## Approach & Efficiency
We kept it simple by creating a function that takes in a single list as an argument. We decided to use slicing to reverse the list because it results in short, easy-to-read code. Big O was O(N) - grows linearly and in direct proportion to the size of the input data set. 

## Solution
![](code_challenges/assets/array-reverse.jpg)

# Shift an Array
[Code For Array Shift Challenge](code_challenges/array_shift/array_shift.py)

## Challenge
When given a list (array) as an argument, along with a single value as a second argument, we want to be able to insert that value in the middle of the array without removing any pre-existing values in the array. We want to shift the existing values to the right of where the new value is being placed (the middle).

## Approach & Efficiency
We kept it simple by creating a function that takes in a list (array) and a new value to be added. We took the length of the list argument and divided by 2 to get the middle position. In case of an odd length, we then used math.ceil to ensure that length is rounded up. We then used insert() to insert the new value at the correct middle position. Finally, we returned the array with the new value. Big O was O(1) - Constant time algorithms take the same amount of time to be executed. Execution time of O(1) algorithms is independent of input size.

## Solution
![](code_challenges/assets/codechal2.jpg)

# Array Binary Search
[Code For Array Binary Search Challenge](code_challenges/array_binary_search/array_binary_search.py)

## Challenge
When given a list (array) as an argument, along with a single value as a second argument, we want to be able to insert that value in the middle of the array without removing any pre-existing values in the array. We want to shift the existing values to the right of where the new value is being placed (the middle).

## Approach & Efficiency
We kept it simple by creating a function that takes in a list (array) and a new value to be added. We took the length of the list argument and divided by 2 to get the middle position. In case of an odd length, we then used math.ceil to ensure that length is rounded up. We then used insert() to insert the new value at the correct middle position. Finally, we returned the array with the new value. Big O was O(1) - Constant time algorithms take the same amount of time to be executed. Execution time of O(1) algorithms is independent of input size.

## Solution
![](code_challenges/assets/array_binary_search.jpg)
