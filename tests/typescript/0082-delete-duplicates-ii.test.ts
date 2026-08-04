import deleteDuplicates from '../../solutions/typescript/0082';
import { test_cases } from '../../problems/0082-删除排序链表中的重复元素 II/test_cases.json';

// 本地测试需要构造与平台注入 ListNode 同形的数据结构；解法使用 LNode 接口，
// 字段一致，构造的对象可双向流通。
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

describe('82. 删除排序链表中的重复元素 II', () => {
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