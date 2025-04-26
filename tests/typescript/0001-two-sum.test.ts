import twoSum from '../../solutions/typescript/src/0001-two-sum';
import { test_cases } from '../../problems/0001-two-sum/test_cases.json';

describe('两数之和', () => {
    test_cases.forEach((test_case, index) => {
        test(`测试用例 ${index + 1}`, () => {
            const { input, expected } = test_case;
            const result = twoSum(input.nums, input.target);
            expect(result).toEqual(expected);
        });
    });
}); 