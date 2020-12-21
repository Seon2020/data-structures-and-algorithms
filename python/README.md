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
Perform a binary search on a sorted array with only 2 arguments (arr and x). arr is the sorted array and x is the value we are looking for in the array. We want to return the index that x appears in the array. If x does not exist in the array we should return -1. 

## Approach & Efficiency
Created a function that takes in an ordered array and an integer and returns the index that the integer appears in the array. If the integer does not exist in the array, it will return -1. Defined low as 0 (always starting index of array), mid as 0 (to be updated as we go through the while loop), and high as length of array - 1 (to match 0 index concept). Then, find the middle value of the input array and determine whether it is less than, greater than, or equal to the integer argument. If equal, return middle index. If middle value is less than integer, ignore the left half. If middle value is greater than integer, ignore the right half. If the element is not present in the array, then return -1. Keep halving the array until value is found.

## Solution
![](code_challenges/assets/array_binary_search.jpg)

# Singly Linked List

Linked List implementation with two classes: Node and LinkedList

## Challenge
Create two classes, LinkedList and Node. Using test-driven development, implement/test the following features:
1. Can successfully instantiate an empty linked list
2. Can properly insert into the linked list
3. The head property will properly point to the first node in the linked list
4. Can properly insert multiple nodes into the linked list
5. Will return true when finding a value within the linked list that exists
6. Will return false when searching for a value in the linked list that does not exist
7. Can properly return a collection of all the values that exist in the linked list

## Approach & Efficiency
For each of the features/requirements, I started by making a test that would prove that functionality. From there, I updated the Node and LinkedList classes to create the actual functionality that I would then test. After doing this for all of the features, I wrote docstrings to explain the purpose of each function that I constructed. 

## API
Methods:
- LinkedList __init__: This is the constructor for the actual linked list. Head (optional param) defaults to none and represents the head of the linked list.
- Node __init__: This is the Node Constructor. Value param is the value that the node will represent. Next (optional param) defaults to none and represents the next node in the list.
- LinkedList insert: Inserts a value to the head of the linked list. Takes in a value that the new node represents.
- LinkedList includes: Searches the linked list for a specific value. Takes in value we are searching for and outputs a boolean to indicate whether or not the value was found.
- LinkedList __str__: Produces a string representation of the linked list.
