package main

// 125. 验证回文串
// 双指针：左右两端向中间走，跳过非字母数字字符，
// 其余字符忽略大小写后逐个比较，不一致就不是回文。
func isPalindrome(s string) bool {
	isAlnum := func(c byte) bool {
		return (c >= '0' && c <= '9') || (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')
	}
	lower := func(c byte) byte {
		if c >= 'A' && c <= 'Z' {
			return c + 32
		}
		return c
	}

	left, right := 0, len(s)-1
	for left < right {
		for left < right && !isAlnum(s[left]) {
			left++
		}
		for left < right && !isAlnum(s[right]) {
			right--
		}
		if lower(s[left]) != lower(s[right]) {
			return false
		}
		left++
		right--
	}
	return true
}
