# 1824. 最少侧跳次数

## 题目描述

<p>给你一个长度为 <code>n</code> 的 <strong>3 跑道道路</strong> ，它总共包含 <code>n + 1</code> 个 <strong>点</strong> ，编号为 <code>0</code> 到 <code>n</code> 。一只青蛙从 <code>0</code> 号点第二条跑道 <strong>出发</strong> ，它想要跳到点 <code>n</code> 处。然而道路上可能有一些障碍。</p>

<p>给你一个长度为 <code>n + 1</code> 的数组 <code>obstacles</code> ，其中 <code>obstacles[i]</code> （<b>取值范围从 0 到 3</b>）表示在点 <code>i</code> 处的 <code>obstacles[i]</code> 跑道上有一个障碍。如果 <code>obstacles[i] == 0</code> ，那么点 <code>i</code> 处没有障碍。任何一个点的三条跑道中 <strong>最多有一个</strong> 障碍。</p>

<ul>
	<li>比方说，如果 <code>obstacles[2] == 1</code> ，那么说明在点 2 处跑道 1 有障碍。</li>
</ul>

<p>这只青蛙从点 <code>i</code> 跳到点 <code>i + 1</code> 且跑道不变的前提是点 <code>i + 1</code> 的同一跑道上没有障碍。为了躲避障碍，这只青蛙也可以在 <strong>同一个</strong> 点处 <strong>侧跳</strong> 到 <strong>另外一条</strong> 跑道（这两条跑道可以不相邻），但前提是跳过去的跑道该点处没有障碍。</p>

<ul>
	<li>比方说，这只青蛙可以从点 3 处的跑道 3 跳到点 3 处的跑道 1 。</li>
</ul>

<p>这只青蛙从点 0 处跑道 <code>2</code> 出发，并想到达点 <code>n</code> 处的 <strong>任一跑道</strong> ，请你返回 <strong>最少侧跳次数</strong> 。</p>

<p><strong>注意</strong>：点 <code>0</code> 处和点 <code>n</code> 处的任一跑道都不会有障碍。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/ic234-q3-ex1.png" style="width: 500px; height: 244px;" />
<pre>
<b>输入：</b>obstacles = [0,1,2,3,0]
<b>输出：</b>2 
<b>解释：</b>最优方案如上图箭头所示。总共有 2 次侧跳（红色箭头）。
注意，这只青蛙只有当侧跳时才可以跳过障碍（如上图点 2 处所示）。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/ic234-q3-ex2.png" style="width: 500px; height: 196px;" />
<pre>
<b>输入：</b>obstacles = [0,1,1,3,3,0]
<b>输出：</b>0
<b>解释：</b>跑道 2 没有任何障碍，所以不需要任何侧跳。
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/ic234-q3-ex3.png" style="width: 500px; height: 196px;" />
<pre>
<b>输入：</b>obstacles = [0,2,1,0,3,0]
<b>输出：</b>2
<b>解释：</b>最优方案如上图所示。总共有 2 次侧跳。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>obstacles.length == n + 1</code></li>
	<li><code>1 <= n <= 5 * 10<sup>5</sup></code></li>
	<li><code>0 <= obstacles[i] <= 3</code></li>
	<li><code>obstacles[0] == obstacles[n] == 0</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 动态规划

## 提示

1. At a given point, there are only 3 possible states for where the frog can be.
2. Check all the ways to move from one point to the next and update the minimum side jumps for each lane.

## 示例

```
[0,1,2,3,0]
[0,1,1,3,3,0]
[0,2,1,0,3,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSideJumps(vector<int>& obstacles) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSideJumps(int[] obstacles) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        
```

### C

```c
int minSideJumps(int* obstacles, int obstaclesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSideJumps(int[] obstacles) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} obstacles
 * @return {number}
 */
var minSideJumps = function(obstacles) {
    
};
```

### TypeScript

```typescript
function minSideJumps(obstacles: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $obstacles
     * @return Integer
     */
    function minSideJumps($obstacles) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSideJumps(_ obstacles: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSideJumps(obstacles: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSideJumps(List<int> obstacles) {
    
  }
}
```

### Go

```golang
func minSideJumps(obstacles []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} obstacles
# @return {Integer}
def min_side_jumps(obstacles)
    
end
```

### Scala

```scala
object Solution {
    def minSideJumps(obstacles: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_side_jumps(obstacles: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-side-jumps obstacles)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_side_jumps(Obstacles :: [integer()]) -> integer().
min_side_jumps(Obstacles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_side_jumps(obstacles :: [integer]) :: integer
  def min_side_jumps(obstacles) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSideJumps(obstacles: Array<Int64>): Int64 {

    }
}
```

