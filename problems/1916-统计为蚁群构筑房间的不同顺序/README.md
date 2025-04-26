# 1916. 统计为蚁群构筑房间的不同顺序

## 题目描述

<p>你是一只蚂蚁，负责为蚁群构筑 <code>n</code> 间编号从 <code>0</code> 到 <code>n-1</code> 的新房间。给你一个 <strong>下标从 0 开始</strong> 且长度为 <code>n</code> 的整数数组&nbsp;<code>prevRoom</code> 作为扩建计划。其中，<code>prevRoom[i]</code> 表示在构筑房间 <code>i</code> 之前，你必须先构筑房间 <code>prevRoom[i]</code> ，并且这两个房间必须 <strong>直接</strong> 相连。房间 <code>0</code> 已经构筑完成，所以 <code>prevRoom[0] = -1</code> 。扩建计划中还有一条硬性要求，在完成所有房间的构筑之后，从房间 <code>0</code> 可以访问到每个房间。</p>

<p>你一次只能构筑 <strong>一个</strong> 房间。你可以在 <strong>已经构筑好的</strong> 房间之间自由穿行，只要这些房间是 <strong>相连的</strong> 。如果房间&nbsp;<code>prevRoom[i]</code> 已经构筑完成，那么你就可以构筑房间 <code>i</code>。</p>

<p>返回你构筑所有房间的 <strong>不同顺序的数目</strong> 。由于答案可能很大，请返回对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/19/d1.JPG" style="width: 200px; height: 212px;" />
<pre>
<strong>输入：</strong><code>prevRoom</code> = [-1,0,1]
<strong>输出：</strong>1
<strong>解释：</strong>仅有一种方案可以完成所有房间的构筑：0 → 1 → 2
</pre>

<p><strong>示例 2：</strong></p>
<strong><img alt="" src="https://assets.leetcode.com/uploads/2021/06/19/d2.JPG" style="width: 200px; height: 239px;" /></strong>

<pre>
<strong>输入：</strong><code>prevRoom</code> = [-1,0,0,1,2]
<strong>输出：</strong>6
<strong>解释：
</strong>有 6 种不同顺序：
0 → 1 → 3 → 2 → 4
0 → 2 → 4 → 1 → 3
0 → 1 → 2 → 3 → 4
0 → 1 → 2 → 4 → 3
0 → 2 → 1 → 3 → 4
0 → 2 → 1 → 4 → 3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == prevRoom.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>prevRoom[0] == -1</code></li>
	<li>对于所有的&nbsp;<code>1 &lt;= i &lt; n</code>&nbsp;，都有&nbsp;<code>0 &lt;= prevRoom[i] &lt; n</code></li>
	<li>题目保证所有房间都构筑完成后，从房间 <code>0</code> 可以访问到每个房间</li>
</ul>


## 难度

Hard

## 标签

- 树
- 图
- 拓扑排序
- 数学
- 动态规划
- 组合数学

## 提示

1. Use dynamic programming.
2. Let dp[i] be the number of ways to solve the problem for the subtree of node i.
3. Imagine you are trying to fill an array with the order of traversal, dp[i] equals the multiplications of the number of ways to distribute the subtrees of the children of i on the array using combinatorics, multiplied bu their dp values.

## 示例

```
[-1,0,1]
[-1,0,0,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int waysToBuildRooms(vector<int>& prevRoom) {
        
    }
};
```

### Java

```java
class Solution {
    public int waysToBuildRooms(int[] prevRoom) {
        
    }
}
```

### Python

```python
class Solution(object):
    def waysToBuildRooms(self, prevRoom):
        """
        :type prevRoom: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        
```

### C

```c
int waysToBuildRooms(int* prevRoom, int prevRoomSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int WaysToBuildRooms(int[] prevRoom) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} prevRoom
 * @return {number}
 */
var waysToBuildRooms = function(prevRoom) {
    
};
```

### TypeScript

```typescript
function waysToBuildRooms(prevRoom: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $prevRoom
     * @return Integer
     */
    function waysToBuildRooms($prevRoom) {
        
    }
}
```

### Swift

```swift
class Solution {
    func waysToBuildRooms(_ prevRoom: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun waysToBuildRooms(prevRoom: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int waysToBuildRooms(List<int> prevRoom) {
    
  }
}
```

### Go

```golang
func waysToBuildRooms(prevRoom []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} prev_room
# @return {Integer}
def ways_to_build_rooms(prev_room)
    
end
```

### Scala

```scala
object Solution {
    def waysToBuildRooms(prevRoom: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ways_to_build_rooms(prev_room: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (ways-to-build-rooms prevRoom)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec ways_to_build_rooms(PrevRoom :: [integer()]) -> integer().
ways_to_build_rooms(PrevRoom) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ways_to_build_rooms(prev_room :: [integer]) :: integer
  def ways_to_build_rooms(prev_room) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func waysToBuildRooms(prevRoom: Array<Int64>): Int64 {

    }
}
```

