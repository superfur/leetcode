impl Solution {
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        // 9x9 数独：使用回溯 + 位掩码
        // - row_masks/col_masks/box_masks 记录每行/列/宫已使用数字（bit=1 表示已用）
        // - 收集空格坐标，按候选数最少排序以减少回溯
        // - 逐格尝试可用数字，递归求解；失败则回溯
        const N: usize = 9;
        const FULL_MASK: u16 = (1 << 9) - 1; // 0b1_1111_1111

        let mut row_masks: [u16; N] = [0; N];
        let mut col_masks: [u16; N] = [0; N];
        let mut box_masks: [u16; N] = [0; N];
        let mut empties: Vec<(usize, usize)> = Vec::new();

        let get_box_index = |r: usize, c: usize| -> usize { (r / 3) * 3 + (c / 3) };

        // 初始化掩码与空位列表
        for r in 0..N {
            for c in 0..N {
                let ch = board[r][c];
                if ch == '.' {
                    empties.push((r, c));
                    continue;
                }
                let digit = (ch as u8 - b'1') as u16; // 0..8
                let bit = 1u16 << digit;
                row_masks[r] |= bit;
                col_masks[c] |= bit;
                box_masks[get_box_index(r, c)] |= bit;
            }
        }

        // 计数 1 比特个数（Kernighan）
        fn count_bits(mut x: u16) -> u32 {
            let mut cnt = 0u32;
            while x != 0 {
                x &= x - 1;
                cnt += 1;
            }
            cnt
        }

        // 启发式：空位按候选数升序排序
        empties.sort_by(|&(ra, ca), &(rb, cb)| {
            let mask_a = row_masks[ra] | col_masks[ca] | box_masks[get_box_index(ra, ca)];
            let mask_b = row_masks[rb] | col_masks[cb] | box_masks[get_box_index(rb, cb)];
            let avail_a = FULL_MASK & !mask_a;
            let avail_b = FULL_MASK & !mask_b;
            count_bits(avail_a).cmp(&count_bits(avail_b))
        });

        // DFS 回溯
        fn dfs(
            idx: usize,
            empties: &[(usize, usize)],
            board: &mut [Vec<char>],
            row_masks: &mut [u16; N],
            col_masks: &mut [u16; N],
            box_masks: &mut [u16; N],
        ) -> bool {
            if idx == empties.len() { return true; }

            let (r, c) = empties[idx];
            let box_idx = (r / 3) * 3 + (c / 3);
            let used = row_masks[r] | col_masks[c] | box_masks[box_idx];
            let mut avail = FULL_MASK & !used; // 可用数字位集合

            while avail != 0 {
                // 取最低位 1
                let bit = avail & (!avail + 1); // 等价于 avail & -avail（在无符号下的两补运算）
                let digit = bit.trailing_zeros() as u8; // 0..8
                let ch = (b'1' + digit) as char;

                // 放置
                board[r][c] = ch;
                row_masks[r] |= bit;
                col_masks[c] |= bit;
                box_masks[box_idx] |= bit;

                if dfs(idx + 1, empties, board, row_masks, col_masks, box_masks) { return true; }

                // 回溯
                board[r][c] = '.';
                row_masks[r] &= !bit;
                col_masks[c] &= !bit;
                box_masks[box_idx] &= !bit;

                // 去掉该候选
                avail &= avail - 1;
            }

            false
        }

        dfs(0, &empties, board, &mut row_masks, &mut col_masks, &mut box_masks);
    }
}