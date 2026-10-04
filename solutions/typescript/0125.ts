/**
 * 125. 验证回文串
 * 双指针：左右两端向中间走，跳过非字母数字字符，
 * 其余字符忽略大小写后逐个比较，不一致就不是回文。
 */
function isPalindrome(s: string): boolean {
    const isAlnum = (c: string): boolean => /[a-zA-Z0-9]/.test(c);
    let left = 0;
    let right = s.length - 1;
    while (left < right) {
        while (left < right && !isAlnum(s[left])) left++;
        while (left < right && !isAlnum(s[right])) right--;
        if (s[left].toLowerCase() !== s[right].toLowerCase()) return false;
        left++;
        right--;
    }
    return true;
}

export default isPalindrome;
