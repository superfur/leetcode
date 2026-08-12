import partition from '../../solutions/typescript/0086';
import { test_cases } from '../../problems/0086-分隔链表/test_cases.json';

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

describe('86. 分隔链表', () => {
    test_cases.forEach(
        (test_case: { input: { values: number[]; x: number }; expected: number[] }, index: number) => {
            test(`测试用例 ${index + 1}`, () => {
                const head = fromValues(test_case.input.values);
                const resultHead = partition(head, test_case.input.x);
                expect(toList(resultHead)).toEqual(test_case.expected);
            });
        }
    );
});