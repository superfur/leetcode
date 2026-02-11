def getPermutation(*args, **kwargs):
    """
    排列序列
    """
    # 支持传入 (n, k) 或关键字参数 n,k
    if len(args) >= 2 and isinstance(args[0], int) and isinstance(args[1], int):
        n, k = args[0], args[1]
    elif 'n' in kwargs and 'k' in kwargs:
        n, k = kwargs['n'], kwargs['k']
    else:
        raise TypeError('expected (n, k)')

    if n <= 0 or k <= 0:
        return ""

    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i
    if k > fact[n]:
        return ""

    nums = [str(i) for i in range(1, n + 1)]
    k -= 1  # 转为 0-index
    res = []
    for i in range(n, 0, -1):
        f = fact[i - 1]
        idx = k // f
        res.append(nums.pop(idx))
        k %= f

    return ''.join(res)


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return getPermutation(n, k)
