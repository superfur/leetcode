import removeDuplicates from '../../solutions/typescript/0080';
import { test_cases } from '../../problems/0080-删除有序数组中的重复项 II/test_cases.json';

interface Expected {
    length: number;
    prefix: number[];
}

describe('80. 删除有序数组中的重复项 II', () => {
    test_cases.forEach(
        (
            test_case: { input: { nums: number[] }; expected: Expected },
            index: number
        ) => {
            test(`测试用例 ${index + 1}`, () => {
                // 深拷贝 nums，因为 removeDuplicates 是原地修改
                const nums = [...test_case.input.nums];
                const length = removeDuplicates(nums);
                expect(length).toEqual(test_case.expected.length);
                expect(nums.slice(0, length)).toEqual(test_case.expected.prefix);
            });
        }
    );
});