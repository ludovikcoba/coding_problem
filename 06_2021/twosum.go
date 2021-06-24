package main

import (
	"fmt"
)

func twoSum(nums []int, target int) []int {
	difference_storage := make(map[int]int)

	var result [2]int

	for i, v := range nums {
		if difference_storage[v] > 0 {
			result[0] = difference_storage[v] - 1
			result[1] = i
			return result[:]
		} else {
			temp := target - v
			difference_storage[temp] = i + 1
		}

	}

	return result[:]
}

func main() {

	fmt.Print(twoSum([]int{7, 0, 3, 4}, 7))
}
