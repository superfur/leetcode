# 2703. 返回传递的参数的长度

## 题目描述

请你编写一个函数 <code>argumentsLength</code>，返回传递给该函数的参数数量。
<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>args = [5]
<b>输出：</b>1
<strong>解释：</strong>
argumentsLength(5); // 1

只传递了一个值给函数，因此它应返回 1。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>args = [{}, null, "3"]
<b>输出：</b>3
<b>解释：</b>
argumentsLength({}, null, "3"); // 3

传递了三个值给函数，因此它应返回 3。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>args</code>&nbsp;是一个有效的 JSON 数组</li>
	<li><code>0 &lt;= args.length &lt;= 100</code></li>
</ul>


## 难度

Easy

## 示例

```
[5]
[{},null,"3"]
```

## 示例代码

### JavaScript

```javascript
/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
```

### TypeScript

```typescript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function argumentsLength(...args: JSONValue[]): number {
    
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
```

