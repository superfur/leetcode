function findSubstring(s: string, words: string[]): number[] {
    if (!s || !words || words.length === 0) {
        return [];
    }
    
    const wordLen = words[0].length;
    const totalLen = words.length * wordLen;
    const result: number[] = [];
    
    // 创建words的计数映射
    const wordCount = new Map<string, number>();
    for (const word of words) {
        wordCount.set(word, (wordCount.get(word) || 0) + 1);
    }
    
    // 遍历所有可能的起始位置
    for (let i = 0; i <= s.length - totalLen; i++) {
        const currentCount = new Map<string, number>();
        let matched = 0;
        
        // 检查从位置i开始的子串
        for (let j = 0; j < words.length; j++) {
            const start = i + j * wordLen;
            const word = s.substring(start, start + wordLen);
            
            // 如果这个单词不在words中，直接跳出
            if (!wordCount.has(word)) {
                break;
            }
            
            // 更新当前计数
            currentCount.set(word, (currentCount.get(word) || 0) + 1);
            
            // 如果当前单词出现次数超过words中的次数，跳出
            if (currentCount.get(word)! > wordCount.get(word)!) {
                break;
            }
            
            matched++;
        }
        
        // 如果所有单词都匹配了，记录起始位置
        if (matched === words.length) {
            result.push(i);
        }
    }
    
    return result;
};