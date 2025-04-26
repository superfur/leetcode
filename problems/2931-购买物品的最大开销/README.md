# 2931. 购买物品的最大开销

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始大小为&nbsp;<code>m * n</code>&nbsp;的整数矩阵&nbsp;<code>values</code>&nbsp;，表示&nbsp;<code>m</code>&nbsp;个不同商店里&nbsp;<code>m * n</code>&nbsp;件不同的物品。每个商店有 <code>n</code>&nbsp;件物品，第&nbsp;<code>i</code>&nbsp;个商店的第 <code>j</code>&nbsp;件物品的价值为&nbsp;<code>values[i][j]</code>&nbsp;。除此以外，第&nbsp;<code>i</code>&nbsp;个商店的物品已经按照价值非递增排好序了，也就是说对于所有&nbsp;<code>0 &lt;= j &lt; n - 1</code>&nbsp;都有&nbsp;<code>values[i][j] &gt;= values[i][j + 1]</code>&nbsp;。</p>

<p>每一天，你可以在一个商店里购买一件物品。具体来说，在第&nbsp;<code>d</code>&nbsp;天，你可以：</p>

<ul>
	<li>选择商店&nbsp;<code>i</code>&nbsp;。</li>
	<li>购买数组中最右边的物品&nbsp;<code>j</code>&nbsp;，开销为&nbsp;<code>values[i][j] * d</code>&nbsp;。换句话说，选择该商店中还没购买过的物品中最大的下标&nbsp;<code>j</code>&nbsp;，并且花费&nbsp;<code>values[i][j] * d</code>&nbsp;去购买。</li>
</ul>

<p><strong>注意</strong>，所有物品都视为不同的物品。比方说如果你已经从商店 <code>1</code>&nbsp;购买了物品&nbsp;<code>0</code>&nbsp;，你还可以在别的商店里购买其他商店的物品&nbsp;<code>0</code>&nbsp;。</p>

<p>请你返回购买所有 <code>m * n</code>&nbsp;件物品需要的 <strong>最大开销</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>values = [[8,5,2],[6,4,1],[9,7,3]]
<b>输出：</b>285
<b>解释：</b>第一天，从商店 1 购买物品 2 ，开销为 values[1][2] * 1 = 1 。
第二天，从商店 0 购买物品 2 ，开销为 values[0][2] * 2 = 4 。
第三天，从商店 2 购买物品 2 ，开销为 values[2][2] * 3 = 9 。
第四天，从商店 1 购买物品 1 ，开销为 values[1][1] * 4 = 16 。
第五天，从商店 0 购买物品 1 ，开销为 values[0][1] * 5 = 25 。
第六天，从商店 1 购买物品 0 ，开销为 values[1][0] * 6 = 36 。
第七天，从商店 2 购买物品 1 ，开销为 values[2][1] * 7 = 49 。
第八天，从商店 0 购买物品 0 ，开销为 values[0][0] * 8 = 64 。
第九天，从商店 2 购买物品 0 ，开销为 values[2][0] * 9 = 81 。
所以总开销为 285 。
285 是购买所有 m * n 件物品的最大总开销。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>values = [[10,8,6,4,2],[9,7,5,3,2]]
<b>输出：</b>386
<b>解释：</b>第一天，从商店 0 购买物品 4 ，开销为 values[0][4] * 1 = 2 。
第二天，从商店 1 购买物品 4 ，开销为 values[1][4] * 2 = 4 。
第三天，从商店 1 购买物品 3 ，开销为 values[1][3] * 3 = 9 。
第四天，从商店 0 购买物品 3 ，开销为 values[0][3] * 4 = 16 。
第五天，从商店 1 购买物品 2 ，开销为 values[1][2] * 5 = 25 。
第六天，从商店 0 购买物品 2 ，开销为 values[0][2] * 6 = 36 。
第七天，从商店 1 购买物品 1 ，开销为 values[1][1] * 7 = 49 。
第八天，从商店 0 购买物品 1 ，开销为 values[0][1] * 8 = 64 。
第九天，从商店 1 购买物品 0 ，开销为 values[1][0] * 9 = 81 。
第十天，从商店 0 购买物品 0 ，开销为 values[0][0] * 10 = 100 。
所以总开销为 386 。
386 是购买所有 m * n 件物品的最大总开销。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= m == values.length &lt;= 10</code></li>
	<li><code>1 &lt;= n == values[i].length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= values[i][j] &lt;= 10<sup>6</sup></code></li>
	<li><code>values[i]</code>&nbsp;按照非递增顺序排序。</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 矩阵
- 排序
- 堆（优先队列）

## 提示

1. Iterate on days <code>1</code> to <code>m * n</code>.
2. On each day, buy the product that minimizes <code>values[i][values[i].length - 1]</code>, and pop it from <code>values[i]</code>.

## 示例

```
[[8,5,2],[6,4,1],[9,7,3]]
[[10,8,6,4,2],[9,7,5,3,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxSpending(vector<vector<int>>& values) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxSpending(int[][] values) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSpending(self, values):
        """
        :type values: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        
```

### C

```c
long long maxSpending(int** values, int valuesSize, int* valuesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxSpending(int[][] values) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} values
 * @return {number}
 */
var maxSpending = function(values) {
    
};
```

### TypeScript

```typescript
function maxSpending(values: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $values
     * @return Integer
     */
    function maxSpending($values) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSpending(_ values: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSpending(values: Array<IntArray>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSpending(List<List<int>> values) {
    
  }
}
```

### Go

```golang
func maxSpending(values [][]int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} values
# @return {Integer}
def max_spending(values)
    
end
```

### Scala

```scala
object Solution {
    def maxSpending(values: Array[Array[Int]]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_spending(values: Vec<Vec<i32>>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-spending values)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_spending(Values :: [[integer()]]) -> integer().
max_spending(Values) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_spending(values :: [[integer]]) :: integer
  def max_spending(values) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSpending(values: Array<Array<Int64>>): Int64 {

    }
}
```

