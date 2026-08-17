import merge from '../../solutions/typescript/0088';
import { test_cases } from '../../problems/0088-合并两个有序数组/test_cases.json';

interface Input {
    nums1: number[];
    m: number;
    nums2: number[];
    n: number;
}

describe('88. 合并两个有序数组', () => {
    test_cases.forEach(
        (test_case: { input: Input; expected: number[] }, index: number) => {
            test(`测试用例 ${index + 1}`, () => {
                // 深拷贝，避免对原数组的原地修改污染后续用例
                const nums1 = [...test_case.input.nums1];
                merge(nums1, test_case.input.m, test_case.input.nums2, test_case.input.n);
                expect(nums1).toEqual(test_case.expected);
            });
        }
    );
});