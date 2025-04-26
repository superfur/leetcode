use std::collections::HashMap;

pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map = HashMap::new();
    
    for (i, &num) in nums.iter().enumerate() {
        let complement = target - num;
        if let Some(&j) = map.get(&complement) {
            return vec![j as i32, i as i32];
        }
        map.insert(num, i);
    }
    
    vec![]
}

#[cfg(test)]
mod tests {
    use super::*;
    use test_case::test_case;

    #[test_case(vec![2, 7, 11, 15], 9, vec![0, 1])]
    #[test_case(vec![3, 2, 4], 6, vec![1, 2])]
    #[test_case(vec![3, 3], 6, vec![0, 1])]
    fn test_two_sum(nums: Vec<i32>, target: i32, expected: Vec<i32>) {
        assert_eq!(two_sum(nums, target), expected);
    }
} 