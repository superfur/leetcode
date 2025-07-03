use std::collections::HashMap;

impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.is_empty() {
            return vec![];
        }

        let map = HashMap::from([
            ('2', vec!['a', 'b', 'c']),
            ('3', vec!['d', 'e', 'f']),
            ('4', vec!['g', 'h', 'i']),
            ('5', vec!['j', 'k', 'l']),
            ('6', vec!['m', 'n', 'o']),
            ('7', vec!['p', 'q', 'r', 's']),
            ('8', vec!['t', 'u', 'v']),
            ('9', vec!['w', 'x', 'y', 'z']),
        ]);

        let mut result = vec![];
        let mut combination = String::new();
        let digits_chars: Vec<char> = digits.chars().collect();

        fn backtrack(
            index: usize,
            digits_chars: &Vec<char>,
            map: &HashMap<char, Vec<char>>,
            combination: &mut String,
            result: &mut Vec<String>,
        ) {
            if index == digits_chars.len() {
                result.push(combination.clone());
                return;
            }

            if let Some(letters) = map.get(&digits_chars[index]) {
                for &letter in letters {
                    combination.push(letter);
                    backtrack(index + 1, digits_chars, map, combination, result);
                    combination.pop();
                }
            }
        }

        backtrack(0, &digits_chars, &map, &mut combination, &mut result);
        result
    }
}