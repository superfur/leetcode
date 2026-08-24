import reverseBetween from '../../solutions/typescript/0092';
import { test_cases } from '../../problems/0092-反转链表 II/test_cases.json';

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

describe('92. 反转链表 II', () => {
    test_cases.forEach(
        (
            test_case: { input: { values: number[]; left: number; right: number }; expected: number[] },
            index: number
        ) => {
            test(`测试用例 ${index + 1}`, () => {
                const head = fromValues(test_case.input.values);
                const resultHead = reverseBetween(head, test_case.input.left, test_case.input.right);
                expect(toList(resultHead)).toEqual(test_case.expected);
            });
        }
    );
});
