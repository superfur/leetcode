function addBinary(a: string, b: string): string {
    let i = a.length - 1;
    let j = b.length - 1;
    let carry = 0;
    const result: string[] = [];
    while (i >= 0 || j >= 0 || carry) {
        let total = carry;
        if (i >= 0) total += parseInt(a[i--]);
        if (j >= 0) total += parseInt(b[j--]);
        result.push(String(total % 2));
        carry = Math.floor(total / 2);
    }
    return result.reverse().join('');
}

export default addBinary;
