# Coding Challenge - Path Reduction
## Background
We are given paths to go from one point to another. The paths are "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going one path and coming back the opposite path is a wasted effort, so let's concise these paths to go the shortest route.

For example, given the following paths:

You can immediately see that going "NORTH" and then "SOUTH" is not reasonable, better stay to the same place!So the task is to reduce a simplified version of the plan. 

A better plan in this case is simply:

Other examples:In ["NORTH", "SOUTH", "EAST", "WEST"], the path "NORTH" + "SOUTH" is going north and coming back right away. What a waste of time! Better to do nothing. 

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] .In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

## Task
You have to write a function pathReduc which will take a list of strings and returns a list of strings with the needless paths removed (W<->E or S<->N side by side).

The task will not only be assessed on correct functionality but also how optimal the code is from a performance perspective.
## Specification
> TeliaChallenge.pathReduc(ls)
> 
> Parameters
> 
> ls: List<String> - A list with each item as 1 of the 4 cardinal paths, all in uppercase
> 
> Return Value
> 
> List<String> - The optimized set of instructions
> 
## Examples
| list | Return Value|
| ----------- | ----------- |
|["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","WEST"] | ["WEST"]|
|["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"] | []|
|["NORTH","WEST","SOUTH","EAST"] | ["NORTH","WEST","SOUTH","EAST"]|


### Note
Not all paths can be made simpler.

The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].

Difficulty Estimates

Intermediate Difficulty, 30 Minutes Estimated Time
