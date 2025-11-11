impl Solution {
    pub fn is_match(s: String, p: String) -> bool {
        let s_bytes = s.as_bytes();
        let p_bytes = p.as_bytes();
        let mut i: usize = 0;
        let mut j: usize = 0;
        let mut star_idx: Option<usize> = None;
        let mut match_idx: usize = 0;

        while i < s_bytes.len() {
            if j < p_bytes.len()
                && (p_bytes[j] == b'?' || p_bytes[j] == s_bytes[i])
            {
                i += 1;
                j += 1;
            } else if j < p_bytes.len() && p_bytes[j] == b'*' {
                star_idx = Some(j);
                match_idx = i;
                j += 1;
            } else if let Some(star_pos) = star_idx {
                j = star_pos + 1;
                match_idx += 1;
                i = match_idx;
            } else {
                return false;
            }
        }

        while j < p_bytes.len() && p_bytes[j] == b'*' {
            j += 1;
        }

        j == p_bytes.len()
    }
}