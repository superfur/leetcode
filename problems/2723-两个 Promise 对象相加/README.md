# 2723. 两个 Promise 对象相加

## 题目描述

给定两个 promise 对象&nbsp;<code>promise1</code> 和 <code>promise2</code>，返回一个新的 promise。<code>promise1</code> 和 <code>promise2</code> 都会被解析为一个数字。返回的 Promise 应该解析为这两个数字的和。
<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>
promise1 = new Promise(resolve =&gt; setTimeout(() =&gt; resolve(2), 20)), 
promise2 = new Promise(resolve =&gt; setTimeout(() =&gt; resolve(5), 60))
<b>输出：</b>7
<b>解释：</b>两个输入的 Promise 分别解析为值 2 和 5。返回的 Promise 应该解析为 2 + 5 = 7。返回的 Promise 解析的时间不作为判断条件。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>
promise1 = new Promise(resolve =&gt; setTimeout(() =&gt; resolve(10), 50)), 
promise2 = new Promise(resolve =&gt; setTimeout(() =&gt; resolve(-12), 30))
<b>输出：</b>-2
<b>解释：</b>两个输入的 Promise 分别解析为值 10 和 -12。返回的 Promise 应该解析为 10 + -12 = -2。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>promise1 和 promise2</code> 都是被解析为一个数字的 promise 对象</li>
</ul>


## 难度

Easy

## 示例

```
new Promise(resolve => setTimeout(() => resolve(2), 20))
new Promise(resolve => setTimeout(() => resolve(5), 60))
new Promise(resolve => setTimeout(() => resolve(10), 50))
new Promise(resolve => setTimeout(() => resolve(-12), 30))
```

## 示例代码

### JavaScript

```javascript
/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
```

### TypeScript

```typescript
type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
```

