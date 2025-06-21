package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
)

func intToRoman(num int) string {
	romanMap := [][]interface{}{
		{1000, "M"},
		{900, "CM"},
		{500, "D"},
		{400, "CD"},
		{100, "C"},
		{90, "XC"},
		{50, "L"},
		{40, "XL"},
		{10, "X"},
		{9, "IX"},
		{5, "V"},
		{4, "IV"},
		{1, "I"},
	}
	result := ""
	remaining := num

	for _, value := range romanMap {
		for remaining >= value[0].(int) {
			result += value[1].(string)
			remaining -= value[0].(int)
		}
	}
	return result
}