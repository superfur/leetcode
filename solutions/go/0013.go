func romanToInt(s string) int {
	romanMap := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	
	result := 0
	for i := 0; i < len(s); i++ {
		current := romanMap[s[i]]
		
		// 检查是否有下一个字符
		if i+1 < len(s) {
			next := romanMap[s[i+1]]
			if current < next {
				result -= current
			} else {
				result += current
			}
		} else {
			result += current
		}
	}
	
	return result
}