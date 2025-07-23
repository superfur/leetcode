func isValid(s string) bool {
    stack := []rune{}
    for _, char := range s {
        if char == '(' || char == '{' || char == '[' {
            stack = append(stack, char)
        } else if char == ')' || char == '}' || char == ']' {
            if len(stack) == 0 {
                return false
            }
            top := stack[len(stack)-1]
            if (char == ')' && top != '(') || (char == '}' && top != '{') || (char == ']' && top != '[') {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}