# 1386. 安排电影院座位

## 题目描述

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/21/cinema_seats_1.png" style="height: 149px; width: 400px;" /></p>

<p>如上图所示，电影院的观影厅中有 <code>n</code>&nbsp;行座位，行编号从 1&nbsp;到 <code>n</code>&nbsp;，且每一行内总共有 10 个座位，列编号从 1 到 10 。</p>

<p>给你数组&nbsp;<code>reservedSeats</code>&nbsp;，包含所有已经被预约了的座位。比如说，<code>reservedSeats[i]=[3,8]</code>&nbsp;，它表示第&nbsp;<strong>3</strong>&nbsp;行第&nbsp;<strong>8</strong>&nbsp;个座位被预约了。</p>

<p>请你返回&nbsp;<strong>最多能安排多少个 4 人家庭</strong>&nbsp;。4 人家庭要占据&nbsp;<strong>同一行内连续&nbsp;</strong>的 4 个座位。隔着过道的座位（比方说 [3,3] 和 [3,4]）不是连续的座位，但是如果你可以将 4 人家庭拆成过道两边各坐 2 人，这样子是允许的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/21/cinema_seats_3.png" style="height: 96px; width: 400px;" /></p>

<pre>
<strong>输入：</strong>n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
<strong>输出：</strong>4
<strong>解释：</strong>上图所示是最优的安排方案，总共可以安排 4 个家庭。蓝色的叉表示被预约的座位，橙色的连续座位表示一个 4 人家庭。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^9</code></li>
	<li><code>1 &lt;=&nbsp;reservedSeats.length &lt;= min(10*n, 10^4)</code></li>
	<li><code>reservedSeats[i].length == 2</code></li>
	<li><code>1&nbsp;&lt;=&nbsp;reservedSeats[i][0] &lt;= n</code></li>
	<li><code>1 &lt;=&nbsp;reservedSeats[i][1] &lt;= 10</code></li>
	<li>所有&nbsp;<code>reservedSeats[i]</code> 都是互不相同的。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 位运算
- 数组
- 哈希表

## 提示

1. Note you can allocate at most two families in one row.
2. Greedily check if you can allocate seats for two families, one family or none.
3. Process only rows that appear in the input, for other rows you can always allocate seats for two families.

## 示例

```
3
[[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
2
[[2,1],[1,8],[2,6]]
4
[[4,3],[1,4],[4,6],[1,7]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
```

### C

```c
int maxNumberOfFamilies(int n, int** reservedSeats, int reservedSeatsSize, int* reservedSeatsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxNumberOfFamilies(int n, int[][] reservedSeats) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} reservedSeats
 * @return {number}
 */
var maxNumberOfFamilies = function(n, reservedSeats) {
    
};
```

### TypeScript

```typescript
function maxNumberOfFamilies(n: number, reservedSeats: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $reservedSeats
     * @return Integer
     */
    function maxNumberOfFamilies($n, $reservedSeats) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxNumberOfFamilies(_ n: Int, _ reservedSeats: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxNumberOfFamilies(n: Int, reservedSeats: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxNumberOfFamilies(int n, List<List<int>> reservedSeats) {
    
  }
}
```

### Go

```golang
func maxNumberOfFamilies(n int, reservedSeats [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} reserved_seats
# @return {Integer}
def max_number_of_families(n, reserved_seats)
    
end
```

### Scala

```scala
object Solution {
    def maxNumberOfFamilies(n: Int, reservedSeats: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_number_of_families(n: i32, reserved_seats: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-number-of-families n reservedSeats)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_number_of_families(N :: integer(), ReservedSeats :: [[integer()]]) -> integer().
max_number_of_families(N, ReservedSeats) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_number_of_families(n :: integer, reserved_seats :: [[integer]]) :: integer
  def max_number_of_families(n, reserved_seats) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxNumberOfFamilies(n: Int64, reservedSeats: Array<Array<Int64>>): Int64 {

    }
}
```

