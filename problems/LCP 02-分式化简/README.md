# LCP 02. 分式化简

## 题目描述

<p>有一个同学在学习分式。他需要将一个连分数化成最简分数，你能帮助他吗？</p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/09/fraction_example_1.jpg" style="height: 195px; width: 480px;"></p>

<p>连分数是形如上图的分式。在本题中，所有系数都是大于等于0的整数。</p>

<p>&nbsp;</p>

<p>输入的<code>cont</code>代表连分数的系数（<code>cont[0]</code>代表上图的<code>a<sub>0</sub></code>，以此类推）。返回一个长度为2的数组<code>[n, m]</code>，使得连分数的值等于<code>n / m</code>，且<code>n, m</code>最大公约数为1。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>cont = [3, 2, 0, 2]
<strong>输出：</strong>[13, 4]
<strong>解释：</strong>原连分数等价于3 + (1 / (2 + (1 / (0 + 1 / 2))))。注意[26, 8], [-13, -4]都不是正确答案。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>cont = [0, 0, 3]
<strong>输出：</strong>[3, 1]
<strong>解释：</strong>如果答案是整数，令分母为1即可。</pre>

<p><strong>限制：</strong></p>

<ol>
	<li><code>cont[i] &gt;= 0</code></li>
	<li><code>1 &lt;= cont的长度 &lt;= 10</code></li>
	<li><code>cont</code>最后一个元素不等于0</li>
	<li>答案的<code>n, m</code>的取值都能被32位int整型存下（即不超过<code>2 ^ 31 - 1</code>）。</li>
</ol>


## 难度

Easy

## 标签

- 数组
- 数学
- 数论
- 模拟

## 示例

```
[3, 2, 0, 2]
[0, 0, 3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> fraction(vector<int>& cont) {

    }
};
```

### Java

```java
class Solution {
    public int[] fraction(int[] cont) {

    }
}
```

### Python

```python
class Solution(object):
    def fraction(self, cont):
        """
        :type cont: List[int]
        :rtype: List[int]
        """
```

### Python3

```python3
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
```

### C

```c


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* fraction(int* cont, int contSize, int* returnSize){

}

```

### JavaScript

```javascript
/**
 * @param {number[]} cont
 * @return {number[]}
 */
var fraction = function(cont) {

};
```

### TypeScript

```typescript
function fraction(cont: number[]): number[] {

};
```

### Go

```golang
func fraction(cont []int) []int {

}
```

