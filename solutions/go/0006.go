package main

// convert 将字符串按照 Z 字形排列后按行读取
// 参数:
//   - s: 输入字符串
//   - numRows: Z 字形的行数
// 返回:
//   - 按行读取后的字符串
func convert(s string, numRows int) string {
	// 如果只有一行，直接返回原字符串
	if numRows == 1 {
		return s
	}

	// 创建存储每行字符的切片
	rows := make([]string, numRows)
	curRow := 0
	goingDown := false

	// 遍历字符串中的每个字符
	for _, char := range s {
		// 将字符添加到当前行
		rows[curRow] += string(char)

		// 在到达顶部或底部时改变方向
		if curRow == 0 || curRow == numRows-1 {
			goingDown = !goingDown
		}

		// 根据方向更新当前行
		if goingDown {
			curRow++
		} else {
			curRow--
		}
	}

	// 将所有行连接起来
	result := ""
	for _, row := range rows {
		result += row
	}

	return result
}

