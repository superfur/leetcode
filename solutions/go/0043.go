func multiply(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}

	m := len(num1)
	n := len(num2)
	result := make([]int, m+n)

	for i := m - 1; i >= 0; i-- {
		digit1 := int(num1[i] - '0')
		for j := n - 1; j >= 0; j-- {
			digit2 := int(num2[j] - '0')
			mul := digit1 * digit2

			p1 := i + j
			p2 := i + j + 1
			sum := mul + result[p2]

			result[p2] = sum % 10
			result[p1] += sum / 10
		}
	}

	resBytes := make([]byte, 0, len(result))
	leadingZero := true
	for _, val := range result {
		if leadingZero && val == 0 {
			continue
		}
		leadingZero = false
		resBytes = append(resBytes, byte(val)+'0')
	}

	if len(resBytes) == 0 {
		return "0"
	}

	return string(resBytes)
}