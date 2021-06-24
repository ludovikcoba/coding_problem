package main

import (
	"fmt"
	"math"
)

func lengthOfLongestSubstring(s string) int {

	cursor := 0
	max := 0
	// c r i
	// aaaaa

	for index := 1; index < len(s); index++ {
		for runner := cursor; runner < index; runner++ {
			if s[runner] == s[index] {
				cursor = runner + 1
				max = int(math.Max(float64(max), float64(index-cursor+1)))
				break
			}
		}
	}
	return max
}

func main() {
	fmt.Print(lengthOfLongestSubstring(""))
}
