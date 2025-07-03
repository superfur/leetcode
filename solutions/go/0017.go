package main

import (
    "strings"
)

func letterCombinations(digits string) []string {
    if digits == "" {
        return []string{}
    }

    digitMap := map[byte]string{
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
    }

    var result []string
    var combination []string

    var backtrack func(index int)
    backtrack = func(index int) {
        if index == len(digits) {
            result = append(result, strings.Join(combination, ""))
            return
        }

        letters := digitMap[digits[index]]
        for i := 0; i < len(letters); i++ {
            combination = append(combination, string(letters[i]))
            backtrack(index + 1)
            combination = combination[:len(combination)-1]
        }
    }

    backtrack(0)
    return result
}