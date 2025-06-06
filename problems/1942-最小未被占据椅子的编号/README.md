# 1942. 最小未被占据椅子的编号

## 题目描述

<p>有 <code>n</code> 个朋友在举办一个派对，这些朋友从 <code>0</code> 到 <code>n - 1</code> 编号。派对里有 <strong>无数</strong> 张椅子，编号为 <code>0</code> 到 <code>infinity</code> 。当一个朋友到达派对时，他会占据 <strong>编号最小</strong> 且未被占据的椅子。</p>

<ul>
	<li>比方说，当一个朋友到达时，如果椅子 <code>0</code> ，<code>1</code> 和 <code>5</code> 被占据了，那么他会占据 <code>2</code> 号椅子。</li>
</ul>

<p>当一个朋友离开派对时，他的椅子会立刻变成未占据状态。如果同一时刻有另一个朋友到达，可以立即占据这张椅子。</p>

<p>给你一个下标从 <strong>0</strong> 开始的二维整数数组 <code>times</code> ，其中 <code>times[i] = [arrival<sub>i</sub>, leaving<sub>i</sub>]</code> 表示第 <code>i</code> 个朋友到达和离开的时刻，同时给你一个整数 <code>targetFriend</code> 。所有到达时间 <strong>互不相同</strong> 。</p>

<p>请你返回编号为 <code>targetFriend</code> 的朋友占据的 <strong>椅子编号</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>times = [[1,4],[2,3],[4,6]], targetFriend = 1
<b>输出：</b>1
<b>解释：</b>
- 朋友 0 时刻 1 到达，占据椅子 0 。
- 朋友 1 时刻 2 到达，占据椅子 1 。
- 朋友 1 时刻 3 离开，椅子 1 变成未占据。
- 朋友 0 时刻 4 离开，椅子 0 变成未占据。
- 朋友 2 时刻 4 到达，占据椅子 0 。
朋友 1 占据椅子 1 ，所以返回 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>times = [[3,10],[1,5],[2,6]], targetFriend = 0
<b>输出：</b>2
<b>解释：</b>
- 朋友 1 时刻 1 到达，占据椅子 0 。
- 朋友 2 时刻 2 到达，占据椅子 1 。
- 朋友 0 时刻 3 到达，占据椅子 2 。
- 朋友 1 时刻 5 离开，椅子 0 变成未占据。
- 朋友 2 时刻 6 离开，椅子 1 变成未占据。
- 朋友 0 时刻 10 离开，椅子 2 变成未占据。
朋友 0 占据椅子 2 ，所以返回 2 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == times.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>times[i].length == 2</code></li>
	<li><code>1 &lt;= arrival<sub>i</sub> &lt; leaving<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= targetFriend &lt;= n - 1</code></li>
	<li>每个 <code>arrival<sub>i</sub></code> 时刻 <strong>互不相同</strong> 。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 堆（优先队列）

## 提示

1. Sort times by arrival time.
2. for each arrival_i find the smallest unoccupied chair and mark it as occupied until leaving_i.

## 示例

```
[[1,4],[2,3],[4,6]]
1
[[3,10],[1,5],[2,6]]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int smallestChair(vector<vector<int>>& times, int targetFriend) {
        
    }
};
```

### Java

```java
class Solution {
    public int smallestChair(int[][] times, int targetFriend) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
```

### C

```c
int smallestChair(int** times, int timesSize, int* timesColSize, int targetFriend) {
    
}
```

### C#

```csharp
public class Solution {
    public int SmallestChair(int[][] times, int targetFriend) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} times
 * @param {number} targetFriend
 * @return {number}
 */
var smallestChair = function(times, targetFriend) {
    
};
```

### TypeScript

```typescript
function smallestChair(times: number[][], targetFriend: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $times
     * @param Integer $targetFriend
     * @return Integer
     */
    function smallestChair($times, $targetFriend) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestChair(_ times: [[Int]], _ targetFriend: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestChair(times: Array<IntArray>, targetFriend: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int smallestChair(List<List<int>> times, int targetFriend) {
    
  }
}
```

### Go

```golang
func smallestChair(times [][]int, targetFriend int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} times
# @param {Integer} target_friend
# @return {Integer}
def smallest_chair(times, target_friend)
    
end
```

### Scala

```scala
object Solution {
    def smallestChair(times: Array[Array[Int]], targetFriend: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_chair(times: Vec<Vec<i32>>, target_friend: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-chair times targetFriend)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec smallest_chair(Times :: [[integer()]], TargetFriend :: integer()) -> integer().
smallest_chair(Times, TargetFriend) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_chair(times :: [[integer]], target_friend :: integer) :: integer
  def smallest_chair(times, target_friend) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestChair(times: Array<Array<Int64>>, targetFriend: Int64): Int64 {

    }
}
```

