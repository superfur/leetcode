impl Solution {
    /// 150. 逆波兰表达式求值
    /// 用栈从左到右扫描：遇到数字就入栈；遇到运算符就弹出两个操作数计算，再把结果压回栈。
    /// 注意弹出的顺序：先弹出的是右操作数 b，后弹出的是左操作数 a，结果是 a op b（减法、除法顺序不能反）。
    /// Rust 的整数除法本来就是向零截断，直接用 / 即可。
    /// 时间 O(n)，空间 O(n)。
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = Vec::with_capacity(tokens.len());
        for token in &tokens {
            match token.as_str() {
                op @ ("+" | "-" | "*" | "/") => {
                    let b = stack.pop().unwrap();
                    let a = stack.pop().unwrap();
                    stack.push(match op {
                        "+" => a + b,
                        "-" => a - b,
                        "*" => a * b,
                        _ => a / b,
                    });
                }
                num => stack.push(num.parse().unwrap()),
            }
        }
        stack[0]
    }
}
