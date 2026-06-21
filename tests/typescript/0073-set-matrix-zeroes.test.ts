import setZeroes from '../../solutions/typescript/0073';
import { test_cases } from '../../problems/0073-矩阵置零/test_cases.json';

describe('73. 矩阵置零', () => {
    test_cases.forEach((test_case: { input: number[][]; expected: number[][] }, index: number) => {
        test(`测试用例 ${index + 1}`, () => {
            const matrix = test_case.input.map((row) => [...row]);
            setZeroes(matrix);
            expect(matrix).toEqual(test_case.expected);
        });
    });
});
