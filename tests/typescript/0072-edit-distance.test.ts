import minDistance from '../../solutions/typescript/0072';
import { test_cases } from '../../problems/0072-编辑距离/test_cases.json';

describe('72. 编辑距离', () => {
    test_cases.forEach((test_case: { input: { word1: string; word2: string }; expected: number }, index: number) => {
        test(`测试用例 ${index + 1}`, () => {
            const result = minDistance(test_case.input.word1, test_case.input.word2);
            expect(result).toEqual(test_case.expected);
        });
    });
});
