def is_number(s: str) -> bool:
    s = s.strip()
    if not s:
        return False
    seen_digit = False
    seen_dot = False
    seen_exponent = False
    for i, ch in enumerate(s):
        if ch in "+-":
            if i > 0 and s[i - 1] not in "eE":
                return False
        elif ch == ".":
            if seen_dot or seen_exponent:
                return False
            seen_dot = True
        elif ch in "eE":
            if seen_exponent or not seen_digit:
                return False
            seen_exponent = True
            seen_digit = False
        elif ch.isdigit():
            seen_digit = True
        else:
            return False
    return seen_digit


class Solution:
    def isNumber(self, s: str) -> bool:
        return is_number(s)


if __name__ == "__main__":
    test_cases = [
        ("0", True),
        ("e", False),
        (".", False),
        ("0089", True),
        ("-0.1", True),
        ("+3.14", True),
        ("4.", True),
        ("-.9", True),
        ("2e10", True),
        ("-90E3", True),
        ("3e+7", True),
        ("abc", False),
        ("1e", False),
        ("e3", False),
        ("99e2.5", False),
        ("--6", False),
        (".e1", False),
        ("1e.", False),
    ]
    for i, (inp, expected) in enumerate(test_cases, 1):
        got = is_number(inp)
        status = "通过" if got == expected else "失败"
        print(f"测试用例 {i}: {status} (input={inp!r}, 期望={expected}, 实际={got})")
