# 1434. 每个人戴不同帽子的方案数

## 题目描述

<p>总共有 <code>n</code>&nbsp;个人和 <code>40</code> 种不同的帽子，帽子编号从 <code>1</code> 到 <code>40</code> 。</p>

<p>给你一个整数列表的列表&nbsp;<code>hats</code>&nbsp;，其中&nbsp;<code>hats[i]</code>&nbsp;是第 <code>i</code>&nbsp;个人所有喜欢帽子的列表。</p>

<p>请你给每个人安排一顶他喜欢的帽子，确保每个人戴的帽子跟别人都不一样，并返回方案数。</p>

<p>由于答案可能很大，请返回它对&nbsp;<code>10^9 + 7</code>&nbsp;取余后的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>hats = [[3,4],[4,5],[5]]
<strong>输出：</strong>1
<strong>解释：</strong>给定条件下只有一种方法选择帽子。
第一个人选择帽子 3，第二个人选择帽子 4，最后一个人选择帽子 5。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>hats = [[3,5,1],[3,5]]
<strong>输出：</strong>4
<strong>解释：</strong>总共有 4 种安排帽子的方法：
(3,5)，(5,3)，(1,3) 和 (1,5)
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
<strong>输出：</strong>24
<strong>解释：</strong>每个人都可以从编号为 1 到 4 的帽子中选。
(1,2,3,4) 4 个帽子的排列方案数为 24 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == hats.length</code></li>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>1 &lt;= hats[i].length &lt;= 40</code></li>
	<li><code>1 &lt;= hats[i][j] &lt;= 40</code></li>
	<li><code>hats[i]</code>&nbsp;包含一个数字互不相同的整数列表。</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划
- 状态压缩

## 提示

1. Dynamic programming + bitmask.
2. dp(peopleMask, idHat) number of ways to wear different hats given a bitmask (people visited) and used hats from 1 to idHat-1.

## 示例

```
[[3,4],[4,5],[5]]
[[3,5,1],[3,5]]
[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberWays(vector<vector<int>>& hats) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberWays(List<List<Integer>> hats) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberWays(self, hats):
        """
        :type hats: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        
```

### C

```c
int numberWays(int** hats, int hatsSize, int* hatsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberWays(IList<IList<int>> hats) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} hats
 * @return {number}
 */
var numberWays = function(hats) {
    
};
```

### TypeScript

```typescript
function numberWays(hats: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $hats
     * @return Integer
     */
    function numberWays($hats) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberWays(_ hats: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberWays(hats: List<List<Int>>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberWays(List<List<int>> hats) {
    
  }
}
```

### Go

```golang
func numberWays(hats [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} hats
# @return {Integer}
def number_ways(hats)
    
end
```

### Scala

```scala
object Solution {
    def numberWays(hats: List[List[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_ways(hats: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-ways hats)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_ways(Hats :: [[integer()]]) -> integer().
number_ways(Hats) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_ways(hats :: [[integer]]) :: integer
  def number_ways(hats) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberWays(hats: ArrayList<ArrayList<Int64>>): Int64 {

    }
}
```

