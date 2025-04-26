# 1751. 最多可以参加的会议数目 II

## 题目描述

<p>给你一个 <code>events</code> 数组，其中 <code>events[i] = [startDay<sub>i</sub>, endDay<sub>i</sub>, value<sub>i</sub>]</code> ，表示第 <code>i</code> 个会议在 <code>startDay<sub>i</sub></code><sub> </sub>天开始，第 <code>endDay<sub>i</sub></code> 天结束，如果你参加这个会议，你能得到价值 <code>value<sub>i</sub></code> 。同时给你一个整数 <code>k</code> 表示你能参加的最多会议数目。</p>

<p>你同一时间只能参加一个会议。如果你选择参加某个会议，那么你必须 <strong>完整</strong> 地参加完这个会议。会议结束日期是包含在会议内的，也就是说你不能同时参加一个开始日期与另一个结束日期相同的两个会议。</p>

<p>请你返回能得到的会议价值 <strong>最大和</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/02/06/screenshot-2021-01-11-at-60048-pm.png" style="width: 400px; height: 103px;" /></p>

<pre>
<b>输入：</b>events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
<b>输出：</b>7
<strong>解释：</strong>选择绿色的活动会议 0 和 1，得到总价值和为 4 + 3 = 7 。</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/02/06/screenshot-2021-01-11-at-60150-pm.png" style="width: 400px; height: 103px;" /></p>

<pre>
<b>输入：</b>events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
<b>输出：</b>10
<b>解释：</b>参加会议 2 ，得到价值和为 10 。
你没法再参加别的会议了，因为跟会议 2 有重叠。你 <strong>不</strong> 需要参加满 k 个会议。</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/02/06/screenshot-2021-01-11-at-60703-pm.png" style="width: 400px; height: 126px;" /></strong></p>

<pre>
<b>输入：</b>events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
<b>输出：</b>9
<b>解释：</b>尽管会议互不重叠，你只能参加 3 个会议，所以选择价值最大的 3 个会议。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= k <= events.length</code></li>
	<li><code>1 <= k * events.length <= 10<sup>6</sup></code></li>
	<li><code>1 <= startDay<sub>i</sub> <= endDay<sub>i</sub> <= 10<sup>9</sup></code></li>
	<li><code>1 <= value<sub>i</sub> <= 10<sup>6</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 二分查找
- 动态规划
- 排序

## 提示

1. Sort the events by its startTime.
2. For every event, you can either choose it and consider the next event available, or you can ignore it. You can efficiently find the next event that is available using binary search.

## 示例

```
[[1,2,4],[3,4,3],[2,3,1]]
2
[[1,2,4],[3,4,3],[2,3,10]]
2
[[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxValue(int[][] events, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
```

### C

```c
int maxValue(int** events, int eventsSize, int* eventsColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxValue(int[][] events, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} events
 * @param {number} k
 * @return {number}
 */
var maxValue = function(events, k) {
    
};
```

### TypeScript

```typescript
function maxValue(events: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $events
     * @param Integer $k
     * @return Integer
     */
    function maxValue($events, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxValue(_ events: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxValue(events: Array<IntArray>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxValue(List<List<int>> events, int k) {
    
  }
}
```

### Go

```golang
func maxValue(events [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} events
# @param {Integer} k
# @return {Integer}
def max_value(events, k)
    
end
```

### Scala

```scala
object Solution {
    def maxValue(events: Array[Array[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_value(events: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-value events k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_value(Events :: [[integer()]], K :: integer()) -> integer().
max_value(Events, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_value(events :: [[integer]], k :: integer) :: integer
  def max_value(events, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxValue(events: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

