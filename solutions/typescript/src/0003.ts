function lengthOfLongestSubstring(s: string): number {
  const map = new Map<string, number>();
  let maxLength = 0;
  let left = 0;

  for (let right = 0; right < s.length; right++) {
    const char = s[right];
    if (map.has(char)) {
      left = Math.max(map.get(char)! + 1, left);
    }
    map.set(char, right);
    maxLength = Math.max(maxLength, right - left + 1);
  }
  return maxLength;
}

export default lengthOfLongestSubstring;
