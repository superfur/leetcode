# 1353. 最多可以参加的会议数目

## 题目描述

<p>给你一个数组&nbsp;<code>events</code>，其中&nbsp;<code>events[i] = [startDay<sub>i</sub>, endDay<sub>i</sub>]</code>&nbsp;，表示会议&nbsp;<code>i</code>&nbsp;开始于&nbsp;<code>startDay<sub>i</sub></code>&nbsp;，结束于&nbsp;<code>endDay<sub>i</sub></code>&nbsp;。</p>

<p>你可以在满足&nbsp;<code>startDay<sub>i</sub>&nbsp;&lt;= d &lt;= endDay<sub>i</sub></code><sub>&nbsp;</sub>中的任意一天&nbsp;<code>d</code>&nbsp;参加会议&nbsp;<code>i</code>&nbsp;。在任意一天&nbsp;<code>d</code>&nbsp;中只能参加一场会议。</p>

<p>请你返回你可以参加的&nbsp;<strong>最大&nbsp;</strong>会议数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/16/e1.png" style="height: 267px; width: 400px;" /></p>

<pre>
<strong>输入：</strong>events = [[1,2],[2,3],[3,4]]
<strong>输出：</strong>3
<strong>解释：</strong>你可以参加所有的三个会议。
安排会议的一种方案如上图。
第 1 天参加第一个会议。
第 2 天参加第二个会议。
第 3 天参加第三个会议。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>events= [[1,2],[2,3],[3,4],[1,2]]
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong>​​​​​​</p>

<ul>
	<li><code>1 &lt;= events.length &lt;= 10<sup>5</sup></code></li>
	<li><code>events[i].length == 2</code></li>
	<li><code>1 &lt;= startDay<sub>i</sub>&nbsp;&lt;= endDay<sub>i</sub>&nbsp;&lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序
- 堆（优先队列）

## 提示

1. Sort the events by the start time and in case of tie by the end time in ascending order.
2. Loop over the sorted events. Attend as much as you can and keep the last day occupied. When you try to attend new event keep in mind the first day you can attend a new event in.

## 示例

```
[[1,2],[2,3],[3,4]]
[[1,2],[2,3],[3,4],[1,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxEvents(int[][] events) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
```

### C

```c
int maxEvents(int** events, int eventsSize, int* eventsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxEvents(int[][] events) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} events
 * @return {number}
 */
var maxEvents = function(events) {
    
};
```

### TypeScript

```typescript
function maxEvents(events: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $events
     * @return Integer
     */
    function maxEvents($events) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxEvents(_ events: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxEvents(events: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxEvents(List<List<int>> events) {
    
  }
}
```

### Go

```golang
func maxEvents(events [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} events
# @return {Integer}
def max_events(events)
    
end
```

### Scala

```scala
object Solution {
    def maxEvents(events: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_events(events: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-events events)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_events(Events :: [[integer()]]) -> integer().
max_events(Events) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_events(events :: [[integer]]) :: integer
  def max_events(events) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxEvents(events: Array<Array<Int64>>): Int64 {

    }
}
```

