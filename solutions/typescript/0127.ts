/**
 * 127. 单词接龙
 * BFS：从 beginWord 出发，每次把某一位换成 a~z，命中字典的单词就入队，
 * 并立刻从字典里删掉（等价于标记已访问）。
 * 第一次碰到 endWord 时的步数（按单词个数计，起点算 1）就是答案。
 */
function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
    const words = new Set<string>(wordList);
    if (!words.has(endWord)) return 0;

    words.delete(beginWord);
    let level: string[] = [beginWord];
    let steps = 1;

    while (level.length > 0) {
        const next: string[] = [];
        for (const word of level) {
            for (let i = 0; i < word.length; i++) {
                for (let code = 97; code <= 122; code++) {
                    const c = String.fromCharCode(code);
                    if (c === word[i]) continue;
                    const nw = word.slice(0, i) + c + word.slice(i + 1);
                    if (words.has(nw)) {
                        if (nw === endWord) return steps + 1;
                        words.delete(nw);
                        next.push(nw);
                    }
                }
            }
        }
        level = next;
        steps++;
    }
    return 0;
}

export default ladderLength;
