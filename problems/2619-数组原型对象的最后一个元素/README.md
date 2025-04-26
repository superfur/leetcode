# 2619. 数组原型对象的最后一个元素

## 题目描述

<p>请你编写一段代码实现一个数组方法，使任何数组都可以调用 <code>array.last()</code> 方法，这个方法将返回数组最后一个元素。如果数组中没有元素，则返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>你可以假设数组是 <code>JSON.parse</code> 的输出结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1 ：</strong></p>

<pre>
<b>输入：</b>nums = [null, {}, 3]
<b>输出：</b>3
<b>解释</b>：调用 nums.last() 后返回最后一个元素： 3。
</pre>

<p><strong>示例 2 ：</strong></p>

<pre>
<b>输入：</b>nums = []
<b>输出：</b>-1
<strong>解释：</strong>因为此数组没有元素，所以应该返回 -1。
</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>arr</code> 是一个有效的 JSON 数组</li>
	<li><code>0 &lt;= arr.length &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 提示

1. Inside the Array.prototype.last function body, you have access to the "this" keyword. "this" is equal to the contents of the array in this case.
2. You can access elements in the array via this[0], this[1], etc. You can also access properties and method like this.length, this.forEach, etc.

## 示例

```
[null, {}, 3]
[]
```

## 示例代码

### JavaScript

```javascript
/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
```

### TypeScript

```typescript
interface Array<T> {
    last(): T | -1;
}

Array.prototype.last = function() {
    
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
```

