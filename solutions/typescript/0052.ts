function totalNQueens(n: number): number {
  // 位运算回溯：用三个 bitmask 分别记录 列 / 主对角线 / 副对角线 是否已被占用
  let count = 0;

  /**
   * row: 当前要放置皇后的行号
   * cols: 已被占用的列集合（第 j 列占用，则第 j 位为 1）
   * diag1: 主对角线集合（row - col 固定，用 (row - col + n - 1) 映射到 [0, 2n-2]）
   * diag2: 副对角线集合（row + col 固定，直接用 row + col 映射到 [0, 2n-2]）
   */
  function backtrack(row: number, cols: number, diag1: number, diag2: number): void {
    if (row === n) {
      count++;
      return;
    }

    for (let col = 0; col < n; col++) {
      const d1 = row - col + n - 1;
      const d2 = row + col;

      const colBit = 1 << col;
      const d1Bit = 1 << d1;
      const d2Bit = 1 << d2;

      if ((cols & colBit) !== 0) continue;
      if ((diag1 & d1Bit) !== 0) continue;
      if ((diag2 & d2Bit) !== 0) continue;

      backtrack(
        row + 1,
        cols | colBit,
        diag1 | d1Bit,
        diag2 | d2Bit,
      );
    }
  }

  backtrack(0, 0, 0, 0);
  return count;
}