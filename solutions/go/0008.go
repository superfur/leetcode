// public class Solution {
//     public int myAtoi(String s) {
//         int MAX_INT = Integer.MAX_VALUE;
//         int MIN_INT = Integer.MIN_VALUE;
//         s = s.trim();
//         if (s.isEmpty()) return 0;
//         int sign = 1;
//         int i = 0;
//         if (s.charAt(i) == '+' || s.charAt(i) == '-') {
//             sign = s.charAt(i) == '-' ? -1 : 1;
//             i++;
//         }
//         long result = 0;  // 使用long来避免中间计算溢出
//         while (i < s.length() && Character.isDigit(s.charAt(i))) {
//             result = result * 10 + (s.charAt(i) - '0');
//             if (sign == 1 && result > MAX_INT) {
//                 return MAX_INT;
//             }
//             if (sign == -1 && result > -(long)MIN_INT) {
//                 return MIN_INT;
//             }
//             i++;
//         }
//         return (int)(result * sign);
//     }
// }

package main

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