func generateParenthesis(n int) []string {
    parens := []string{}
    generate("", n, n, &parens)
    return parens
}

func generate(p string, left, right int, parens *[]string) {
    if left > 0 {
        generate(p + "(", left - 1, right, parens)
    }
    if right > left {
        generate(p + ")", left, right - 1, parens)
    }
    if right == 0 {
        *parens = append(*parens, p)
    }
}