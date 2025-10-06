function solveSudoku(board: string[][]): void {
  // 9x9 数独，使用回溯 + 位掩码（bitmask）进行求解：
  // - 用三个掩码数组 rowMasks/colMasks/boxMasks 记录每行/列/宫中已使用的数字
  // - 空位按“候选数最少”优先（启发式）排序，降低回溯分支
  // - 每次取最低位 1 作为候选数字，放置 -> 递归 -> 回溯
  const N = 9;
  const FULL_MASK = (1 << 9) - 1; // 9 位 1，对应数字 1..9 的可用位

  const rowMasks: number[] = new Array(N).fill(0); // 第 i 行已使用位
  const colMasks: number[] = new Array(N).fill(0); // 第 j 列已使用位
  const boxMasks: number[] = new Array(N).fill(0); // 第 k 宫已使用位（k = r/3*3 + c/3）
  const empties: Array<[number, number]> = []; // 记录所有空格位置

  const getBoxIndex = (r: number, c: number): number => ((Math.floor(r / 3) * 3) + Math.floor(c / 3));

  // 初始化：统计已填数字到掩码中，并收集空格
  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      const ch = board[r][c];
      if (ch === '.') {
        empties.push([r, c]);
        continue;
      }
      const digit = ch.charCodeAt(0) - '1'.charCodeAt(0); // 将 '1'..'9' 映射到 0..8
      const bit = 1 << digit;
      rowMasks[r] |= bit;
      colMasks[c] |= bit;
      boxMasks[getBoxIndex(r, c)] |= bit;
    }
  }

  // 启发式：空格按候选数（可用位数量）升序排序，减少搜索空间
  empties.sort((a, b) => {
    const [ra, ca] = a;
    const [rb, cb] = b;
    const maskA = rowMasks[ra] | colMasks[ca] | boxMasks[getBoxIndex(ra, ca)];
    const maskB = rowMasks[rb] | colMasks[cb] | boxMasks[getBoxIndex(rb, cb)];
    const availA = FULL_MASK & ~maskA; // 可用位：1 表示该数字可填
    const availB = FULL_MASK & ~maskB;
    const countA = countBits(availA);
    const countB = countBits(availB);
    return countA - countB;
  });

  function countBits(x: number): number {
    // Kernighan 算法：每次清除最低位 1，统计次数
    let cnt = 0;
    while (x !== 0) {
      x &= (x - 1);
      cnt++;
    }
    return cnt;
  }

  function dfs(idx: number): boolean {
    // 若所有空格填完，找到解
    if (idx === empties.length) return true;

    const [r, c] = empties[idx];
    const used = rowMasks[r] | colMasks[c] | boxMasks[getBoxIndex(r, c)]; // 当前格不可用数字集合
    let avail = FULL_MASK & ~used; // 可用数字集合（bit 为 1 表示可用）

    while (avail !== 0) {
      const bit = avail & -avail; // 取最低位 1（选择一个候选）
      const digit = Math.log2(bit) | 0; // 对应数字 0..8
      const ch = String.fromCharCode('1'.charCodeAt(0) + digit);

      // 放置该候选
      board[r][c] = ch;
      rowMasks[r] |= bit;
      colMasks[c] |= bit;
      const boxIdx = getBoxIndex(r, c);
      boxMasks[boxIdx] |= bit;

      // 继续填下一个空格
      if (dfs(idx + 1)) return true;

      // 回溯：撤销放置
      board[r][c] = '.';
      rowMasks[r] &= ~bit;
      colMasks[c] &= ~bit;
      boxMasks[boxIdx] &= ~bit;

      // 去掉该候选，尝试下一个候选
      avail &= (avail - 1);
    }

    // 所有候选均失败，回溯上一层
    return false;
  }

  dfs(0);
}