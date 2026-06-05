import mySqrt from '../../solutions/typescript/0069';
import { test_cases } from '../../problems/0069-x的平方根/test_cases.json';

describe('69. x 的平方根', () => {
    test_cases.forEach((test_case: { input: number[]; expected: number }, index: number) => {
        test(`测试用例 ${index + 1}`, () => {
            const x = test_case.input[0];
            const result = mySqrt(x);
            expect(result).toEqual(test_case.expected);
        });
    });
});
