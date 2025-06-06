# 2665. 计数器 II

## 题目描述

<p>请你写一个函数&nbsp;<code>createCounter</code>。这个函数接收一个初始的整数值 <code>init</code>。并返回一个包含三个函数的对象。</p>

<p>这三个函数是：</p>

<ul>
	<li><code>increment()</code>&nbsp;将当前值加 1 并返回。</li>
	<li><code>decrement()</code>&nbsp;将当前值减 1 并返回。</li>
	<li><code>reset()</code>&nbsp;将当前值设置为 <code>init</code> 并返回。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>init = 5, calls = ["increment","reset","decrement"]
<strong>输出：</strong>[6,5,4]
<strong>解释：</strong>
const counter = createCounter(5);
counter.increment(); // 6
counter.reset(); // 5
counter.decrement(); // 4
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>init = 0, calls = ["increment","increment","decrement","reset","reset"]
<strong>输出：</strong>[1,2,1,0,0]
<strong>解释：</strong>
const counter = createCounter(0);
counter.increment(); // 1
counter.increment(); // 2
counter.decrement(); // 1
counter.reset(); // 0
counter.reset(); // 0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-1000 &lt;= init &lt;= 1000</code></li>
	<li><code>0 &lt;= calls.length &lt;= 1000</code></li>
	<li><code>calls[i]</code> 是 “increment”、“decrement” 和 “reset” 中的一个</li>
</ul>


## 难度

Easy

## 提示

1. You can return an object with methods.
2. Initialize a variable for currentCount. Inside these methods, add the appropriate logic which mutates currentCount.

## 示例

```
5
["increment","reset","decrement"]
0
["increment","increment","decrement","reset","reset"]
```

## 示例代码

### JavaScript

```javascript
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
```

### TypeScript

```typescript
type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): Counter {
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
```

