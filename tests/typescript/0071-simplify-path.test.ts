import simplifyPath from '../../solutions/typescript/0071';
import { test_cases } from '../../problems/0071-简化路径/test_cases.json';

describe('71. 简化路径', () => {
    test_cases.forEach((test_case: { input: string; expected: string }, index: number) => {
        test(`测试用例 ${index + 1}`, () => {
            const result = simplifyPath(test_case.input);
            expect(result).toEqual(test_case.expected);
        });
    });
});
