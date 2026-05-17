import plusOne from '../../solutions/typescript/0066';
import { test_cases } from '../../problems/0066-加一/test_cases.json';

describe('66. 加一', () => {
    test_cases.forEach((test_case: { input: number[]; expected: number[] }, index: number) => {
        test(`测试用例 ${index + 1}: input=${JSON.stringify(test_case.input)}`, () => {
            const result = plusOne([...test_case.input]);
            expect(result).toEqual(test_case.expected);
        });
    });
});
