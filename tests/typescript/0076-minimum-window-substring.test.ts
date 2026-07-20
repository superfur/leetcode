import minWindow from '../../solutions/typescript/0076';
import { test_cases } from '../../problems/0076-最小覆盖子串/test_cases.json';

describe('76. 最小覆盖子串', () => {
    test_cases.forEach((test_case: { input: { s: string; t: string }; expected: string }, index: number) => {
        test(`测试用例 ${index + 1}`, () => {
            const { s, t } = test_case.input;
            const result = minWindow(s, t);
            expect(result).toEqual(test_case.expected);
        });
    });
});
