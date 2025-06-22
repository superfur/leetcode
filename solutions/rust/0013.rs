use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let roman_map = HashMap::from([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)
        ]);
        let mut result = 0;
        for (i, c) in s.chars().enumerate() {
            let current = roman_map.get(&c).unwrap();
            let next = roman_map.get(&s.chars().nth(i + 1).unwrap_or(' ')).unwrap_or(&0);
            if current < next {
                result -= current;
            } else {
                result += current;
            }
        }
        result
    }
}
