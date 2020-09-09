"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def non_adjacent_sum(a:list):

    if len(a) == 0:
        return 0
    
    if len(a) == 1:
        return a[0]

    sums = [0] * 2 

    sums[0] = a[0] 
    sums[1] = max(a[0], a[1])

    for i in range(2, len(a)):
        temp = max(sums[i%2], sums[i%2] + a[i]) # the number we are adding is negative so we might not want it
        temp = max(temp, a[i]) # we had only negative numbers so far so we might not need them
        sums[i%2] = max(sums[(i-1)%2], temp) # we compare it to the first

    return sums[(len(a) - 1)%2]


if __name__ == "__main__":
    
    print(non_adjacent_sum([5, 1, 1, 5]))
    print(non_adjacent_sum([-2, 4, 6, 2, -5, 5]))
    print(non_adjacent_sum([5, 5, 10, 100, 10, 5]))