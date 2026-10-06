package main

// 126. 单词接龙 II
// BFS 逐层扩展，记录每个单词在最短路径上的所有前驱（只记录首次被发现的那一层），
// 第一次碰到 endWord 就停；然后从 endWord 沿前驱表回溯到 beginWord，还原所有最短路径。
func findLadders(beginWord string, endWord string, wordList []string) [][]string {
	words := make(map[string]bool, len(wordList))
	for _, w := range wordList {
		words[w] = true
	}
	if !words[endWord] {
		return [][]string{}
	}

	parents := map[string][]string{}
	visited := map[string]bool{beginWord: true}
	level := []string{beginWord}
	found := false

	for len(level) > 0 && !found {
		nextSet := map[string]bool{}
		next := []string{}
		for _, w := range level {
			b := []byte(w)
			for i := range b {
				orig := b[i]
				for c := byte('a'); c <= 'z'; c++ {
					if c == orig {
						continue
					}
					b[i] = c
					nw := string(b)
					if words[nw] && !visited[nw] {
						parents[nw] = append(parents[nw], w)
						if !nextSet[nw] {
							nextSet[nw] = true
							next = append(next, nw)
						}
						if nw == endWord {
							found = true
						}
					}
				}
				b[i] = orig
			}
		}
		for _, w := range next {
			visited[w] = true
		}
		level = next
	}

	if !found {
		return [][]string{}
	}

	res := [][]string{}
	path := []string{endWord}

	var back func(w string)
	back = func(w string) {
		if w == beginWord {
			cp := make([]string, len(path))
			for i, x := range path {
				cp[len(path)-1-i] = x
			}
			res = append(res, cp)
			return
		}
		for _, p := range parents[w] {
			path = append(path, p)
			back(p)
			path = path[:len(path)-1]
		}
	}

	back(endWord)
	return res
}
