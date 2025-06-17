impl Solution {
    fn is_palindrome(mut x: i32) -> bool {
        if x < 0 {
            return false;
        }
        let mut reversed = 0;
        let mut original = x;
        while x > 0 {
            reversed = reversed * 10 + x % 10;
            x = x / 10;
        }
        return reversed == original;
    }
}