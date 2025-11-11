function isMatch(s: string, p: string): boolean {
    let i = 0;
    let j = 0;
    let starIdx = -1;
    let match = 0;
    
    const sLen = s.length;
    const pLen = p.length;

    while (i < sLen) {
        if (j < pLen && (p[j] === s[i] || p[j] === '?')) {
            i++;
            j++;
        } else if (j < pLen && p[j] === '*') {
            starIdx = j;
            match = i;
            j++;
        } else if (starIdx !== -1) {
            j = starIdx + 1;
            match++;
            i = match;
        } else {
            return false;
        }
    }

    while (j < pLen && p[j] === '*') {
        j++;
    }

    return j === pLen;
};