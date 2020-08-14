"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def find_k_as_sum(k, lst):
    adict = {}

    for i in lst:

        if k-i in adict:
            return True
        elif not i in adict: adict[i] = None

    return False


if __name__ == "__main__":
    a = [10, 15, 3, 7]

    print(find_k_as_sum(17,a))
    print(find_k_as_sum(16,a))