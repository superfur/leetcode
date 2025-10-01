function isValidSudoku(board: string[][]): boolean {
    // 使用三个Set来分别记录行、列、宫格中数字的出现情况
    const rows = new Set<string>();
    const cols = new Set<string>();
    const boxes = new Set<string>();
    
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const num = board[i][j];
            
            // 跳过空白格
            if (num === '.') continue;
            
            // 创建唯一标识符
            const rowKey = `${i}-${num}`;
            const colKey = `${j}-${num}`;
            const boxKey = `${Math.floor(i / 3)}-${Math.floor(j / 3)}-${num}`;
            
            // 检查是否已经存在
            if (rows.has(rowKey) || cols.has(colKey) || boxes.has(boxKey)) {
                return false;
            }
            
            // 添加到对应的Set中
            rows.add(rowKey);
            cols.add(colKey);
            boxes.add(boxKey);
        }
    }
    
    return true;
};