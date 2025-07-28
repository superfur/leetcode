function generateParenthesis(n: number): string[] {
    const result: string[] = [];
    const generate = (left: number, right: number, current: string) => {
        if (current.length === 2 * n) {
            result.push(current);
            return;
        }
        if (left < n) {
            generate(left + 1, right, current + '(');
        }
        if (right < left) {
            generate(left, right + 1, current + ')');
        }
    };
    generate(0, 0, '');
    return result;
};