import isNumber from '../../solutions/typescript/0065';
import { test_cases } from '../../problems/0065-有效数字/test_cases.json';

describe('65. 有效数字', () => {
    test_cases.forEach((test_case: { input: string; expected: boolean }, index: number) => {
        test(`测试用例 ${index + 1}: input="${test_case.input}"`, () => {
            const result = isNumber(test_case.input);
            expect(result).toBe(test_case.expected);
        });
    });
});
