import climbStairs from '../../solutions/typescript/0070';
import { test_cases } from '../../problems/0070-爬楼梯/test_cases.json';

describe('70. 爬楼梯', () => {
    test_cases.forEach((test_case: { input: number[]; expected: number }, index: number) => {
        test(`测试用例 ${index + 1}`, () => {
            const n = test_case.input[0];
            const result = climbStairs(n);
            expect(result).toEqual(test_case.expected);
        });
    });
});
