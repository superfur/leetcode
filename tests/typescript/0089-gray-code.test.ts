import grayCode from '../../solutions/typescript/0089';
import { test_cases } from '../../problems/0089-格雷编码/test_cases.json';

describe('89. 格雷编码', () => {
    test_cases.forEach(
        (test_case: { input: { n: number }; expected: number[] }, index: number) => {
            test(`测试用例 ${index + 1}`, () => {
                expect(grayCode(test_case.input.n)).toEqual(test_case.expected);
            });
        }
    );
});