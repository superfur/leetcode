// 定义链表节点类
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

// 从数组创建链表
function createLinkedList(arr: number[]): ListNode | null {
    if (arr.length === 0) return null;
    const head = new ListNode(arr[0]);
    let current = head;
    for (let i = 1; i < arr.length; i++) {
        current.next = new ListNode(arr[i]);
        current = current.next;
    }
    return head;
}

// 将链表转换为数组
function linkedListToArray(head: ListNode | null): number[] {
    const result: number[] = [];
    let current = head;
    while (current) {
        result.push(current.val);
        current = current.next;
    }
    return result;
}

// 反转K个节点的函数
function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    if (!head || k === 1) return head;
    const dummy = new ListNode(0, head);
    let prev = dummy;
    let current = head;
    while (current) {
        // 检查是否有足够的节点进行反转
        let tail = current;
        let count = 1;
        while (tail.next && count < k) {
            tail = tail.next;
            count++;
        }
        
        // 如果节点数量不足k个，直接返回
        if (count < k) break;
        
        const next = tail.next;
        tail.next = null;
        const [newHead, newTail] = reverse(current);
        prev.next = newHead;
        newTail.next = next;
        prev = newTail;
        current = next;
    }
    return dummy.next;
}

function reverse(head: ListNode | null): [ListNode | null, ListNode | null] {
    let prev = null;
    let current = head;
    while (current) {
        const next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }
    return [prev, head];
}

// 测试用例
function test() {
    console.log("测试开始...");
    
    // 测试用例1: [1,2,3,4], k=2
    const input1 = [1, 2, 3, 4];
    const k1 = 2;
    const head1 = createLinkedList(input1);
    const result1 = reverseKGroup(head1, k1);
    const output1 = linkedListToArray(result1);
    console.log(`输入: [${input1}], k=${k1}`);
    console.log(`输出: [${output1}]`);
    console.log(`期望: [2,1,4,3]`);
    console.log(`测试结果: ${JSON.stringify(output1) === JSON.stringify([2,1,4,3]) ? '通过' : '失败'}`);
    console.log();
    
    // 测试用例2: [1,2,3,4,5], k=3
    const input2 = [1, 2, 3, 4, 5];
    const k2 = 3;
    const head2 = createLinkedList(input2);
    const result2 = reverseKGroup(head2, k2);
    const output2 = linkedListToArray(result2);
    console.log(`输入: [${input2}], k=${k2}`);
    console.log(`输出: [${output2}]`);
    console.log(`期望: [3,2,1,4,5]`);
    console.log(`测试结果: ${JSON.stringify(output2) === JSON.stringify([3,2,1,4,5]) ? '通过' : '失败'}`);
    console.log();
    
    // 测试用例3: [1], k=1
    const input3 = [1];
    const k3 = 1;
    const head3 = createLinkedList(input3);
    const result3 = reverseKGroup(head3, k3);
    const output3 = linkedListToArray(result3);
    console.log(`输入: [${input3}], k=${k3}`);
    console.log(`输出: [${output3}]`);
    console.log(`期望: [1]`);
    console.log(`测试结果: ${JSON.stringify(output3) === JSON.stringify([1]) ? '通过' : '失败'}`);
    
    console.log("测试完成！");
}

test(); 