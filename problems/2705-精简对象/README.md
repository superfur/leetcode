# 2705. 精简对象

## 题目描述

<p>现给定一个对象或数组 <code>obj</code>，返回一个 <strong>精简对象</strong> 。</p>

<p><strong>精简对象</strong> 与原始对象相同，只是将包含 <strong>假</strong> 值的键移除。该操作适用于对象及其嵌套对象。数组被视为索引作为键的对象。当 <code>Boolean(value)</code> 返回 <code>false</code> 时，值被视为 <strong>假</strong> 值。</p>

<p>你可以假设 <code>obj</code> 是 <code>JSON.parse</code> 的输出结果。换句话说，它是有效的 JSON。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>obj = [null, 0, false, 1]
<b>输出：</b>[1]
<b>解释：</b>数组中的所有假值已被移除。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>obj = {"a": null, "b": [false, 1]}
<b>输出：</b>{"b": [1]}
<b>解释：</b>obj["a"] 和 obj["b"][0] 包含假值，因此被移除。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>obj = [null, 0, 5, [0], [false, 16]]
<b>输出：</b>[5, [], [16]]
<b>解释：</b>obj[0], obj[1], obj[3][0], 和 obj[4][0] 包含假值，因此被移除。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>obj</code> 是一个有效的 JSON 对象</li>
	<li><code>2 &lt;= JSON.stringify(obj).length &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 示例

```
[null, 0, false, 1]
{"a": null, "b": [false, 1]}
[null, 0, 5, [0], [false, 16]]
```

## 示例代码

### JavaScript

```javascript
/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    
};
```

### TypeScript

```typescript
type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function compactObject(obj: Obj): Obj {
    
};
```

