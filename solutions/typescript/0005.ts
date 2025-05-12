function longestPalindrome(s: string): string {
    if (s.length <= 1) return s;
    let maxLen = 1;
    let begin = 0;
    const dp = Array.from({length: s.length}, () => new Array(s.length).fill(false));
    for (let i = 0; i < s.length; i++) {
        dp[i][i] = true;
    }
    for (let j = 1; j < s.length; j++) {
        for (let i = 0; i < j; i++) {
            if (s[i] !== s[j]) {
                dp[i][j] = false;
            } else {
                if (j - i < 3) {
                    dp[i][j] = true;
                } else {
                    dp[i][j] = dp[i + 1][j - 1];
                }
                if (dp[i][j] && j - i + 1 > maxLen) {
                    maxLen = j - i + 1;
                    begin = i;
                }
            }
        }
    }
    return s.slice(begin, begin + maxLen);
};