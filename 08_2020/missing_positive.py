"""
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
def segregate(arr, size):
    j=0
    for i in range(size):
        if (arr[i] <= 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return j

def find_missing(arr, size):
    for i in range(size):
        if(arr[i] - 1 < size and arr[arr[i]-1] > 0):
            arr[arr[i] - 1] = -arr[arr[i]-1]

    for i in range(size):
        if(arr[i]>0):
            return i+1
        return size+1
        

def missing_positive(inp):
    shift = segregate(inp, len(inp))
    return find_missing(inp[shift:], len(inp)-shift)


if __name__ == "__main__":
    inp = [3, 4, -1, 1]
    inp2 = [1, 2, 0]

    print(missing_positive(inp2))