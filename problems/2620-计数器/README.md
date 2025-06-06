# 2620. 计数器

## 题目描述

<p>给定一个整型参数 <code>n</code>，请你编写并返回一个 <code>counter</code><strong>&nbsp;</strong>函数。这个&nbsp;<code>counter</code><strong>&nbsp;</strong>函数最初返回 <code>n</code>，每次调用它时会返回前一个值加 1 的值 ( <code>n</code> ,&nbsp; <code>n + 1</code> ,&nbsp; <code>n + 2</code> ，等等)。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
n = 10 
["call","call","call"]
<strong>输出：</strong>[10,11,12]
<strong>解释：</strong>
counter() = 10 // 第一次调用 counter()，返回 n。
counter() = 11 // 返回上次调用的值加 1。
counter() = 12 // 返回上次调用的值加 1。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>
n = -2
["call","call","call","call","call"]
<strong>输出：</strong>[-2,-1,0,1,2]
<strong>解释：</strong>counter() 最初返回 -2。然后在每个后续调用后增加 1。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-1000<sup>&nbsp;</sup>&lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= calls.length &lt;= 1000</code></li>
	<li><code>calls[i] === "call"</code></li>
</ul>


## 难度

Easy

## 提示

1. In JavaScript, a function can return a closure. A closure is defined as a function and the variables declared around it (it's lexical environment).
2. A count variable can be initialized in the outer function and mutated in the inner function.

## 示例

```
10
["call","call","call"]
-2
["call","call","call","call","call"]
```

## 示例代码

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    
    return function() {
        
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
```

### TypeScript

```typescript
function createCounter(n: number): () => number {
    
    return function() {
        
    }
}


/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
```

