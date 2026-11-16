/**
 * 150. 逆波兰表达式求值
 * 用栈从左到右扫描：遇到数字就入栈；遇到运算符就弹出两个操作数计算，再把结果压回栈。
 * 注意弹出的顺序：先弹出的是右操作数 b，后弹出的是左操作数 a，结果是 a op b（减法、除法顺序不能反）。
 * 除法要向零截断：用 Math.trunc 而不是 Math.floor（负数结果会差 1）。
 * 题目保证中间结果都在 32 位整数范围内，double 除法后再截断不会丢精度。
 * 时间 O(n)，空间 O(n)。
 */
function evalRPN(tokens: string[]): number {
    const stack: number[] = [];
    for (const token of tokens) {
        switch (token) {
            case "+":
            case "-":
            case "*":
            case "/": {
                const b = stack.pop()!;
                const a = stack.pop()!;
                if (token === "+") stack.push(a + b);
                else if (token === "-") stack.push(a - b);
                else if (token === "*") stack.push(a * b);
                else stack.push(Math.trunc(a / b));
                break;
            }
            default:
                stack.push(parseInt(token, 10));
        }
    }
    return stack[0];
}

export default evalRPN;
