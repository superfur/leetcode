# 3017. 按距离统计房屋对数目 II

## 题目描述

<p>给你三个<strong> 正整数 </strong><code>n</code> 、<code>x</code> 和 <code>y</code> 。</p>

<p>在城市中，存在编号从 <code>1</code> 到 <code>n</code> 的房屋，由 <code>n</code> 条街道相连。对所有 <code>1 &lt;= i &lt; n</code> ，都存在一条街道连接编号为 <code>i</code> 的房屋与编号为 <code>i + 1</code> 的房屋。另存在一条街道连接编号为 <code>x</code> 的房屋与编号为 <code>y</code> 的房屋。</p>

<p>对于每个 <code>k</code>（<code>1 &lt;= k &lt;= n</code>），你需要找出所有满足要求的 <strong>房屋对 </strong><code>[house<sub>1</sub>, house<sub>2</sub>]</code> ，即从 <code>house<sub>1</sub></code> 到 <code>house<sub>2</sub></code> 需要经过的<strong> 最少</strong> 街道数为 <code>k</code> 。</p>

<p>返回一个下标从 <strong>1</strong> 开始且长度为 <code>n</code> 的数组 <code>result</code> ，其中 <code>result[k]</code> 表示所有满足要求的房屋对的数量，即从一个房屋到另一个房屋需要经过的<strong> 最少 </strong>街道数为 <code>k</code> 。</p>

<p><strong>注意</strong>，<code>x</code> 与 <code>y</code> 可以 <strong>相等 </strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/20/example2.png" style="width: 474px; height: 197px;" />
<pre>
<strong>输入：</strong>n = 3, x = 1, y = 3
<strong>输出：</strong>[6,0,0]
<strong>解释：</strong>让我们检视每个房屋对
- 对于房屋对 (1, 2)，可以直接从房屋 1 到房屋 2。
- 对于房屋对 (2, 1)，可以直接从房屋 2 到房屋 1。
- 对于房屋对 (1, 3)，可以直接从房屋 1 到房屋 3。
- 对于房屋对 (3, 1)，可以直接从房屋 3 到房屋 1。
- 对于房屋对 (2, 3)，可以直接从房屋 2 到房屋 3。
- 对于房屋对 (3, 2)，可以直接从房屋 3 到房屋 2。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/20/example3.png" style="width: 668px; height: 174px;" />
<pre>
<strong>输入：</strong>n = 5, x = 2, y = 4
<strong>输出：</strong>[10,8,2,0,0]
<strong>解释：</strong>对于每个距离 k ，满足要求的房屋对如下：
- 对于 k == 1，满足要求的房屋对有 (1, 2), (2, 1), (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3), (4, 5), 以及 (5, 4)。
- 对于 k == 2，满足要求的房屋对有 (1, 3), (3, 1), (1, 4), (4, 1), (2, 5), (5, 2), (3, 5), 以及 (5, 3)。
- 对于 k == 3，满足要求的房屋对有 (1, 5)，以及 (5, 1) 。
- 对于 k == 4 和 k == 5，不存在满足要求的房屋对。
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/20/example5.png" style="width: 544px; height: 130px;" />
<pre>
<strong>输入：</strong>n = 4, x = 1, y = 1
<strong>输出：</strong>[6,4,2,0]
<strong>解释：</strong>对于每个距离 k ，满足要求的房屋对如下：
- 对于 k == 1，满足要求的房屋对有 (1, 2), (2, 1), (2, 3), (3, 2), (3, 4), 以及 (4, 3)。
- 对于 k == 2，满足要求的房屋对有 (1, 3), (3, 1), (2, 4), 以及 (4, 2)。
- 对于 k == 3，满足要求的房屋对有 (1, 4), 以及 (4, 1)。
- 对于 k == 4，不存在满足要求的房屋对。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= x, y &lt;= n</code></li>
</ul>


## 难度

Hard

## 标签

- 图
- 前缀和

## 提示

1. If there were no additional street connecting house <code>x</code> to house <code>y</code>, there would be <code>2 * (n - i)</code> pairs of houses at distance <code>i</code>.
2. The shortest distance between house <code>i</code> and house <code>j</code> (<code>j < i</code>) is along one of these paths:
- <code>i -> j</code>
- <code>i -> y---x -> j</code>
3. Try to change the distances calculated by path <code>i ->j</code> to the other path.
4. Can we use prefix sums to compute the answer?

## 示例

```
3
1
3
5
2
4
4
1
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> countOfPairs(int n, int x, int y) {
        
    }
};
```

### Java

```java
class Solution {
    public long[] countOfPairs(int n, int x, int y) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countOfPairs(self, n, x, y):
        """
        :type n: int
        :type x: int
        :type y: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* countOfPairs(int n, int x, int y, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long[] CountOfPairs(int n, int x, int y) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} x
 * @param {number} y
 * @return {number[]}
 */
var countOfPairs = function(n, x, y) {
    
};
```

### TypeScript

```typescript
function countOfPairs(n: number, x: number, y: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $x
     * @param Integer $y
     * @return Integer[]
     */
    function countOfPairs($n, $x, $y) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countOfPairs(_ n: Int, _ x: Int, _ y: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countOfPairs(n: Int, x: Int, y: Int): LongArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> countOfPairs(int n, int x, int y) {
    
  }
}
```

### Go

```golang
func countOfPairs(n int, x int, y int) []int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} x
# @param {Integer} y
# @return {Integer[]}
def count_of_pairs(n, x, y)
    
end
```

### Scala

```scala
object Solution {
    def countOfPairs(n: Int, x: Int, y: Int): Array[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_of_pairs(n: i32, x: i32, y: i32) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (count-of-pairs n x y)
  (-> exact-integer? exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec count_of_pairs(N :: integer(), X :: integer(), Y :: integer()) -> [integer()].
count_of_pairs(N, X, Y) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_of_pairs(n :: integer, x :: integer, y :: integer) :: [integer]
  def count_of_pairs(n, x, y) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countOfPairs(n: Int64, x: Int64, y: Int64): Array<Int64> {

    }
}
```

