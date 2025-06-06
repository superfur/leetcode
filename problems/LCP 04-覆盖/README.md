# LCP 04. 覆盖

## 题目描述

<p>你有一块棋盘，棋盘上有一些格子已经坏掉了。你还有无穷块大小为<code>1 * 2</code>的多米诺骨牌，你想把这些骨牌<strong>不重叠</strong>地覆盖在<strong>完好</strong>的格子上，请找出你最多能在棋盘上放多少块骨牌？这些骨牌可以横着或者竖着放。</p>

<p>&nbsp;</p>

<p>输入：<code>n, m</code>代表棋盘的大小；<code>broken</code>是一个<code>b * 2</code>的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。</p>

<p>输出：一个整数，代表最多能在棋盘上放的骨牌数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 2, m = 3, broken = [[1, 0], [1, 1]]
<strong>输出：</strong>2
<strong>解释：</strong>我们最多可以放两块骨牌：[[0, 0], [0, 1]]以及[[0, 2], [1, 2]]。（见下图）</pre>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/09/domino_example_1.jpg" style="height: 204px; width: 304px;"></p>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 3, m = 3, broken = []
<strong>输出：</strong>4
<strong>解释：</strong>下图是其中一种可行的摆放方式
</pre>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/09/domino_example_2.jpg" style="height: 304px; width: 304px;"></p>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ol>
	<li><code>1 &lt;= n &lt;= 8</code></li>
	<li><code>1 &lt;= m &lt;= 8</code></li>
	<li><code>0 &lt;= b &lt;= n * m</code></li>
</ol>


## 难度

Hard

## 标签

- 位运算
- 图
- 数组
- 动态规划
- 状态压缩

## 示例

```
2
3
[[1, 0], [1, 1]]
3
3
[]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int domino(int n, int m, vector<vector<int>>& broken) {

    }
};
```

### Java

```java
class Solution {
    public int domino(int n, int m, int[][] broken) {

    }
}
```

### Python

```python
class Solution(object):
    def domino(self, n, m, broken):
        """
        :type n: int
        :type m: int
        :type broken: List[List[int]]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
```

### C

```c


int domino(int n, int m, int** broken, int brokenSize, int* brokenColSize){

}

```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @param {number[][]} broken
 * @return {number}
 */
var domino = function(n, m, broken) {

};
```

### TypeScript

```typescript
function domino(n: number, m: number, broken: number[][]): number {

};
```

### Go

```golang
func domino(n int, m int, broken [][]int) int {

}
```

