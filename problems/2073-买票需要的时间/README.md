# 2073. 买票需要的时间

## 题目描述

<p>有 <code>n</code> 个人前来排队买票，其中第 <code>0</code> 人站在队伍 <strong>最前方</strong> ，第 <code>(n - 1)</code> 人站在队伍 <strong>最后方</strong> 。</p>

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>tickets</code> ，数组长度为 <code>n</code> ，其中第 <code>i</code> 人想要购买的票数为 <code>tickets[i]</code> 。</p>

<p>每个人买票都需要用掉 <strong>恰好 1 秒</strong> 。一个人 <strong>一次只能买一张票</strong> ，如果需要购买更多票，他必须走到&nbsp; <strong>队尾</strong> 重新排队（<strong>瞬间 </strong>发生，不计时间）。如果一个人没有剩下需要买的票，那他将会 <strong>离开</strong> 队伍。</p>

<p>返回位于位置 <code>k</code>（下标从 <strong>0</strong> 开始）的人完成买票需要的时间（以秒为单位）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>tickets = [2,3,2], k = 2</p>

<p><strong>输出：</strong>6</p>

<p><strong>解释：</strong></p>

<ul>
	<li>队伍一开始为 [2,3,2]，第 k 个人以下划线标识。</li>
	<li>在最前面的人买完票后，队伍在第 1 秒变成 [3,<u>2</u>,1]。</li>
	<li>继续这个过程，队伍在第 2 秒变为[<u>2</u>,1,2]。</li>
	<li>继续这个过程，队伍在第 3 秒变为[1,2,<u>1</u>]。</li>
	<li>继续这个过程，队伍在第 4 秒变为[2,<u>1</u>]。</li>
	<li>继续这个过程，队伍在第 5 秒变为[<u>1</u>,1]。</li>
	<li>继续这个过程，队伍在第 6 秒变为[1]。第 k 个人完成买票，所以返回 6。</li>
</ul>
</div>

<p><strong>示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>tickets = [5,1,1,1], k = 0</p>

<p><strong>输出：</strong>8</p>

<p><strong>解释：</strong></p>

<ul>
	<li>队伍一开始为 [<u>5</u>,1,1,1]，第 k 个人以下划线标识。</li>
	<li>在最前面的人买完票后，队伍在第 1 秒变成 [1,1,1,<u>4</u>]。</li>
	<li>继续这个过程 3 秒，队伍在第 4&nbsp;秒变为[<u>4</u>]。</li>
	<li>继续这个过程 4 秒，队伍在第 8&nbsp;秒变为[]。第 k 个人完成买票，所以返回 8。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == tickets.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= tickets[i] &lt;= 100</code></li>
	<li><code>0 &lt;= k &lt; n</code></li>
</ul>


## 难度

Easy

## 标签

- 队列
- 数组
- 模拟

## 提示

1. Loop through the line of people and decrement the number of tickets for each to buy one at a time as if simulating the line moving forward. Keep track of how many tickets have been sold up until person k has no more tickets to buy.
2. Remember that those who have no more tickets to buy will leave the line.

## 示例

```
[2,3,2]
2
[5,1,1,1]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
```

### C

```c
int timeRequiredToBuy(int* tickets, int ticketsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int TimeRequiredToBuy(int[] tickets, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} tickets
 * @param {number} k
 * @return {number}
 */
var timeRequiredToBuy = function(tickets, k) {
    
};
```

### TypeScript

```typescript
function timeRequiredToBuy(tickets: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $tickets
     * @param Integer $k
     * @return Integer
     */
    function timeRequiredToBuy($tickets, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func timeRequiredToBuy(_ tickets: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun timeRequiredToBuy(tickets: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int timeRequiredToBuy(List<int> tickets, int k) {
    
  }
}
```

### Go

```golang
func timeRequiredToBuy(tickets []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} tickets
# @param {Integer} k
# @return {Integer}
def time_required_to_buy(tickets, k)
    
end
```

### Scala

```scala
object Solution {
    def timeRequiredToBuy(tickets: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn time_required_to_buy(tickets: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (time-required-to-buy tickets k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec time_required_to_buy(Tickets :: [integer()], K :: integer()) -> integer().
time_required_to_buy(Tickets, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec time_required_to_buy(tickets :: [integer], k :: integer) :: integer
  def time_required_to_buy(tickets, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func timeRequiredToBuy(tickets: Array<Int64>, k: Int64): Int64 {

    }
}
```

