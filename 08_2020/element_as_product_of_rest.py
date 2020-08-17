"""Given an array of integers, return a new array such that each element at index i of the new array is the product 
of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?"""

def product_of_rest(inp):

    sz = len(inp)

    ord = [0 for i in range(sz)]
    ord[0] = inp[0]

    rvo = [0 for i in range(sz)]
    rvo[-1] = inp[-1]

    for i in range(1, sz):
        ord[i] = inp[i] * ord[i-1]
        rvo[-(i+1)] = inp[-(i+1)] * rvo[-i]

    res = []
    res.append(rvo[1])

    for i in range(1, sz-1):
        res.append(ord[i-1] * rvo[i+1])

    res.append(ord[-2])

    return res


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]

    print(product_of_rest(a))