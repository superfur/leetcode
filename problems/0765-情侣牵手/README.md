# 765. 情侣牵手

## 题目描述

<p><code>n</code> 对情侣坐在连续排列的 <code>2n</code>&nbsp;个座位上，想要牵到对方的手。</p>

<p>人和座位由一个整数数组 <code>row</code> 表示，其中 <code>row[i]</code> 是坐在第 <code>i </code>个座位上的人的 <strong>ID</strong>。情侣们按顺序编号，第一对是&nbsp;<code>(0, 1)</code>，第二对是&nbsp;<code>(2, 3)</code>，以此类推，最后一对是&nbsp;<code>(2n-2, 2n-1)</code>。</p>

<p>返回 <em>最少交换座位的次数，以便每对情侣可以并肩坐在一起</em>。 <i>每次</i>交换可选择任意两人，让他们站起来交换座位。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> row = [0,2,1,3]
<strong>输出:</strong> 1
<strong>解释:</strong> 只需要交换row[1]和row[2]的位置即可。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> row = [3,2,0,1]
<strong>输出:</strong> 0
<strong>解释:</strong> 无需交换座位，所有的情侣都已经可以手牵手了。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>2n == row.length</code></li>
	<li><code>2 &lt;= n &lt;= 30</code></li>
	<li><code>n</code>&nbsp;是偶数</li>
	<li><code>0 &lt;= row[i] &lt; 2n</code></li>
	<li><code>row</code>&nbsp;中所有元素均<strong>无重复</strong></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 深度优先搜索
- 广度优先搜索
- 并查集
- 图

## 提示

1. Say there are N two-seat couches.  For each couple, draw an edge from the couch of one partner to the couch of the other partner.

## 示例

```
[0,2,1,3]
[3,2,0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSwapsCouples(vector<int>& row) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSwapsCouples(int[] row) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        
```

### C

```c
int minSwapsCouples(int* row, int rowSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSwapsCouples(int[] row) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} row
 * @return {number}
 */
var minSwapsCouples = function(row) {
    
};
```

### TypeScript

```typescript
function minSwapsCouples(row: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $row
     * @return Integer
     */
    function minSwapsCouples($row) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSwapsCouples(_ row: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSwapsCouples(row: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSwapsCouples(List<int> row) {
    
  }
}
```

### Go

```golang
func minSwapsCouples(row []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} row
# @return {Integer}
def min_swaps_couples(row)
    
end
```

### Scala

```scala
object Solution {
    def minSwapsCouples(row: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_swaps_couples(row: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-swaps-couples row)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_swaps_couples(Row :: [integer()]) -> integer().
min_swaps_couples(Row) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_swaps_couples(row :: [integer]) :: integer
  def min_swaps_couples(row) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSwapsCouples(row: Array<Int64>): Int64 {

    }
}
```

