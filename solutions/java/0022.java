class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> parens = new ArrayList<>();
        generate("", n, n, parens);
        return parens;
    }

    private void generate(String p, int left, int right, List<String> parens) {
        if (left > 0) generate(p + "(", left - 1, right, parens);
        if (right > left) generate(p + ")", left, right - 1, parens);
        if (right == 0) parens.add(p);
    }
}