# 1735. 生成乘积数组的方案数

## 题目描述

<p>给你一个二维整数数组 <code>queries</code> ，其中 <code>queries[i] = [n<sub>i</sub>, k<sub>i</sub>]</code> 。第 <code>i</code> 个查询 <code>queries[i]</code> 要求构造长度为 <code>n<sub>i</sub></code> 、每个元素都是正整数的数组，且满足所有元素的乘积为 <code>k<sub>i</sub></code><sub> </sub>，请你找出有多少种可行的方案。由于答案可能会很大，方案数需要对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 。</p>

<p>请你返回一个整数数组<em> </em><code>answer</code>，满足<em> </em><code>answer.length == queries.length</code> ，其中<em> </em><code>answer[i]</code>是第<em> </em><code>i</code> 个查询的结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>queries = [[2,6],[5,1],[73,660]]
<b>输出：</b>[4,1,50734910]
<b>解释：</b>每个查询之间彼此独立。
[2,6]：总共有 4 种方案得到长度为 2 且乘积为 6 的数组：[1,6]，[2,3]，[3,2]，[6,1]。
[5,1]：总共有 1 种方案得到长度为 5 且乘积为 1 的数组：[1,1,1,1,1]。
[73,660]：总共有 1050734917 种方案得到长度为 73 且乘积为 660 的数组。1050734917 对 10<sup>9</sup> + 7 取余得到 50734910 。
</pre>

<p><strong>示例 2 ：</strong></p>

<pre>
<b>输入：</b>queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
<b>输出：</b>[1,2,3,10,5]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= queries.length <= 10<sup>4</sup> </code></li>
	<li><code>1 <= n<sub>i</sub>, k<sub>i</sub> <= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 动态规划
- 组合数学
- 数论

## 提示

1. Prime-factorize ki and count how many ways you can distribute the primes among the ni positions.
2. After prime factorizing ki, suppose there are x amount of prime factor. There are (x + n - 1) choose (n - 1) ways to distribute the x prime factors into n positions, allowing repetitions.

## 示例

```
[[2,6],[5,1],[73,660]]
[[1,1],[2,2],[3,3],[4,4],[5,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> waysToFillArray(vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] waysToFillArray(int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def waysToFillArray(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* waysToFillArray(int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] WaysToFillArray(int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} queries
 * @return {number[]}
 */
var waysToFillArray = function(queries) {
    
};
```

### TypeScript

```typescript
function waysToFillArray(queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function waysToFillArray($queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func waysToFillArray(_ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun waysToFillArray(queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> waysToFillArray(List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func waysToFillArray(queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} queries
# @return {Integer[]}
def ways_to_fill_array(queries)
    
end
```

### Scala

```scala
object Solution {
    def waysToFillArray(queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ways_to_fill_array(queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (ways-to-fill-array queries)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec ways_to_fill_array(Queries :: [[integer()]]) -> [integer()].
ways_to_fill_array(Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ways_to_fill_array(queries :: [[integer]]) :: [integer]
  def ways_to_fill_array(queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func waysToFillArray(queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

