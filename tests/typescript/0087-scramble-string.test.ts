import isScramble from '../../solutions/typescript/0087';
import { test_cases } from '../../problems/0087-扰乱字符串/test_cases.json';

describe('87. 扰乱字符串', () => {
    test_cases.forEach(
        (test_case: { input: { s1: string; s2: string }; expected: boolean }, index: number) => {
            test(`测试用例 ${index + 1}`, () => {
                expect(isScramble(test_case.input.s1, test_case.input.s2)).toEqual(test_case.expected);
            });
        }
    );
});