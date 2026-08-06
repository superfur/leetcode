import largestRectangleArea from '../../solutions/typescript/0084';
import { test_cases } from '../../problems/0084-柱状图中最大的矩形/test_cases.json';

describe('84. 柱状图中最大的矩形', () => {
    test_cases.forEach(
        (test_case: { input: { heights: number[] }; expected: number }, index: number) => {
            test(`测试用例 ${index + 1}`, () => {
                expect(largestRectangleArea(test_case.input.heights)).toEqual(test_case.expected);
            });
        }
    );
});