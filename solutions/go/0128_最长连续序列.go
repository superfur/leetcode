package main

// 128. 最长连续序列
// 哈希集合去重，只从「序列起点」（x - 1 不在集合里）出发往后数 x+1, x+2, ...，
// 每个数最多被数一次，所以整体 O(n)。
func longestConsecutive(nums []int) int {
	set := make(map[int]bool, len(nums))
	for _, x := range nums {
		set[x] = true
	}

	best := 0
	for x := range set {
		if set[x-1] {
			continue
		}
		end := x
		for set[end+1] {
			end++
		}
		if end-x+1 > best {
			best = end - x + 1
		}
	}
	return best
}
