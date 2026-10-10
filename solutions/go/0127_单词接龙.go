package main

// 127. 单词接龙
// BFS：从 beginWord 出发，每次把某一位换成 a~z，命中字典的单词就入队，
// 并立刻从字典里删掉（等价于标记已访问）。
// 第一次碰到 endWord 时的步数（按单词个数计，起点算 1）就是答案。
func ladderLength(beginWord string, endWord string, wordList []string) int {
	words := make(map[string]bool, len(wordList))
	for _, w := range wordList {
		words[w] = true
	}
	if !words[endWord] {
		return 0
	}

	delete(words, beginWord)
	level := []string{beginWord}
	steps := 1

	for len(level) > 0 {
		next := []string{}
		for _, word := range level {
			b := []byte(word)
			for i := range b {
				orig := b[i]
				for c := byte('a'); c <= 'z'; c++ {
					if c == orig {
						continue
					}
					b[i] = c
					nw := string(b)
					if words[nw] {
						if nw == endWord {
							return steps + 1
						}
						delete(words, nw)
						next = append(next, nw)
					}
				}
				b[i] = orig
			}
		}
		level = next
		steps++
	}
	return 0
}
