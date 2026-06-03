package main

import (
	"fmt"
	"strings"
)

func fullJustify(words []string, maxWidth int) []string {
	var result []string
	i := 0

	for i < len(words) {
		lineLen := len(words[i])
		j := i + 1
		for j < len(words) && lineLen+1+len(words[j]) <= maxWidth {
			lineLen += 1 + len(words[j])
			j++
		}

		lineWords := words[i:j]
		totalChars := 0
		for _, w := range lineWords {
			totalChars += len(w)
		}
		gaps := len(lineWords) - 1
		isLastLine := j == len(words)

		if gaps == 0 || isLastLine {
			line := strings.Join(lineWords, " ")
			line += strings.Repeat(" ", maxWidth-len(line))
			result = append(result, line)
		} else {
			totalSpaces := maxWidth - totalChars
			spacePerGap := totalSpaces / gaps
			extraSpaces := totalSpaces % gaps
			var line strings.Builder
			for k := 0; k < len(lineWords); k++ {
				line.WriteString(lineWords[k])
				if k < gaps {
					spaces := spacePerGap
					if extraSpaces > 0 {
						spaces++
						extraSpaces--
					}
					line.WriteString(strings.Repeat(" ", spaces))
				}
			}
			result = append(result, line.String())
		}

		i = j
	}

	return result
}

func main() {
	words1 := []string{"This", "is", "an", "example", "of", "text", "justification."}
	result1 := fullJustify(words1, 16)
	for _, line := range result1 {
		fmt.Printf("\"%s\"\n", line)
	}

	words2 := []string{"What", "must", "be", "acknowledgment", "shall", "be"}
	result2 := fullJustify(words2, 16)
	for _, line := range result2 {
		fmt.Printf("\"%s\"\n", line)
	}

	words3 := []string{"Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"}
	result3 := fullJustify(words3, 20)
	for _, line := range result3 {
		fmt.Printf("\"%s\"\n", line)
	}
}
