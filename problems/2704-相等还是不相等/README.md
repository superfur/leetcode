# 2704. 相等还是不相等

## 题目描述

<p>请你编写一个名为 <code>expect</code> 的函数，用于帮助开发人员测试他们的代码。它应该接受任何值 <code>val</code> 并返回一个包含以下两个函数的对象。</p>

<ul>
	<li><code>toBe(val)</code> 接受另一个值并在两个值相等（ <code>===</code> ）时返回 <code>true</code> 。如果它们不相等，则应抛出错误 <code>"Not Equal"</code> 。</li>
	<li><code>notToBe(val)</code> 接受另一个值并在两个值不相等（ <code>!==</code> ）时返回 <code>true</code> 。如果它们相等，则应抛出错误 <code>"Equal"</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>func = () =&gt; expect(5).toBe(5)
<b>输出：</b>{"value": true}
<b>解释：</b>5 === 5 因此该表达式返回 true。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>func = () =&gt; expect(5).toBe(null)
<b>输出：</b>{"error": "Not Equal"}
<b>解释：</b>5 !== null 因此抛出错误 "Not Equal".
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>func = () =&gt; expect(5).notToBe(null)
<b>输出：</b>{"value": true}
<b>解释：</b>5 !== null 因此该表达式返回 true.
</pre>


## 难度

Easy

## 示例

```
() => expect(5).toBe(5)
() => expect(5).toBe(null)
() => expect(5).notToBe(null)
```

## 示例代码

### JavaScript

```javascript
/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
```

### TypeScript

```typescript
type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
```

