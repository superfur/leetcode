# 2626. 数组归约运算

## 题目描述

<p>给定一个整数数组 <code>nums</code>、一个 reducer 函数 <code>fn</code> 和一个初始值 <code>init</code>，返回通过依次对数组的每个元素执行 <code>fn</code> 函数得到的最终结果。</p>

<p>通过以下操作实现这个结果：<code>val = fn(init, nums[0])，val = fn(val, nums[1])，val = fn(val, nums[2])，...</code> 直到处理数组中的每个元素。然后返回 <code>val</code> 的最终值。</p>

<p>如果数组的长度为 0，则函数应返回 <code>init</code>。</p>

<p>请你在不使用内置数组方法的&nbsp;<code>Array.reduce</code>&nbsp;前提下解决这个问题。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>
nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr; }
init = 0
<strong>输出：</strong>10
<strong>解释：</strong>
初始值为 init=0 。
(0) + nums[0] = 1
(1) + nums[1] = 3
(3) + nums[2] = 6
(6) + nums[3] = 10
Val 最终值为 10。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong> 
nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr * curr; }
init = 100
<strong>输出：</strong>130
<strong>解释：</strong>
初始值为 init=100 。
(100) + nums[0]^2 = 101
(101) + nums[1]^2 = 105
(105) + nums[2]^2 = 114
(114) + nums[3]^2 = 130
Val 最终值为 130。
</pre>

<p><strong class="example">示例3:</strong></p>

<pre>
<strong>输入：</strong> 
nums = []
fn = function sum(accum, curr) { return 0; }
init = 25
<strong>输出：</strong>25
<b>解释：</b>这是一个空数组，所以返回 init 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= init &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 提示

1. Declare a variable "res" and set it it equal to the initial value.
2. Loop over each value in the array and set "res" = fn(res, arr[i]).

## 示例

```
[1,2,3,4]
function sum(accum, curr) { return accum + curr; }
0
[1,2,3,4]
function sum(accum, curr) { return accum + curr * curr; }
100
[]
function sum(accum, curr) { return 0; }
25
```

## 示例代码

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    
};
```

### TypeScript

```typescript
type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    
};
```

