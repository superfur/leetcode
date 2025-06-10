function myAtoi(s: string): number {
  const MAX_INT = Math.pow(2, 31) - 1;
  const MIN_INT = -Math.pow(2, 31);

  // 去除前导空格
  s = s.trim();
  if (s.length === 0) return 0;

  let sign = 1;
  let i = 0;

  // 处理正负号
  if (s[i] === "+" || s[i] === "-") {
    sign = s[i] === "-" ? -1 : 1;
    i++;
  }

  let result = 0;

  // 处理数字
  while (i < s.length && /^\d$/.test(s[i])) {
    const digit = parseInt(s[i]);

    // 检查是否溢出
    if (
      result > Math.floor(MAX_INT / 10) ||
      (result === Math.floor(MAX_INT / 10) && digit > MAX_INT % 10)
    ) {
      return sign === 1 ? MAX_INT : MIN_INT;
    }

    result = result * 10 + digit;
    i++;
  }

  return result * sign;
}
