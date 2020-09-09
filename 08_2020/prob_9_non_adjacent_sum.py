"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def non_adjacent_sum(a:list):
    sums = [0] * len(a) #can be imporved to having only two variables

    sums[0] = a[0] 
    sums[1] = max(a[0], a[1])

    for i in range(2, len(a)):
        temp = max(sums[i-2], sums[i-2] + a[i], a[i])
        
        sums[i] = max(sums[i-1], temp)

    return sums[len(a) - 1]


if __name__ == "__main__":
    
    print(non_adjacent_sum([5, 1, 1, 5]))
    print(non_adjacent_sum([-2, 4, 6, 2, -5, 5]))
    print(non_adjacent_sum([5, 5, 10, 100, 10, 5]))