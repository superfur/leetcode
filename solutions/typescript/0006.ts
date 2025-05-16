function convert(s: string, numRows: number): string {
    if (numRows === 1) return s;
    const rows = Array.from({length: numRows}, () => "");
    let curRow = 0;
    let goingDown = false;
    for (const char of s) {
        rows[curRow] += char;
        if (curRow === 0 || curRow === numRows - 1) {
            goingDown = !goingDown;
        }
        curRow += goingDown ? 1 : -1;
    }
    return rows.join("");
};