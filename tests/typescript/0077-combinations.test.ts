import combine from '../../solutions/typescript/0077';
import { test_cases } from '../../problems/0077-组合/test_cases.json';

describe('77. 组合', () => {
    test_cases.forEach((test_case: { input: { n: number; k: number }; expected: number[][] }, index: number) => {
        test(`测试用例 ${index + 1}`, () => {
            const { n, k } = test_case.input;
            const result = combine(n, k);
            // 题目允许任意顺序，转换为集合比较
            const sortedResult = new Set(result.map((c) => JSON.stringify([...c].sort((a, b) => a - b))));
            const sortedExpected = new Set(
                test_case.expected.map((c) => JSON.stringify([...c].sort((a, b) => a - b)))
            );

            expect(sortedResult.size).toEqual(sortedExpected.size);
            for (const key of sortedExpected) {
                expect(sortedResult.has(key)).toBe(true);
            }
        });
    });
});
