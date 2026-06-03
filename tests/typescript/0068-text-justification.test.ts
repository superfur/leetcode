import fullJustify from '../../solutions/typescript/0068';
import { test_cases } from '../../problems/0068-文本左右对齐/test_cases.json';

describe('68. 文本左右对齐', () => {
    test_cases.forEach((test_case: { input: (string[] | number)[]; expected: string[] }, index: number) => {
        test(`测试用例 ${index + 1}`, () => {
            const words = test_case.input[0] as string[];
            const maxWidth = test_case.input[1] as number;
            const result = fullJustify(words, maxWidth);
            expect(result).toEqual(test_case.expected);
        });
    });
});
