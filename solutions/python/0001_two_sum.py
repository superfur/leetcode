from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    两数之和
    :param nums: 整数数组
    :param target: 目标值
    :return: 两个数的索引
    """
    num_map = {}
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
        print(f"测试用例 {i}:")
        print(f"输入: nums = {input_data['nums']}, target = {input_data['target']}")
        print(f"输出: {result}")
        print(f"预期: {expected}")
        print(f"结果: {'通过' if result == expected else '失败'}\n") 