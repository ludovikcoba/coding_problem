"""
Given an array of numbers, find the length of the longest increasing subsequence in the array. 
The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: 
it is 0, 2, 6, 9, 11, 15.
"""

def find_subsequence_naive(seq):

    cnt_vec = [1] * len(seq)

    print(cnt_vec)

    for i in range(1, len(seq)):
        for j in range(i):

            if seq[j] < seq[i]:
                cnt_vec[i] = max(cnt_vec[i], cnt_vec[j] + 1)

    return max(cnt_vec)



def find_subsequence(seq):
    if len(seq) == 1:
        return 1

    return scan_subsequences(seq, seq[0], 1, 0)

def scan_subsequences(seq, last_max_num, pos, count):

    if pos == len(seq) - 1:
        if last_max_num < seq[pos]:
            return count + 1
        else:
            return 0

    prov_max = count
    
    for i in range(pos, len(seq)):
        if seq[i] > last_max_num:
            temp_cnt = scan_subsequences(seq, seq[i], i + 1, prov_max + 1)
        else:
            temp_cnt = scan_subsequences(seq, last_max_num, i + 1, prov_max)

        prov_max = max(prov_max, temp_cnt)
        
        return prov_max

if __name__ == "__main__":
    seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(find_subsequence_naive(seq))