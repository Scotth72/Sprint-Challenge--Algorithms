#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime is O(n^c) because of multiplication of n while loop (n^3)
   the while loop will help reduce increase in runtime complexity when multiplying (n^2).

b) Runtime O(nlogn) because it is a linear loop through the range of n, the while loop inside the loop creates the values to double at a point where it equals/ passes the input n.


c) Runtime O(n) because it runs linear with the input of bunnies, it adds the function one more time causing to run recursive.

## Exercise II

Based on a binary search.
Create a list of floors based on the n sorted stories.
# safe_floor = i+1 for i in range(n)

locate a midpoint

# mid = len(safe_floor) //2

Check the midpoint if eggs fall safely, if so, focus of left side of the list, doing away with half the floors. I am able to repeat the process until I find where the eggs start breaking and where they safely land without breaking finding my endpoint.
 f= end_point
 The runtime is O(logn) by constantly reducng the floors by 2.

