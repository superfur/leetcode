func myAtoi(s string) int {
	MAX_INT := 1<<31 - 1
	MIN_INT := -1 << 31
	s = strings.TrimSpace(s)
	if s == "" {
		return 0
	}
	sign := 1
	if s[0] == '-' {
		sign = -1
		s = s[1:]
	} else if s[0] == '+' {
		s = s[1:]
	}
	result := 0
	for _, char := range s {
		if !unicode.IsDigit(char) {
			break
		}
		digit := int(char - '0')
		if sign == 1 && (result > MAX_INT/10 || (result == MAX_INT/10 && digit > MAX_INT%10)) {
			return MAX_INT
		}
		if sign == -1 && (result > -(MIN_INT/10) || (result == -(MIN_INT/10) && digit > -(MIN_INT%10))) {
			return MIN_INT
		}
		result = result*10 + digit
	}
	return result * sign
}