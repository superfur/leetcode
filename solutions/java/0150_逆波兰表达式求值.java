class Solution {
    /**
     * 150. 逆波兰表达式求值
     * 用栈从左到右扫描：遇到数字就入栈；遇到运算符就弹出两个操作数计算，再把结果压回栈。
     * 注意弹出的顺序：先弹出的是右操作数 b，后弹出的是左操作数 a，结果是 a op b（减法、除法顺序不能反）。
     * Java 的整数除法本来就是向零截断，直接用 / 即可。
     * 用 int 数组当栈，避免 Integer 装箱。时间 O(n)，空间 O(n)。
     */
    public int evalRPN(String[] tokens) {
        int[] stack = new int[tokens.length];
        int top = 0;
        for (String token : tokens) {
            switch (token) {
                case "+":
                    top--;
                    stack[top - 1] += stack[top];
                    break;
                case "-":
                    top--;
                    stack[top - 1] -= stack[top];
                    break;
                case "*":
                    top--;
                    stack[top - 1] *= stack[top];
                    break;
                case "/":
                    top--;
                    stack[top - 1] /= stack[top];
                    break;
                default:
                    stack[top++] = Integer.parseInt(token);
            }
        }
        return stack[0];
    }
}
