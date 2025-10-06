function solveSudoku(board: string[][]): void {
  const N = 9;
  const FULL_MASK = (1 << 9) - 1; // 0b1_1111_1111 for digits 1..9

  const rowMasks: number[] = new Array(N).fill(0);
  const colMasks: number[] = new Array(N).fill(0);
  const boxMasks: number[] = new Array(N).fill(0);
  const empties: Array<[number, number]> = [];

  const getBoxIndex = (r: number, c: number): number => ((Math.floor(r / 3) * 3) + Math.floor(c / 3));

  // Initialize masks and collect empty cells
  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      const ch = board[r][c];
      if (ch === '.') {
        empties.push([r, c]);
        continue;
      }
      const digit = ch.charCodeAt(0) - '1'.charCodeAt(0); // 0..8
      const bit = 1 << digit;
      rowMasks[r] |= bit;
      colMasks[c] |= bit;
      boxMasks[getBoxIndex(r, c)] |= bit;
    }
  }

  // Choose-next heuristic: sort empties by least available candidates (optional but speeds up)
  empties.sort((a, b) => {
    const [ra, ca] = a;
    const [rb, cb] = b;
    const maskA = rowMasks[ra] | colMasks[ca] | boxMasks[getBoxIndex(ra, ca)];
    const maskB = rowMasks[rb] | colMasks[cb] | boxMasks[getBoxIndex(rb, cb)];
    const availA = FULL_MASK & ~maskA;
    const availB = FULL_MASK & ~maskB;
    // Count bits (number of candidates)
    const countA = countBits(availA);
    const countB = countBits(availB);
    return countA - countB;
  });

  function countBits(x: number): number {
    // Kernighan's algorithm
    let cnt = 0;
    while (x !== 0) {
      x &= (x - 1);
      cnt++;
    }
    return cnt;
  }

  function dfs(idx: number): boolean {
    if (idx === empties.length) return true;

    const [r, c] = empties[idx];
    const used = rowMasks[r] | colMasks[c] | boxMasks[getBoxIndex(r, c)];
    let avail = FULL_MASK & ~used; // bits for digits that can be used

    while (avail !== 0) {
      const bit = avail & -avail; // lowest set bit
      const digit = Math.log2(bit) | 0; // 0..8
      const ch = String.fromCharCode('1'.charCodeAt(0) + digit);

      // place
      board[r][c] = ch;
      rowMasks[r] |= bit;
      colMasks[c] |= bit;
      const boxIdx = getBoxIndex(r, c);
      boxMasks[boxIdx] |= bit;

      if (dfs(idx + 1)) return true;

      // backtrack
      board[r][c] = '.';
      rowMasks[r] &= ~bit;
      colMasks[c] &= ~bit;
      boxMasks[boxIdx] &= ~bit;

      // try next candidate
      avail &= (avail - 1);
    }

    return false;
  }

  dfs(0);
}