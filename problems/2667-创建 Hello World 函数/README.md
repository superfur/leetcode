# 2667. 创建 Hello World 函数

## 题目描述

请你编写一个名为 <code>createHelloWorld</code> 的函数。它应该返回一个新的函数，该函数总是返回 <code>"Hello World"</code>&nbsp;。
<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>args = []
<b>输出：</b>"Hello World"
<strong>解释：</strong>
const f = createHelloWorld();
f(); // "Hello World"

createHelloWorld 返回的函数应始终返回 "Hello World"。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>args = [{},null,42]
<b>输出：</b>"Hello World"
<strong>解释：</strong>
const f = createHelloWorld();
f({}, null, 42); // "Hello World"

可以传递任何参数给函数，但它应始终返回 "Hello World"。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= args.length &lt;= 10</code></li>
</ul>


## 难度

Easy

## 示例

```
[]
[{},null,42]
```

## 示例代码

### JavaScript

```javascript
/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
```

### TypeScript

```typescript
function createHelloWorld() {
    
    return function(...args): string {
        
    };
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
```

