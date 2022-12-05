# Coding Challenge – The Grocery Store simulation

## Background
In this assignment, we are simulating a grocery store checkout line to see the total time required to check out for all the customers.

## Task
Your task is to write a function computeCheckoutTime which will take an array of positive integers representing the customers and returns an integer which would be the total time required to check out for all the customers.

The task will not only be assessed on correct functionality but also how optimal the code is from a performance perspective.

## Specifications

### input
customers: an array of positive integers representing the customers. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout counters.

### output
The function should return an integer, the total time required.

__Important__

__Please look at the examples and clarifications below, to ensure you understand the task correctly :)__

## Examples
> computeCheckoutTime([5,3,4], 1)
>> should return 12 <br>
>> because when n=1, the total time is just the sum of the times

> computeCheckoutTime([10,2,3,3], 2)
>> should return 10<br>
>> Because here n=2 and the 2nd, 3rd, and 4th people in the <br>
>> queue finish before the 1st person has finished.

> computeCheckoutTime([2,3,10], 2)
>> Should return 12


## Clarifications
There is only ONE customer queue serving many counters, and

The order of the queue NEVER changes, and

The front person in the queue (i.e. the first element in the array/list) proceeds to a counter as soon as it becomes free.

__N.B. You should assume that all the test input will be valid, as specified above.__

Difficulty Estimates

Intermediate Difficulty, 45 Minutes Estimated Time

