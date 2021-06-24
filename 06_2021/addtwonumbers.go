package main

import (
	"fmt"
	"math"
)

type ListNode struct {
	val  int
	Next *ListNode
}

func findLen(l *ListNode) int {
	count := 0

	for l.Next != nil {
		count++
		l = l.Next
	}

	return count
}

func swap(l1 *ListNode, l2 *ListNode) {
	temp := *l1
	*l1 = *l2
	*l2 = temp
}

func sum_two_nodes(l1 *ListNode, l2 *ListNode) (int, int) {
	if l1 == nil {
		return -1, -1
	}
	return (l1.val + l2.val) / 10, (l1.val + l2.val) % 10
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

	len_l1 := findLen(l1)
	len_l2 := findLen(l2)
	if len_l2 > len_l1 {
		swap(l1, l2)
	}

	distance := int(math.Abs(float64(len_l1 - len_l2)))

	var head = ListNode{0, nil}
	cursor := &head

	for i := 0; i < distance; i++ {
		cursor.Next = &ListNode{0, nil}
		cursor.Next.val = l1.val
		cursor = cursor.Next
		l1 = l1.Next
	}

	for l1 != nil {
		quotient, remainder := sum_two_nodes(l1, l2)

		if quotient != -1 {
			cursor.Next = &ListNode{0, nil}
			if remainder == 9 {
				next_reminder, _ := sum_two_nodes(l1.Next, l2.Next)
				if next_reminder != -1 {
					quotient = (next_reminder + remainder) / 10
					remainder = (next_reminder + remainder) % 10
				}
			}
			cursor.val += quotient
			cursor.Next.val = remainder
			cursor = cursor.Next
		}
		l1 = l1.Next
		l2 = l2.Next
	}

	return head.Next
}

func print_linked_list(l *ListNode) {
	for l != nil {
		fmt.Print(l.val)
		l = l.Next
	}
	fmt.Println()
}

func main() {
	l1 := ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, nil}}}}
	l2 := ListNode{1, &ListNode{2, &ListNode{3, nil}}}
	h := addTwoNumbers(&l1, &l2)
	print_linked_list(h)
}
