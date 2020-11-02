"""
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
"""

def change_one(vec):

    l = len(vec)

    if l == 1:
        return True

    count = 0

    
    if vec[1] < vec[0]:
        count += 1

    i = 1

    while i < l-1:
        if count > 1:
            return False

        if vec[i] < vec[i - 1] or vec[i] > vec[i+1]:
            if vec[i-1] < vec[i+1]:
                count += 1
                i = i + 2
            else:
                return False
        else:
            i += 1

        

    return count <= 1


if __name__ == "__main__":
    print(change_one([-1,7,2,3, 5]))