# 1642. 可以到达的最远建筑

## 题目描述

<p>给你一个整数数组 <code>heights</code> ，表示建筑物的高度。另有一些砖块 <code>bricks</code> 和梯子 <code>ladders</code> 。</p>

<p>你从建筑物 <code>0</code> 开始旅程，不断向后面的建筑物移动，期间可能会用到砖块或梯子。</p>

<p>当从建筑物 <code>i</code> 移动到建筑物 <code>i+1</code>（下标<strong> 从 0 开始 </strong>）时：</p>

<ul>
	<li>如果当前建筑物的高度 <strong>大于或等于</strong> 下一建筑物的高度，则不需要梯子或砖块</li>
	<li>如果当前建筑的高度 <strong>小于</strong> 下一个建筑的高度，您可以使用 <strong>一架梯子</strong> 或 <strong><code>(h[i+1] - h[i])</code> 个砖块</strong></li>
</ul>
如果以最佳方式使用给定的梯子和砖块，返回你可以到达的最远建筑物的下标（下标<strong> 从 0 开始 </strong>）。

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/31/q4.gif" style="width: 562px; height: 561px;" />
<pre>
<strong>输入：</strong>heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
<strong>输出：</strong>4
<strong>解释：</strong>从建筑物 0 出发，你可以按此方案完成旅程：
- 不使用砖块或梯子到达建筑物 1 ，因为 4 >= 2
- 使用 5 个砖块到达建筑物 2 。你必须使用砖块或梯子，因为 2 < 7
- 不使用砖块或梯子到达建筑物 3 ，因为 7 >= 6
- 使用唯一的梯子到达建筑物 4 。你必须使用砖块或梯子，因为 6 < 9
无法越过建筑物 4 ，因为没有更多砖块或梯子。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
<strong>输出：</strong>7
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>heights = [14,3,19,3], bricks = 17, ladders = 0
<strong>输出：</strong>3
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= heights.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= heights[i] <= 10<sup>6</sup></code></li>
	<li><code>0 <= bricks <= 10<sup>9</sup></code></li>
	<li><code>0 <= ladders <= heights.length</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 堆（优先队列）

## 提示

1. Assume the problem is to check whether you can reach the last building or not.
2. You'll have to do a set of jumps, and choose for each one whether to do it using a ladder or bricks. It's always optimal to use ladders in the largest jumps.
3. Iterate on the buildings, maintaining the largest r jumps and the sum of the remaining ones so far, and stop whenever this sum exceeds b.

## 示例

```
[4,2,7,6,9,14,12]
5
1
[4,12,2,7,3,18,20,3,19]
10
2
[14,3,19,3]
17
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        
    }
};
```

### Java

```java
class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        
    }
}
```

### Python

```python
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
```

### C

```c
int furthestBuilding(int* heights, int heightsSize, int bricks, int ladders) {
    
}
```

### C#

```csharp
public class Solution {
    public int FurthestBuilding(int[] heights, int bricks, int ladders) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} heights
 * @param {number} bricks
 * @param {number} ladders
 * @return {number}
 */
var furthestBuilding = function(heights, bricks, ladders) {
    
};
```

### TypeScript

```typescript
function furthestBuilding(heights: number[], bricks: number, ladders: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $heights
     * @param Integer $bricks
     * @param Integer $ladders
     * @return Integer
     */
    function furthestBuilding($heights, $bricks, $ladders) {
        
    }
}
```

### Swift

```swift
class Solution {
    func furthestBuilding(_ heights: [Int], _ bricks: Int, _ ladders: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun furthestBuilding(heights: IntArray, bricks: Int, ladders: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int furthestBuilding(List<int> heights, int bricks, int ladders) {
    
  }
}
```

### Go

```golang
func furthestBuilding(heights []int, bricks int, ladders int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} heights
# @param {Integer} bricks
# @param {Integer} ladders
# @return {Integer}
def furthest_building(heights, bricks, ladders)
    
end
```

### Scala

```scala
object Solution {
    def furthestBuilding(heights: Array[Int], bricks: Int, ladders: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn furthest_building(heights: Vec<i32>, bricks: i32, ladders: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (furthest-building heights bricks ladders)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec furthest_building(Heights :: [integer()], Bricks :: integer(), Ladders :: integer()) -> integer().
furthest_building(Heights, Bricks, Ladders) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec furthest_building(heights :: [integer], bricks :: integer, ladders :: integer) :: integer
  def furthest_building(heights, bricks, ladders) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func furthestBuilding(heights: Array<Int64>, bricks: Int64, ladders: Int64): Int64 {

    }
}
```

