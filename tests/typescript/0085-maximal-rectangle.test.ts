import maximalRectangle from '../../solutions/typescript/0085';
import { test_cases } from '../../problems/0085-最大矩形/test_cases.json';

describe('85. 最大矩形', () => {
    test_cases.forEach(
        (test_case: { input: { matrix: string[][] }; expected: number }, index: number) => {
            test(`测试用例 ${index + 1}`, () => {
                expect(maximalRectangle(test_case.input.matrix)).toEqual(test_case.expected);
            });
        }
    );
});