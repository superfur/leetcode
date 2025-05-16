impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1 {
            return s;
        }
        let num_rows = num_rows as usize;
        let mut rows = vec![String::new(); num_rows];
        let mut cur_row: i32 = 0;
        let mut going_down = false;
        for c in s.chars() {
            rows[cur_row as usize].push(c);
            if cur_row == 0 || cur_row == num_rows as i32 - 1 {
                going_down = !going_down;
            }
            cur_row += if going_down { 1 } else { -1 };
        }
        rows.join("")
    }
}
