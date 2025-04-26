# 3169. 无需开会的工作日

## 题目描述

<p>给你一个正整数 <code>days</code>，表示员工可工作的总天数（从第 1 天开始）。另给你一个二维数组 <code>meetings</code>，长度为 <code>n</code>，其中 <code>meetings[i] = [start_i, end_i]</code> 表示第 <code>i</code> 次会议的开始和结束天数（包含首尾）。</p>

<p>返回员工可工作且没有安排会议的天数。</p>

<p><strong>注意：</strong>会议时间可能会有重叠。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">days = 10, meetings = [[5,7],[1,3],[9,10]]</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>第 4 天和第 8 天没有安排会议。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">days = 5, meetings = [[2,4],[1,3]]</span></p>

<p><strong>输出：</strong><span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p>第 5 天没有安排会议。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">days = 6, meetings = [[1,6]]</span></p>

<p><strong>输出：</strong>0</p>

<p><strong>解释：</strong></p>

<p>所有工作日都安排了会议。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= days &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= meetings.length &lt;= 10<sup>5</sup></code></li>
	<li><code>meetings[i].length == 2</code></li>
	<li><code>1 &lt;= meetings[i][0] &lt;= meetings[i][1] &lt;= days</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 排序

## 提示

1. Merge the overlapping meetings and sort the new meetings timings.
2. Return the sum of difference between the end time of a meeting and the start time of the next meeting for all adjacent pairs.

## 示例

```
10
[[5,7],[1,3],[9,10]]
5
[[2,4],[1,3]]
6
[[1,6]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        
    }
};
```

### Java

```java
class Solution {
    public int countDays(int days, int[][] meetings) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
```

### C

```c
int countDays(int days, int** meetings, int meetingsSize, int* meetingsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountDays(int days, int[][] meetings) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} days
 * @param {number[][]} meetings
 * @return {number}
 */
var countDays = function(days, meetings) {
    
};
```

### TypeScript

```typescript
function countDays(days: number, meetings: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $days
     * @param Integer[][] $meetings
     * @return Integer
     */
    function countDays($days, $meetings) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countDays(_ days: Int, _ meetings: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countDays(days: Int, meetings: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countDays(int days, List<List<int>> meetings) {
    
  }
}
```

### Go

```golang
func countDays(days int, meetings [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} days
# @param {Integer[][]} meetings
# @return {Integer}
def count_days(days, meetings)
    
end
```

### Scala

```scala
object Solution {
    def countDays(days: Int, meetings: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_days(days: i32, meetings: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-days days meetings)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_days(Days :: integer(), Meetings :: [[integer()]]) -> integer().
count_days(Days, Meetings) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_days(days :: integer, meetings :: [[integer]]) :: integer
  def count_days(days, meetings) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countDays(days: Int64, meetings: Array<Array<Int64>>): Int64 {

    }
}
```

