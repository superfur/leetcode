from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        组合总和 - 回溯算法
        找出所有可以使数字和为目标数 target 的不同组合
        同一个数字可以无限制重复被选取
        
        算法思路：
        1. 使用回溯算法（DFS）遍历所有可能的组合
        2. 每次可以选择当前数字或跳过，选择当前数字时可以重复选择
        3. 当和等于 target 时，记录当前组合
        4. 当和大于 target 时，剪枝返回
        5. 通过起始索引避免重复组合
        
        时间复杂度：O(S)，S 是所有可行解的长度之和
        空间复杂度：O(target)，递归栈的深度最多为 target
        
        Args:
            candidates: 候选数字数组（无重复元素）
            target: 目标和
            
        Returns:
            所有和为 target 的不同组合
        """
        result = []
        path = []
        
        def backtrack(start: int, current_sum: int) -> None:
            """
            回溯函数
            
            Args:
                start: 当前搜索的起始索引，避免重复组合
                current_sum: 当前路径的和
            """
            # 找到一个有效组合
            if current_sum == target:
                result.append(path[:])  # 复制当前路径
                return
            
            # 剪枝：当前和已经超过目标值
            if current_sum > target:
                return
            
            # 从 start 开始遍历，避免重复组合
            for i in range(start, len(candidates)):
                num = candidates[i]
                
                # 剪枝优化：如果加上当前数字已经超过目标，跳过
                if current_sum + num > target:
                    continue
                
                # 选择当前数字
                path.append(num)
                
                # 递归：注意这里是 i 而不是 i+1，因为可以重复使用当前数字
                backtrack(i, current_sum + num)
                
                # 撤销选择（回溯）
                path.pop()
        
        # 从索引 0 开始搜索
        backtrack(0, 0)
        
        return result