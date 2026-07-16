import searchMatrix from '../../solutions/typescript/0074';
import { test_cases } from '../../problems/0074-搜索二维矩阵/test_cases.json';

describe('74. 搜索二维矩阵', () => {
    test_cases.forEach((test_case: { input: { matrix: number[][]; target: number }; expected: boolean }, index: number) => {
        test(`测试用例 ${index + 1}`, () => {
            const result = searchMatrix(test_case.input.matrix, test_case.input.target);
            expect(result).toEqual(test_case.expected);
        });
    });
});