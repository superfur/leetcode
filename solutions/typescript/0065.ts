function isNumber(s: string): boolean {
    const states: Record<string, number>[] = [
        { " ": 0, s: 1, d: 2, ".": 4 },
        { d: 2, ".": 4 },
        { d: 2, ".": 3, e: 6, " ": 9 },
        { d: 5, e: 6, " ": 9 },
        { d: 5 },
        { d: 5, e: 6, " ": 9 },
        { s: 7, d: 8 },
        { d: 8 },
        { d: 8, " ": 9 },
        { " ": 9 },
    ];
    let state = 0;
    for (const ch of s) {
        let t = "";
        if (ch >= "0" && ch <= "9") t = "d";
        else if (ch === "+" || ch === "-") t = "s";
        else if (ch === "e" || ch === "E") t = "e";
        else t = ch;
        if (states[state][t] === undefined) return false;
        state = states[state][t];
    }
    return [2, 3, 5, 8, 9].includes(state);
}

export default isNumber;
