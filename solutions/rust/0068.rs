impl Solution {
    pub fn full_justify(words: Vec<String>, max_width: i32) -> Vec<String> {
        let max_width = max_width as usize;
        let mut result: Vec<String> = Vec::new();
        let mut i = 0;

        while i < words.len() {
            let mut line_len = words[i].len();
            let mut j = i + 1;
            while j < words.len() && line_len + 1 + words[j].len() <= max_width {
                line_len += 1 + words[j].len();
                j += 1;
            }

            let line_words = &words[i..j];
            let total_chars: usize = line_words.iter().map(|w| w.len()).sum();
            let gaps = line_words.len() - 1;
            let is_last_line = j == words.len();

            if gaps == 0 || is_last_line {
                let mut line = line_words.join(" ");
                let padding = max_width - line.len();
                line.push_str(&" ".repeat(padding));
                result.push(line);
            } else {
                let total_spaces = max_width - total_chars;
                let space_per_gap = total_spaces / gaps;
                let mut extra_spaces = total_spaces % gaps;
                let mut line = String::new();
                for k in 0..line_words.len() {
                    line.push_str(&line_words[k]);
                    if k < gaps {
                        let spaces = space_per_gap + if extra_spaces > 0 { 1 } else { 0 };
                        if extra_spaces > 0 {
                            extra_spaces -= 1;
                        }
                        line.push_str(&" ".repeat(spaces));
                    }
                }
                result.push(line);
            }

            i = j;
        }

        result
    }
}
