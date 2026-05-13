func isNumber(s string) bool {
	s = strings.TrimSpace(s)
	if len(s) == 0 {
		return false
	}
	seenDigit := false
	seenDot := false
	seenExp := false
	for i, ch := range s {
		if ch == '+' || ch == '-' {
			if i > 0 && s[i-1] != 'e' && s[i-1] != 'E' {
				return false
			}
		} else if ch == '.' {
			if seenDot || seenExp {
				return false
			}
			seenDot = true
		} else if ch == 'e' || ch == 'E' {
			if seenExp || !seenDigit {
				return false
			}
			seenExp = true
			seenDigit = false
		} else if unicode.IsDigit(ch) {
			seenDigit = true
		} else {
			return false
		}
	}
	return seenDigit
}
