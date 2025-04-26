# 1659. 最大化网格幸福感

## 题目描述

<p>给你四个整数 <code>m</code>、<code>n</code>、<code>introvertsCount</code> 和 <code>extrovertsCount</code> 。有一个 <code>m x n</code> 网格，和两种类型的人：内向的人和外向的人。总共有 <code>introvertsCount</code> 个内向的人和 <code>extrovertsCount</code> 个外向的人。</p>

<p>请你决定网格中应当居住多少人，并为每个人分配一个网格单元。 注意，<strong>不必</strong> 让所有人都生活在网格中。</p>

<p>每个人的 <strong>幸福感</strong> 计算如下：</p>

<ul>
	<li>内向的人 <strong>开始</strong> 时有 <code>120</code> 个幸福感，但每存在一个邻居（内向的或外向的）他都会 <strong>失去</strong>  <code>30</code> 个幸福感。</li>
	<li>外向的人 <strong>开始</strong> 时有 <code>40</code> 个幸福感，每存在一个邻居（内向的或外向的）他都会 <strong>得到</strong>  <code>20</code> 个幸福感。</li>
</ul>

<p>邻居是指居住在一个人所在单元的上、下、左、右四个直接相邻的单元中的其他人。</p>

<p><strong>网格幸福感</strong> 是每个人幸福感的 <strong>总和</strong> 。 返回 <strong>最大可能的网格幸福感</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/15/grid_happiness.png" style="width: 261px; height: 121px;" />
<pre>
<strong>输入：</strong>m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
<strong>输出：</strong>240
<strong>解释：</strong>假设网格坐标 (row, column) 从 1 开始编号。
将内向的人放置在单元 (1,1) ，将外向的人放置在单元 (1,3) 和 (2,3) 。
- 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (0 * 30)（0 位邻居）= 120
- 位于 (1,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
- 位于 (2,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
网格幸福感为：120 + 60 + 60 = 240
上图展示该示例对应网格中每个人的幸福感。内向的人在浅绿色单元中，而外向的人在浅紫色单元中。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
<strong>输出：</strong>260
<strong>解释：</strong>将内向的人放置在单元 (1,1) 和 (3,1) ，将外向的人放置在单元 (2,1) 。
- 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
- 位于 (2,1) 的外向的人的幸福感：40（初始幸福感）+ (2 * 20)（2 位邻居）= 80
- 位于 (3,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
网格幸福感为 90 + 80 + 90 = 260
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
<strong>输出：</strong>240
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= m, n <= 5</code></li>
	<li><code>0 <= introvertsCount, extrovertsCount <= min(m * n, 6)</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 记忆化搜索
- 动态规划
- 状态压缩

## 提示

1. For each cell, it has 3 options, either it is empty, or contains an introvert, or an extrovert.
2. You can do DP where you maintain the state of the previous row, the number of remaining introverts and extroverts, the current row and column, and try the 3 options for each cell.
3. Assume that the previous columns in the current row already belong to the previous row.

## 示例

```
2
3
1
2
3
1
2
1
2
2
4
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
        
    }
};
```

### Java

```java
class Solution {
    public int getMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getMaxGridHappiness(self, m, n, introvertsCount, extrovertsCount):
        """
        :type m: int
        :type n: int
        :type introvertsCount: int
        :type extrovertsCount: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        
```

### C

```c
int getMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number} introvertsCount
 * @param {number} extrovertsCount
 * @return {number}
 */
var getMaxGridHappiness = function(m, n, introvertsCount, extrovertsCount) {
    
};
```

### TypeScript

```typescript
function getMaxGridHappiness(m: number, n: number, introvertsCount: number, extrovertsCount: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer $introvertsCount
     * @param Integer $extrovertsCount
     * @return Integer
     */
    function getMaxGridHappiness($m, $n, $introvertsCount, $extrovertsCount) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getMaxGridHappiness(_ m: Int, _ n: Int, _ introvertsCount: Int, _ extrovertsCount: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMaxGridHappiness(m: Int, n: Int, introvertsCount: Int, extrovertsCount: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
    
  }
}
```

### Go

```golang
func getMaxGridHappiness(m int, n int, introvertsCount int, extrovertsCount int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} m
# @param {Integer} n
# @param {Integer} introverts_count
# @param {Integer} extroverts_count
# @return {Integer}
def get_max_grid_happiness(m, n, introverts_count, extroverts_count)
    
end
```

### Scala

```scala
object Solution {
    def getMaxGridHappiness(m: Int, n: Int, introvertsCount: Int, extrovertsCount: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_max_grid_happiness(m: i32, n: i32, introverts_count: i32, extroverts_count: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-max-grid-happiness m n introvertsCount extrovertsCount)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec get_max_grid_happiness(M :: integer(), N :: integer(), IntrovertsCount :: integer(), ExtrovertsCount :: integer()) -> integer().
get_max_grid_happiness(M, N, IntrovertsCount, ExtrovertsCount) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_max_grid_happiness(m :: integer, n :: integer, introverts_count :: integer, extroverts_count :: integer) :: integer
  def get_max_grid_happiness(m, n, introverts_count, extroverts_count) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getMaxGridHappiness(m: Int64, n: Int64, introvertsCount: Int64, extrovertsCount: Int64): Int64 {

    }
}
```

