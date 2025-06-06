# 983. 最低票价

## 题目描述

<p>在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为&nbsp;<code>days</code>&nbsp;的数组给出。每一项是一个从&nbsp;<code>1</code>&nbsp;到&nbsp;<code>365</code>&nbsp;的整数。</p>

<p>火车票有 <strong>三种不同的销售方式</strong> ：</p>

<ul>
	<li>一张 <strong>为期一天</strong> 的通行证售价为&nbsp;<code>costs[0]</code> 美元；</li>
	<li>一张 <strong>为期七天</strong> 的通行证售价为&nbsp;<code>costs[1]</code> 美元；</li>
	<li>一张 <strong>为期三十天</strong> 的通行证售价为&nbsp;<code>costs[2]</code> 美元。</li>
</ul>

<p>通行证允许数天无限制的旅行。 例如，如果我们在第 <code>2</code> 天获得一张 <strong>为期 7 天</strong> 的通行证，那么我们可以连着旅行 7 天：第 <code>2</code> 天、第 <code>3</code> 天、第 <code>4</code> 天、第 <code>5</code> 天、第 <code>6</code> 天、第 <code>7</code> 天和第 <code>8</code> 天。</p>

<p>返回 <em>你想要完成在给定的列表&nbsp;<code>days</code>&nbsp;中列出的每一天的旅行所需要的最低消费&nbsp;</em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>days = [1,4,6,7,8,20], costs = [2,7,15]
<strong>输出：</strong>11
<strong>解释： </strong>
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
你总共花了 $11，并完成了你计划的每一天旅行。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
<strong>输出：</strong>17
<strong>解释：
</strong>例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划： 
在第 1 天，你花了 costs[2] = $15 买了一张为期 30 天的通行证，它将在第 1, 2, ..., 30 天生效。
在第 31 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 31 天生效。 
你总共花了 $17，并完成了你计划的每一天旅行。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= days.length &lt;= 365</code></li>
	<li><code>1 &lt;= days[i] &lt;= 365</code></li>
	<li><code>days</code>&nbsp;按顺序严格递增</li>
	<li><code>costs.length == 3</code></li>
	<li><code>1 &lt;= costs[i] &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 示例

```
[1,4,6,7,8,20]
[2,7,15]
[1,2,3,4,5,6,7,8,9,10,30,31]
[2,7,15]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        
    }
};
```

### Java

```java
class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
```

### C

```c
int mincostTickets(int* days, int daysSize, int* costs, int costsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MincostTickets(int[] days, int[] costs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function(days, costs) {
    
};
```

### TypeScript

```typescript
function mincostTickets(days: number[], costs: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $days
     * @param Integer[] $costs
     * @return Integer
     */
    function mincostTickets($days, $costs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mincostTickets(_ days: [Int], _ costs: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mincostTickets(days: IntArray, costs: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int mincostTickets(List<int> days, List<int> costs) {
    
  }
}
```

### Go

```golang
func mincostTickets(days []int, costs []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} days
# @param {Integer[]} costs
# @return {Integer}
def mincost_tickets(days, costs)
    
end
```

### Scala

```scala
object Solution {
    def mincostTickets(days: Array[Int], costs: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn mincost_tickets(days: Vec<i32>, costs: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (mincost-tickets days costs)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec mincost_tickets(Days :: [integer()], Costs :: [integer()]) -> integer().
mincost_tickets(Days, Costs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec mincost_tickets(days :: [integer], costs :: [integer]) :: integer
  def mincost_tickets(days, costs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mincostTickets(days: Array<Int64>, costs: Array<Int64>): Int64 {

    }
}
```

