import subsetsWithDup from '../../solutions/typescript/0090';
import { test_cases } from '../../problems/0090-子集 II/test_cases.json';

interface TestCase {
    input: { nums: number[] };
    expected: number[][];
}

function normalize(subsets: number[][]): string[] {
    return subsets
        .map(s => [...s].sort((a, b) => a - b))
        .sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)))
        .map(s => JSON.stringify(s));
}

describe('90. 子集 II', () => {
    (test_cases as TestCase[]).forEach((testCase, index) => {
        test(`测试用例 ${index + 1}`, () => {
            const result = subsetsWithDup(testCase.input.nums);
            expect(normalize(result)).toEqual(normalize(testCase.expected));
        });
    });
});