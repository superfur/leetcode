import sortColors from '../../solutions/typescript/0075';

describe('75. 颜色分类', () => {
    test.each([
        [[2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]],
        [[2, 0, 1], [0, 1, 2]],
        [[0], [0]],
        [[1], [1]],
        [[2], [2]],
        [[2, 2, 1, 0, 0, 1], [0, 0, 1, 1, 2, 2]],
    ])('sorts %p in place', (input: number[], expected: number[]) => {
        const nums = [...input];
        const result = sortColors(nums);

        expect(result).toBeUndefined();
        expect(nums).toEqual(expected);
    });
});
