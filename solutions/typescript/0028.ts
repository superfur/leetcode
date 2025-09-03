function strStr(haystack: string, needle: string): number {
    if (needle.length === 0) {
        return 0;
    }
    if (haystack.length === 0) {
        return -1;
    }
    const haystackLen = haystack.length;
    const needleLen = needle.length;
    for (let i = 0; i < haystackLen - needleLen + 1; i++) {
        if (haystack[i] === needle[0]) {
            if (haystack.slice(i, i + needleLen) === needle) {
                return i;
            }
        }
    }
    return -1;
};