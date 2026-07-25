import exist from '../../solutions/typescript/0079';
import { test_cases } from '../../problems/0079-单词搜索/test_cases.json';

describe('79. 单词搜索', () => {
    test_cases.forEach((test_case: { input: { board: string[][]; word: string }; expected: boolean }, index: number) => {
        test(`测试用例 ${index + 1}`, () => {
            const { board, word } = test_case.input;
            // 深拷贝，避免对原 board 的原地修改污染后续用例
            const boardCopy = board.map((row) => [...row]);
            const result = exist(boardCopy, word);
            expect(result).toEqual(test_case.expected);
        });
    });
});