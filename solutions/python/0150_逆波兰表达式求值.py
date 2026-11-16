import random
from typing import List, Optional, Tuple, Union


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        150. 逆波兰表达式求值
        用栈从左到右扫描：遇到数字就入栈；遇到运算符就弹出两个操作数计算，再把结果压回栈。
        注意弹出的顺序：先弹出的是右操作数 b，后弹出的是左操作数 a，结果是 a op b（减法、除法顺序不能反）。
        除法要向零截断：Python 的 `//` 是向下取整，负数会差 1，
        所以对绝对值做整除，再按两数符号决定结果的正负，全程不用浮点。
        时间 O(n)，空间 O(n)。
        """
        stack: List[int] = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    q = abs(a) // abs(b)
                    stack.append(q if (a < 0) == (b < 0) else -q)
            else:
                stack.append(int(token))
        return stack[0]


# ---------- 对拍用：随机生成表达式树，递归求值，同时输出它的逆波兰式 ----------
Tree = Union[int, Tuple[str, "Tree", "Tree"]]


def random_tree(depth: int) -> Tree:
    if depth == 0 or random.random() < 0.25:
        return random.randint(-200, 200)
    return (random.choice("+-*/"), random_tree(depth - 1), random_tree(depth - 1))


def eval_tree(tree: Tree) -> Optional[int]:
    """递归求值；出现除零或中间结果超出 32 位则返回 None（该样例作废）。"""
    if isinstance(tree, int):
        return tree
    op, left, right = tree
    a, b = eval_tree(left), eval_tree(right)
    if a is None or b is None:
        return None
    if op == "+":
        r = a + b
    elif op == "-":
        r = a - b
    elif op == "*":
        r = a * b
    else:
        if b == 0:
            return None
        r = int(a / b)  # 数值不大（|a| <= 2^31），float 除法再截断和向零截断等价
    return r if -(2 ** 31) <= r < 2 ** 31 else None


def to_rpn(tree: Tree) -> List[str]:
    if isinstance(tree, int):
        return [str(tree)]
    op, left, right = tree
    return to_rpn(left) + to_rpn(right) + [op]


if __name__ == "__main__":
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        (["18"], 18),
        (["-7"], -7),
        (["7", "-3", "/"], -2),   # 向零截断：-2.33 -> -2，而不是 -3
        (["-7", "3", "/"], -2),
        (["-7", "-3", "/"], 2),
        (["1", "2", "/"], 0),
        (["-1", "2", "/"], 0),    # 结果为 -0.5 -> 0，不能出现 -1
        (["3", "4", "-"], -1),    # 操作数顺序：3 - 4
        (["100", "7", "-"], 93),
    ]
    solution = Solution()
    for i, (tokens, expected) in enumerate(test_cases, 1):
        result = solution.evalRPN(tokens)
        status = "PASS" if result == expected else "FAIL"
        print(f"测试用例 {i}: {status} (tokens={tokens}, got={result}, expected={expected})")

    # 规模：10^4 个 token，先压 5001 个 1，再接 5000 个 "+"
    big = ["1"] * 5001 + ["+"] * 5000
    print(f"测试用例 {len(test_cases) + 1}: {'PASS' if solution.evalRPN(big) == 5001 else 'FAIL'} (10^4 个 token)")

    random.seed(150)
    mismatches, checked = 0, 0
    while checked < 2000:
        tree = random_tree(random.randint(1, 7))
        expected = eval_tree(tree)
        if expected is None:
            continue
        checked += 1
        if solution.evalRPN(to_rpn(tree)) != expected:
            mismatches += 1
    print(f"测试用例 {len(test_cases) + 2}: {'PASS' if mismatches == 0 else 'FAIL'} (2000 个随机表达式树与递归求值对拍，不一致 {mismatches} 个)")
