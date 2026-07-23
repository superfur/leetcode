import subsets from '../../solutions/typescript/0078';
import { test_cases } from '../../problems/0078-子集/test_cases.json';

describe('78. 子集', () => {
    test_cases.forEach((test_case: { input: { nums: number[] }; expected: number[][] }, index: number) => {
        test(`测试用例 ${index + 1}`, () => {
            const { nums } = test_case.input;
            const result = subsets(nums);
            // 子集顺序任意，用集合比较 (内部元素顺序与 expected 一致)
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