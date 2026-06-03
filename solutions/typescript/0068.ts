function fullJustify(words: string[], maxWidth: number): string[] {
    const result: string[] = [];
    let i = 0;

    while (i < words.length) {
        let lineLen = words[i].length;
        let j = i + 1;
        while (j < words.length && lineLen + 1 + words[j].length <= maxWidth) {
            lineLen += 1 + words[j].length;
            j++;
        }

        const lineWords = words.slice(i, j);
        const totalChars = lineWords.reduce((sum, w) => sum + w.length, 0);
        const gaps = lineWords.length - 1;
        const isLastLine = j === words.length;

        if (gaps === 0 || isLastLine) {
            let line = lineWords.join(' ');
            line += ' '.repeat(maxWidth - line.length);
            result.push(line);
        } else {
            const totalSpaces = maxWidth - totalChars;
            const spacePerGap = Math.floor(totalSpaces / gaps);
            let extraSpaces = totalSpaces % gaps;
            let line = '';
            for (let k = 0; k < lineWords.length; k++) {
                line += lineWords[k];
                if (k < gaps) {
                    line += ' '.repeat(spacePerGap + (extraSpaces > 0 ? 1 : 0));
                    extraSpaces--;
                }
            }
            result.push(line);
        }

        i = j;
    }

    return result;
}

export default fullJustify;
