impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let mut merged = [nums1, nums2].concat();
        merged.sort_unstable();
        let middle = merged.len() / 2;
        if merged.len() % 2 == 1 {
            merged[middle] as f64
        } else {
            (merged[middle - 1] as f64 + merged[middle] as f64) / 2.0
        }
    }
}




