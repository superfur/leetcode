import os
import json
from typing import Dict

def generate_typescript_solution(problem: Dict) -> str:
    """生成TypeScript解法模板"""
    return f"""/**
 * {problem['title']}
 * @param nums 整数数组
 * @param target 目标值
 * @returns 两个数的索引
 */
function twoSum(nums: number[], target: number): number[] {{
    const map = new Map<number, number>();
    
    for (let i = 0; i < nums.length; i++) {{
        const complement = target - nums[i];
        if (map.has(complement)) {{
            return [map.get(complement)!, i];
        }}
        map.set(nums[i], i);
    }}
    
    return [];
}}

export default twoSum;
"""

def generate_rust_solution(problem: Dict) -> str:
    """生成Rust解法模板"""
    return f"""use std::collections::HashMap;

pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {{
    let mut map = HashMap::new();
    
    for (i, &num) in nums.iter().enumerate() {{
        let complement = target - num;
        if let Some(&j) = map.get(&complement) {{
            return vec![j as i32, i as i32];
        }}
        map.insert(num, i);
    }}
    
    vec![]
}}

#[cfg(test)]
mod tests {{
    use super::*;
    use test_case::test_case;

    #[test_case(vec![2, 7, 11, 15], 9, vec![0, 1])]
    #[test_case(vec![3, 2, 4], 6, vec![1, 2])]
    #[test_case(vec![3, 3], 6, vec![0, 1])]
    fn test_two_sum(nums: Vec<i32>, target: i32, expected: Vec<i32>) {{
        assert_eq!(two_sum(nums, target), expected);
    }}
}}
"""

def generate_python_solution(problem: Dict) -> str:
    """生成Python解法模板"""
    return f"""from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    {problem['title']}
    :param nums: 整数数组
    :param target: 目标值
    :return: 两个数的索引
    """
    num_map = {{}}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

if __name__ == "__main__":
    import json
    with open("../../problems/0001-two-sum/test_cases.json", "r") as f:
        test_cases = json.load(f)["test_cases"]
    
    for i, test_case in enumerate(test_cases, 1):
        input_data = test_case["input"]
        expected = test_case["expected"]
        result = two_sum(input_data["nums"], input_data["target"])
        print(f"测试用例 {{i}}:")
        print(f"输入: nums = {{input_data['nums']}}, target = {{input_data['target']}}")
        print(f"输出: {{result}}")
        print(f"预期: {{expected}}")
        print(f"结果: {{'通过' if result == expected else '失败'}}\\n")
"""

def generate_go_solution(problem: Dict) -> str:
    """生成Go解法模板"""
    return f"""package main

func twoSum(nums []int, target int) []int {{
    numMap := make(map[int]int)
    
    for i, num := range nums {{
        complement := target - num
        if j, ok := numMap[complement]; ok {{
            return []int{{j, i}}
        }}
        numMap[num] = i
    }}
    
    return []int{{}}
}}

func main() {{
    // 测试用例
    testCases := []struct {{
        nums     []int
        target   int
        expected []int
    }}{{
        {{[]int{{2, 7, 11, 15}}, 9, []int{{0, 1}}}},
        {{[]int{{3, 2, 4}}, 6, []int{{1, 2}}}},
        {{[]int{{3, 3}}, 6, []int{{0, 1}}}},
    }}
    
    for i, tc := range testCases {{
        result := twoSum(tc.nums, tc.target)
        if len(result) != len(tc.expected) {{
            println("测试用例", i+1, "失败")
            continue
        }}
        for j := range result {{
            if result[j] != tc.expected[j] {{
                println("测试用例", i+1, "失败")
                break
            }}
        }}
        println("测试用例", i+1, "通过")
    }}
}}
"""

def generate_java_solution(problem: Dict) -> str:
    """生成Java解法模板"""
    return f"""package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class Solution {{
    /**
     * {problem['title']}
     * @param nums 整数数组
     * @param target 目标值
     * @return 两个数的索引
     */
    public int[] twoSum(int[] nums, int target) {{
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {{
            int complement = target - nums[i];
            if (map.containsKey(complement)) {{
                return new int[]{{map.get(complement), i}};
            }}
            map.put(nums[i], i);
        }}
        
        return new int[0];
    }}
}}
"""

def generate_test_files(problem: Dict):
    """为每个问题生成各种语言的测试文件"""
    problem_id = problem["stat"]["frontend_question_id"]
    title_slug = problem["stat"]["question__title_slug"]
    
    # 读取测试用例
    test_cases_path = os.path.join("problems", f"{problem_id:04d}-{title_slug}", "test_cases.json")
    with open(test_cases_path, "r") as f:
        test_cases = json.load(f)["test_cases"]
    
    # 生成TypeScript测试文件
    ts_test = f"""import twoSum from '../../solutions/typescript/src/{problem_id:04d}-{title_slug}';
import {{ test_cases }} from '../../problems/{problem_id:04d}-{title_slug}/test_cases.json';

describe('{problem["title"]}', () => {{
    test_cases.forEach((test_case, index) => {{
        test(`测试用例 ${{index + 1}}`, () => {{
            const {{ input, expected }} = test_case;
            const result = twoSum(input.nums, input.target);
            expect(result).toEqual(expected);
        }});
    }});
}});
"""
    
    # 生成Rust测试文件
    rust_test = f"""use super::*;
use test_case::test_case;

#[test_case(vec![2, 7, 11, 15], 9, vec![0, 1])]
#[test_case(vec![3, 2, 4], 6, vec![1, 2])]
#[test_case(vec![3, 3], 6, vec![0, 1])]
fn test_two_sum(nums: Vec<i32>, target: i32, expected: Vec<i32>) {{
    assert_eq!(two_sum(nums, target), expected);
}}
"""
    
    # 生成Python测试文件
    python_test = f"""import pytest
from solutions.python.{problem_id:04d}_{title_slug} import two_sum

def test_two_sum():
    test_cases = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1])
    ]
    
    for (input_data, expected) in test_cases:
        nums, target = input_data
        assert two_sum(nums, target) == expected
"""
    
    # 生成Go测试文件
    go_test = f"""package main

import (
    "testing"
)

func TestTwoSum(t *testing.T) {{
    testCases := []struct {{
        nums     []int
        target   int
        expected []int
    }}{{
        {{[]int{{2, 7, 11, 15}}, 9, []int{{0, 1}}}},
        {{[]int{{3, 2, 4}}, 6, []int{{1, 2}}}},
        {{[]int{{3, 3}}, 6, []int{{0, 1}}}},
    }}
    
    for i, tc := range testCases {{
        result := twoSum(tc.nums, tc.target)
        if len(result) != len(tc.expected) {{
            t.Errorf("测试用例 %d 失败", i+1)
            continue
        }}
        for j := range result {{
            if result[j] != tc.expected[j] {{
                t.Errorf("测试用例 %d 失败", i+1)
                break
            }}
        }}
    }}
}}
"""
    
    # 生成Java测试文件
    java_test = f"""package com.leetcode;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {{
    @Test
    void testTwoSum() {{
        Solution solution = new Solution();
        
        int[] nums1 = {{2, 7, 11, 15}};
        int target1 = 9;
        int[] expected1 = {{0, 1}};
        assertArrayEquals(expected1, solution.twoSum(nums1, target1));
        
        int[] nums2 = {{3, 2, 4}};
        int target2 = 6;
        int[] expected2 = {{1, 2}};
        assertArrayEquals(expected2, solution.twoSum(nums2, target2));
        
        int[] nums3 = {{3, 3}};
        int target3 = 6;
        int[] expected3 = {{0, 1}};
        assertArrayEquals(expected3, solution.twoSum(nums3, target3));
    }}
}}
"""
    
    # 保存测试文件
    os.makedirs(f"tests/typescript", exist_ok=True)
    os.makedirs(f"tests/rust", exist_ok=True)
    os.makedirs(f"tests/python", exist_ok=True)
    os.makedirs(f"tests/go", exist_ok=True)
    os.makedirs(f"tests/java", exist_ok=True)
    
    with open(f"tests/typescript/{problem_id:04d}-{title_slug}.test.ts", "w") as f:
        f.write(ts_test)
    
    with open(f"tests/rust/{problem_id:04d}_{title_slug}.rs", "w") as f:
        f.write(rust_test)
    
    with open(f"tests/python/test_{problem_id:04d}_{title_slug}.py", "w") as f:
        f.write(python_test)
    
    with open(f"tests/go/{problem_id:04d}_{title_slug}_test.go", "w") as f:
        f.write(go_test)
    
    with open(f"tests/java/SolutionTest.java", "w") as f:
        f.write(java_test)

def main():
    """主函数"""
    # 创建必要的目录
    os.makedirs("solutions/typescript/src", exist_ok=True)
    os.makedirs("solutions/rust/src", exist_ok=True)
    os.makedirs("solutions/python", exist_ok=True)
    os.makedirs("solutions/go", exist_ok=True)
    os.makedirs("solutions/java", exist_ok=True)
    
    # 获取问题列表
    with open("problems.json", "r") as f:
        problems = json.load(f)
    
    # 为每个问题生成解法
    for problem in problems[:1000]:
        problem_id = problem["stat"]["frontend_question_id"]
        title_slug = problem["stat"]["question__title_slug"]
        
        # 生成解法文件
        with open(f"solutions/typescript/src/{problem_id:04d}-{title_slug}.ts", "w") as f:
            f.write(generate_typescript_solution(problem))
        
        with open(f"solutions/rust/src/{problem_id:04d}_{title_slug}.rs", "w") as f:
            f.write(generate_rust_solution(problem))
        
        with open(f"solutions/python/{problem_id:04d}_{title_slug}.py", "w") as f:
            f.write(generate_python_solution(problem))
        
        with open(f"solutions/go/{problem_id:04d}_{title_slug}.go", "w") as f:
            f.write(generate_go_solution(problem))
        
        with open(f"solutions/java/Solution.java", "w") as f:
            f.write(generate_java_solution(problem))
        
        # 生成测试文件
        generate_test_files(problem)

if __name__ == "__main__":
    main() 