import addBinary from '../../solutions/typescript/0067';
import { test_cases } from '../../problems/0067-二进制求和/test_cases.json';

describe('67. 二进制求和', () => {
    test_cases.forEach((test_case: { input: string[]; expected: string }, index: number) => {
        test(`测试用例 ${index + 1}: a="${test_case.input[0]}", b="${test_case.input[1]}"`, () => {
            const result = addBinary(test_case.input[0], test_case.input[1]);
            expect(result).toBe(test_case.expected);
        });
    });
});
