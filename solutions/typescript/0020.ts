function isValid(s: string): boolean {
    const stack: string[] = [];
    const map: { [key: string]: string } = {
        '(': ')',
        '{': '}',
        '[': ']'
    };
    for (const char of s) {
        if (map[char]) {
            stack.push(char);
        } else if (stack.length > 0 && map[stack[stack.length - 1]] === char) {
            stack.pop();
        } else {
            return false;
        }
    }
    return stack.length === 0;
}