# 2555. 两个线段获得的最多奖品

## 题目描述

<p>在 <strong>X轴</strong>&nbsp;上有一些奖品。给你一个整数数组&nbsp;<code>prizePositions</code>&nbsp;，它按照 <strong>非递减</strong>&nbsp;顺序排列，其中&nbsp;<code>prizePositions[i]</code>&nbsp;是第&nbsp;<code>i</code>&nbsp;件奖品的位置。数轴上一个位置可能会有多件奖品。再给你一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>你可以同时选择两个端点为整数的线段。每个线段的长度都必须是 <code>k</code>&nbsp;。你可以获得位置在任一线段上的所有奖品（包括线段的两个端点）。注意，两个线段可能会有相交。</p>

<ul>
	<li>比方说&nbsp;<code>k = 2</code>&nbsp;，你可以选择线段&nbsp;<code>[1, 3]</code> 和&nbsp;<code>[2, 4]</code>&nbsp;，你可以获得满足&nbsp;<code>1 &lt;= prizePositions[i] &lt;= 3</code> 或者&nbsp;<code>2 &lt;= prizePositions[i] &lt;= 4</code>&nbsp;的所有奖品 i 。</li>
</ul>

<p>请你返回在选择两个最优线段的前提下，可以获得的 <strong>最多</strong>&nbsp;奖品数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>prizePositions = [1,1,2,2,3,3,5], k = 2
<b>输出：</b>7
<b>解释：</b>这个例子中，你可以选择线段 [1, 3] 和 [3, 5] ，获得 7 个奖品。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>prizePositions = [1,2,3,4], k = 0
<b>输出：</b>2
<b>解释：</b>这个例子中，一个选择是选择线段 <code>[3, 3]</code> 和 <code>[4, 4]</code> ，获得 2 个奖品。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= prizePositions.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= prizePositions[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>9</sup> </code></li>
	<li><code>prizePositions</code>&nbsp;有序非递减。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 滑动窗口

## 提示

1. Try solving the problem for one interval.
2. Using the solution with one interval, how can you combine that with a second interval?

## 示例

```
[1,1,2,2,3,3,5]
2
[1,2,3,4]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximizeWin(vector<int>& prizePositions, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximizeWin(int[] prizePositions, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximizeWin(self, prizePositions, k):
        """
        :type prizePositions: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        
```

### C

```c
int maximizeWin(int* prizePositions, int prizePositionsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximizeWin(int[] prizePositions, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} prizePositions
 * @param {number} k
 * @return {number}
 */
var maximizeWin = function(prizePositions, k) {
    
};
```

### TypeScript

```typescript
function maximizeWin(prizePositions: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $prizePositions
     * @param Integer $k
     * @return Integer
     */
    function maximizeWin($prizePositions, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximizeWin(_ prizePositions: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximizeWin(prizePositions: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximizeWin(List<int> prizePositions, int k) {
    
  }
}
```

### Go

```golang
func maximizeWin(prizePositions []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} prize_positions
# @param {Integer} k
# @return {Integer}
def maximize_win(prize_positions, k)
    
end
```

### Scala

```scala
object Solution {
    def maximizeWin(prizePositions: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximize_win(prize_positions: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximize-win prizePositions k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximize_win(PrizePositions :: [integer()], K :: integer()) -> integer().
maximize_win(PrizePositions, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximize_win(prize_positions :: [integer], k :: integer) :: integer
  def maximize_win(prize_positions, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximizeWin(prizePositions: Array<Int64>, k: Int64): Int64 {

    }
}
```

