# 3386. 按下时间最长的按钮

## 题目描述

<p>给你一个二维数组 <code>events</code>，表示孩子在键盘上按下一系列按钮触发的按钮事件。</p>

<p>每个 <code>events[i] = [index<sub>i</sub>, time<sub>i</sub>]</code> 表示在时间 <code>time<sub>i</sub></code> 时，按下了下标为 <code>index<sub>i</sub></code> 的按钮。</p>

<ul>
	<li>数组按照 <code>time</code> 的递增顺序<strong>排序</strong>。</li>
	<li>按下一个按钮所需的时间是连续两次按钮按下的时间差。按下第一个按钮所需的时间就是其时间戳。</li>
</ul>

<p>返回按下时间&nbsp;<strong>最长&nbsp;</strong>的按钮的 <code>index</code>。如果有多个按钮的按下时间相同，则返回 <code>index</code> 最小的按钮。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">events = [[1,2],[2,5],[3,9],[1,15]]</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>下标为 1 的按钮在时间 2 被按下。</li>
	<li>下标为 2 的按钮在时间 5 被按下，因此按下时间为 <code>5 - 2 = 3</code>。</li>
	<li>下标为 3 的按钮在时间 9 被按下，因此按下时间为 <code>9 - 5 = 4</code>。</li>
	<li>下标为 1 的按钮再次在时间 15 被按下，因此按下时间为 <code>15 - 9 = 6</code>。</li>
</ul>

<p>最终，下标为 1 的按钮按下时间最长，为 6。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">events = [[10,5],[1,7]]</span></p>

<p><strong>输出：</strong> <span class="example-io">10</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>下标为 10 的按钮在时间 5 被按下。</li>
	<li>下标为 1 的按钮在时间 7 被按下，因此按下时间为 <code>7 - 5 = 2</code>。</li>
</ul>

<p>最终，下标为 10 的按钮按下时间最长，为 5。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= events.length &lt;= 1000</code></li>
	<li><code>events[i] == [index<sub>i</sub>, time<sub>i</sub>]</code></li>
	<li><code>1 &lt;= index<sub>i</sub>, time<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li>输入保证数组 <code>events</code> 按照 <code>time<sub>i</sub></code> 的递增顺序排序。</li>
</ul>


## 难度

Easy

## 标签

- 数组

## 示例

```
[[1,2],[2,5],[3,9],[1,15]]
[[10,5],[1,7]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int buttonWithLongestTime(vector<vector<int>>& events) {
        
    }
};
```

### Java

```java
class Solution {
    public int buttonWithLongestTime(int[][] events) {
        
    }
}
```

### Python

```python
class Solution(object):
    def buttonWithLongestTime(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        
```

### C

```c
int buttonWithLongestTime(int** events, int eventsSize, int* eventsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ButtonWithLongestTime(int[][] events) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} events
 * @return {number}
 */
var buttonWithLongestTime = function(events) {
    
};
```

### TypeScript

```typescript
function buttonWithLongestTime(events: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $events
     * @return Integer
     */
    function buttonWithLongestTime($events) {
        
    }
}
```

### Swift

```swift
class Solution {
    func buttonWithLongestTime(_ events: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun buttonWithLongestTime(events: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int buttonWithLongestTime(List<List<int>> events) {
    
  }
}
```

### Go

```golang
func buttonWithLongestTime(events [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} events
# @return {Integer}
def button_with_longest_time(events)
    
end
```

### Scala

```scala
object Solution {
    def buttonWithLongestTime(events: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn button_with_longest_time(events: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (button-with-longest-time events)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec button_with_longest_time(Events :: [[integer()]]) -> integer().
button_with_longest_time(Events) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec button_with_longest_time(events :: [[integer]]) :: integer
  def button_with_longest_time(events) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func buttonWithLongestTime(events: Array<Array<Int64>>): Int64 {

    }
}
```

