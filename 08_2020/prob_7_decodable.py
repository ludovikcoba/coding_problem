"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def count_decode(s):
    count = 0
    if len(s) <= 1: 
        return 1

    if int(s[-1:]) > 0:
        count = count_decode(s[:-1])
    
    if 26 - int(s[-2:]) >= 0:
        count += count_decode(s[:-2])

    return count
    
def count_decode_DP(s):
    n = len(s)
    count = [0] * (n + 1)
    count[0] = 1
    count[1] = 1

    for i in range(2, n+1):

        if s[i-1] > '0':
            count[i] = count[i-1]

        if 26 - int(s[i-2:i]) >= 0:
            count[i] += count[i-2]

    return count[n]


if __name__ == "__main__":
    print(count_decode_DP('111'))
    print(count_decode('1234'))