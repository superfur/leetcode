impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let a: Vec<u8> = a.bytes().collect();
        let b: Vec<u8> = b.bytes().collect();
        let mut i = a.len() as i32 - 1;
        let mut j = b.len() as i32 - 1;
        let mut carry = 0i32;
        let mut result = Vec::new();
        while i >= 0 || j >= 0 || carry > 0 {
            let mut total = carry;
            if i >= 0 {
                total += (a[i as usize] - b'0') as i32;
                i -= 1;
            }
            if j >= 0 {
                total += (b[j as usize] - b'0') as i32;
                j -= 1;
            }
            result.push((total % 2) as u8 + b'0');
            carry = total / 2;
        }
        result.reverse();
        String::from_utf8(result).unwrap()
    }
}
