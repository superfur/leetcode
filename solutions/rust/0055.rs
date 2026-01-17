use std::cmp;

impl Solution {
    /*
     * 跳跃游戏 - 贪心算法
     * 
     * 时间复杂度: O(n)，只需遍历一次数组
     * 空间复杂度: O(1)，只使用常数个变量
     * 
     * 思路: 贪心算法
     * 1. 维护当前能到达的最远位置 farthest
     * 2. 从左到右遍历数组：
     *    - 如果当前位置 i 已经超过 farthest，说明 i 不可达，直接返回 false
     *    - 否则更新 farthest = max(farthest, i + nums[i])
     * 3. 若 farthest >= 最后下标，则可以到达，返回 true
     * 
     * 核心思想:
     * - 不需要遍历所有可能的路径，只需要知道能否到达最后
     * - 贪心地维护能到达的最远位置，如果当前位置不可达，则后续也不可达
     * 
     * 示例:
     * nums = [2,3,1,1,4]
     * i=0: farthest=max(0,0+2)=2
     * i=1: farthest=max(2,1+3)=4 >= 4 => true
     * 
     * nums = [3,2,1,0,4]
     * i=0: farthest=max(0,0+3)=3
     * i=1: farthest=max(3,1+2)=3
     * i=2: farthest=max(3,2+1)=3
     * i=3: farthest=max(3,3+0)=3, i=3 <= 3 可达
     * i=4: i=4 > 3 不可达 => false
     */
    pub fn can_jump(nums: Vec<i32>) -> bool {
        if nums.is_empty() {
            return false;
        }
        
        let mut farthest: usize = 0;  // 当前能到达的最远位置
        let last = nums.len() - 1;
        
        for i in 0..nums.len() {
            // 如果当前位置已经超过能到达的最远位置，说明不可达
            if i > farthest {
                return false;
            }
            
            // 更新能到达的最远位置
            // 注意：nums[i] 是 i32，需要转换为 usize
            let reach = i + nums[i] as usize;
            if reach > farthest {
                farthest = reach;
            }
            
            // 如果已经可以到达最后一个位置，提前返回
            if farthest >= last {
                return true;
            }
        }
        
        true
    }
}