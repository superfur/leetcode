func solveSudoku(board [][]byte) {
    // 数独求解器：使用回溯 + 位掩码算法
    // - 用三个位掩码数组记录每行/列/宫已使用的数字
    // - 空格按候选数最少优先排序，减少回溯分支
    // - 逐格尝试可用数字，递归求解；失败则回溯
    const N = 9
    const FULL_MASK uint16 = (1 << 9) - 1 // 0b1_1111_1111
    
    var rowMasks [N]uint16  // 第i行已使用数字的位掩码
    var colMasks [N]uint16  // 第j列已使用数字的位掩码
    var boxMasks [N]uint16  // 第k宫已使用数字的位掩码
    empties := make([][2]int, 0, 81) // 所有空格的位置坐标
    
    // 计算位置(r,c)所属的宫格索引
    getBoxIndex := func(r, c int) int {
        return (r/3)*3 + (c/3)
    }
    
    // 预处理：统计已填数字到掩码中，收集空格
    for r := 0; r < N; r++ {
        for c := 0; c < N; c++ {
            ch := board[r][c]
            if ch == '.' {
                empties = append(empties, [2]int{r, c})
                continue
            }
            
            // 将字节'1'-'9'转换为位索引0-8
            digit := int(ch - '1')
            bit := uint16(1 << digit)
            rowMasks[r] |= bit
            colMasks[c] |= bit
            boxMasks[getBoxIndex(r, c)] |= bit
        }
    }
    
    // Kernighan算法：统计二进制中1的个数
    countBits := func(x uint16) int {
        count := 0
        for x != 0 {
            x &= (x - 1) // 清除最低位的1
            count++
        }
        return count
    }
    
    // 计算位置(r,c)的候选数字个数
    getCandidateCount := func(r, c int) int {
        used := rowMasks[r] | colMasks[c] | boxMasks[getBoxIndex(r, c)]
        available := FULL_MASK & ^used
        return countBits(available)
    }
    
    // 启发式排序：空格按候选数升序排序
    sort.Slice(empties, func(i, j int) bool {
        countI := getCandidateCount(empties[i][0], empties[i][1])
        countJ := getCandidateCount(empties[j][0], empties[j][1])
        return countI < countJ
    })
    
    // 深度优先搜索回溯求解
    var dfs func(idx int) bool
    dfs = func(idx int) bool {
        // 所有空格填完，找到解
        if idx == len(empties) {
            return true
        }
        
        r := empties[idx][0]
        c := empties[idx][1]
        boxIdx := getBoxIndex(r, c)
        
        // 计算当前位置的可用数字位集合
        used := rowMasks[r] | colMasks[c] | boxMasks[boxIdx]
        available := FULL_MASK & ^used // 可用数字的位掩码
        
        // 尝试每个可用数字
        for available != 0 {
            // 取最低位的1（选择一个候选数字）
            bit := available & (^available + 1) // 获取最低位1
            
            // 获取位索引（使用bits包的TrailingZeros16更高效）
            digit := 0
            temp := bit
            for temp > 1 {
                temp >>= 1
                digit++
            }
            
            ch := byte('1' + digit) // 转换为字符'1'-'9'
            
            // 放置该数字
            board[r][c] = ch
            rowMasks[r] |= bit
            colMasks[c] |= bit
            boxMasks[boxIdx] |= bit
            
            // 递归求解下一个空格
            if dfs(idx + 1) {
                return true
            }
            
            // 回溯：撤销放置
            board[r][c] = '.'
            rowMasks[r] &= ^bit
            colMasks[c] &= ^bit
            boxMasks[boxIdx] &= ^bit
            
            // 移除当前候选，尝试下一个
            available &= (available - 1)
        }
        
        // 所有候选都失败，回溯到上一层
        return false
    }
    
    // 开始求解
    dfs(0)
}