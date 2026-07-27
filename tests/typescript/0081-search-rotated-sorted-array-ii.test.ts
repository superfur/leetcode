import search from '../../solutions/typescript/0081';
import { test_cases } from '../../problems/0081-搜索旋转排序数组 II/test_cases.json';

describe('81. 搜索旋转排序数组 II', () => {
    test_cases.forEach(
        (
            test_case: { input: { nums: number[]; target: number }; expected: boolean },
            index: number
        ) => {
            test(`测试用例 ${index + 1}`, () => {
                const { nums, target } = test_case.input;
                expect(search(nums, target)).toEqual(test_case.expected);
            });
        }
    );
});