import numDecodings from '../../solutions/typescript/0091';
import { test_cases } from '../../problems/0091-解码方法/test_cases.json';

describe('91. 解码方法', () => {
    test_cases.forEach(
        (test_case: { input: { s: string }; expected: number }, index: number) => {
            test(`测试用例 ${index + 1}`, () => {
                expect(numDecodings(test_case.input.s)).toEqual(test_case.expected);
            });
        }
    );
});
