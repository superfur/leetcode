/**
 * 126. 单词接龙 II
 * BFS 逐层扩展，记录每个单词在最短路径上的所有前驱（只记录首次被发现的那一层），
 * 第一次碰到 endWord 就停；然后从 endWord 沿前驱表回溯到 beginWord，还原所有最短路径。
 */
function findLadders(beginWord: string, endWord: string, wordList: string[]): string[][] {
    const words = new Set<string>(wordList);
    if (!words.has(endWord)) return [];

    const parents = new Map<string, string[]>();
    const visited = new Set<string>([beginWord]);
    let level = new Set<string>([beginWord]);
    let found = false;

    while (level.size > 0 && !found) {
        const next = new Set<string>();
        for (const w of level) {
            for (let i = 0; i < w.length; i++) {
                for (let code = 97; code <= 122; code++) {
                    const c = String.fromCharCode(code);
                    if (c === w[i]) continue;
                    const nw = w.slice(0, i) + c + w.slice(i + 1);
                    if (words.has(nw) && !visited.has(nw)) {
                        if (!parents.has(nw)) parents.set(nw, []);
                        parents.get(nw)!.push(w);
                        next.add(nw);
                        if (nw === endWord) found = true;
                    }
                }
            }
        }
        next.forEach(w => visited.add(w));
        level = next;
    }

    if (!found) return [];

    const res: string[][] = [];
    const path: string[] = [endWord];

    const back = (w: string): void => {
        if (w === beginWord) {
            res.push([...path].reverse());
            return;
        }
        for (const p of parents.get(w) ?? []) {
            path.push(p);
            back(p);
            path.pop();
        }
    };

    back(endWord);
    return res;
}

export default findLadders;
