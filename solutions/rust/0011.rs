impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = height.len() - 1;
        let mut max_water = 0;

        while left < right {
            let width = (right - left) as i32;
            let h = height[left].min(height[right]);
            let current_water = width * h;

            max_water = max_water.max(current_water);

            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            }
        }
        max_water
    }
}