from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        93. 复原 IP 地址
        回溯：依次切出长度 1~3 的一段作为一个 IP 段，
        段值需在 0~255 之间且不能有前导 0（除了单独的 "0"）；
        切出 4 段且恰好用完所有字符时才是一个合法答案。
        """
        n = len(s)
        result: List[str] = []

        def backtrack(start: int, segments: List[str]) -> None:
            if len(segments) == 4:
                if start == n:
                    result.append(".".join(segments))
                return
            if n - start > (4 - len(segments)) * 3:
                return
            for length in range(1, 4):
                if start + length > n:
                    break
                segment = s[start:start + length]
                if length > 1 and segment[0] == "0":
                    break
                if int(segment) > 255:
                    break
                segments.append(segment)
                backtrack(start + length, segments)
                segments.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    test_cases = [
        ("25525511135", ["255.255.11.135", "255.255.111.35"]),
        ("0000", ["0.0.0.0"]),
        ("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
    ]
    solution = Solution()
    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.restoreIpAddresses(s)
        status = "PASS" if sorted(result) == sorted(expected) else "FAIL"
        print(f"测试用例 {i}: {status} (s={s!r}, got={result})")
