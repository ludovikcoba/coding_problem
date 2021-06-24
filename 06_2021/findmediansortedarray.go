package main

import "fmt"

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	var nums_merged []int
	cursor_nums_1 := 0
	cursor_nums_2 := 0
	range_of_merged_vectors := len(nums1) + len(nums2)

	for i := 0; i < range_of_merged_vectors; i++ {

		if cursor_nums_1 < len(nums1) && cursor_nums_2 < len(nums2) {
			if nums1[cursor_nums_1] > nums2[cursor_nums_2] {
				nums_merged[i] = nums1[cursor_nums_1]
				cursor_nums_1++
			} else {
				nums_merged[i] = nums2[cursor_nums_2]
				cursor_nums_2++
			}
		} else if cursor_nums_1 < len(nums1) {
			nums_merged[i] = nums1[cursor_nums_1]
			cursor_nums_1++
		} else if cursor_nums_2 < len(nums2) {
			nums_merged[i] = nums2[cursor_nums_2]
			cursor_nums_2++
		}

	}

	if range_of_merged_vectors == 1 {
		return float64(nums_merged[0])
	}

	if range_of_merged_vectors%2 == 0 {
		return float64(nums_merged[range_of_merged_vectors/2])
	} else {
		results := nums_merged[range_of_merged_vectors/2] + nums_merged[1+range_of_merged_vectors/2]
		return float64(results) / 2
	}
}

func main() {
	fmt.Print(1)
}
