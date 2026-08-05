import deleteDuplicates from '../../solutions/typescript/0083';
import { test_cases } from '../../problems/0083-删除排序链表中的重复元素/test_cases.json';

// 与解法使用的 LNode 接口同形即可。
interface LNode { val: number; next: LNode | null }

function fromValues(values: number[]): LNode | null {
    let head: LNode | null = null;
    for (let i = values.length - 1; i >= 0; i--) {
        head = { val: values[i], next: head };
    }
    return head;
}

function toList(head: LNode | null): number[] {
    const out: number[] = [];
    while (head) {
        out.push(head.val);
        head = head.next;
    }
    return out;
}

describe('83. 删除排序链表中的重复元素', () => {
    test_cases.forEach(
        (test_case: { input: { values: number[] }; expected: number[] }, index: number) => {
            test(`测试用例 ${index + 1}`, () => {
                const head = fromValues(test_case.input.values);
                const resultHead = deleteDuplicates(head);
                expect(toList(resultHead)).toEqual(test_case.expected);
            });
        }
    );
});