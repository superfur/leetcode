function letterCombinations(digits: string): string[] {
    if (!digits) return [];

    const map = new Map<string, string[]>([
        ['2', ['a', 'b', 'c']],
        ['3', ['d', 'e', 'f']],
        ['4', ['g', 'h', 'i']],
        ['5', ['j', 'k', 'l']],
        ['6', ['m', 'n', 'o']],
        ['7', ['p', 'q', 'r', 's']],
        ['8', ['t', 'u', 'v']],
        ['9', ['w', 'x', 'y', 'z']],
    ]);

    const result: string[] = [];
    const combination: string[] = [];

    const backtrack = (index: number) => {
        if (index === digits.length) {
            result.push(combination.join(''));
            return;
        }

        const letters = map.get(digits[index]);
        if (!letters) return;

        for (const letter of letters) {
            combination.push(letter);
            backtrack(index + 1);
            combination.pop();
        }
    };

    backtrack(0);
    return result;
};