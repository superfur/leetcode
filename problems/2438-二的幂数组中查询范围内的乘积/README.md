# 2438. 二的幂数组中查询范围内的乘积

## 题目描述

<p>给你一个正整数&nbsp;<code>n</code>&nbsp;，你需要找到一个下标从&nbsp;<strong>0</strong>&nbsp;开始的数组&nbsp;<code>powers</code>&nbsp;，它包含 <strong>最少</strong>&nbsp;数目的 <code>2</code>&nbsp;的幂，且它们的和为&nbsp;<code>n</code>&nbsp;。<code>powers</code>&nbsp;数组是&nbsp;<strong>非递减</strong>&nbsp;顺序的。根据前面描述，构造&nbsp;<code>powers</code>&nbsp;数组的方法是唯一的。</p>

<p>同时给你一个下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code>queries</code>&nbsp;，其中&nbsp;<code>queries[i] = [left<sub>i</sub>, right<sub>i</sub>]</code>&nbsp;，其中&nbsp;<code>queries[i]</code>&nbsp;表示请你求出满足&nbsp;<code>left<sub>i</sub> &lt;= j &lt;= right<sub>i</sub></code>&nbsp;的所有&nbsp;<code>powers[j]</code>&nbsp;的乘积。</p>

<p>请你返回一个数组<em>&nbsp;</em><code>answers</code>&nbsp;，长度与<em>&nbsp;</em><code>queries</code>&nbsp;的长度相同，其中<em>&nbsp;</em><code>answers[i]</code>是第<em>&nbsp;</em><code>i</code>&nbsp;个查询的答案。由于查询的结果可能非常大，请你将每个&nbsp;<code>answers[i]</code>&nbsp;都对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>n = 15, queries = [[0,1],[2,2],[0,3]]
<b>输出：</b>[2,4,64]
<strong>解释：</strong>
对于 n = 15 ，得到 powers = [1,2,4,8] 。没法得到元素数目更少的数组。
第 1 个查询的答案：powers[0] * powers[1] = 1 * 2 = 2 。
第 2 个查询的答案：powers[2] = 4 。
第 3 个查询的答案：powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64 。
每个答案对 10<sup>9</sup> + 7 得到的结果都相同，所以返回 [2,4,64] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>n = 2, queries = [[0,0]]
<b>输出：</b>[2]
<strong>解释：</strong>
对于 n = 2, powers = [2] 。
唯一一个查询的答案是 powers[0] = 2 。答案对 10<sup>9</sup> + 7 取余后结果相同，所以返回 [2] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt; powers.length</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 前缀和

## 提示

1. The <code>powers</code> array can be created using the binary representation of <code>n</code>.
2. Once <code>powers</code> is formed, the products can be taken using brute force.

## 示例

```
15
[[0,1],[2,2],[0,3]]
2
[[0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] productQueries(int n, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ProductQueries(int n, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var productQueries = function(n, queries) {
    
};
```

### TypeScript

```typescript
function productQueries(n: number, queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function productQueries($n, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func productQueries(_ n: Int, _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun productQueries(n: Int, queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> productQueries(int n, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func productQueries(n int, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def product_queries(n, queries)
    
end
```

### Scala

```scala
object Solution {
    def productQueries(n: Int, queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn product_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (product-queries n queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec product_queries(N :: integer(), Queries :: [[integer()]]) -> [integer()].
product_queries(N, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec product_queries(n :: integer, queries :: [[integer]]) :: [integer]
  def product_queries(n, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func productQueries(n: Int64, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

