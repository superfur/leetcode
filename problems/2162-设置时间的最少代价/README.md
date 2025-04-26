# 2162. 设置时间的最少代价

## 题目描述

<p>常见的微波炉可以设置加热时间，且加热时间满足以下条件：</p>

<ul>
	<li>至少为 <code>1</code>&nbsp;秒钟。</li>
	<li>至多为&nbsp;<code>99</code>&nbsp;分&nbsp;<code>99</code>&nbsp;秒。</li>
</ul>

<p>你可以 <strong>最多</strong>&nbsp;输入&nbsp;<strong>4 个数字</strong>&nbsp;来设置加热时间。如果你输入的位数不足 4 位，微波炉会自动加 <strong>前缀</strong>&nbsp;<strong>0</strong>&nbsp;来补足 4 位。微波炉会将设置好的四位数中，<strong>前</strong>&nbsp;两位当作分钟数，<strong>后</strong>&nbsp;两位当作秒数。它们所表示的总时间就是加热时间。比方说：</p>

<ul>
	<li>你输入&nbsp;<code>9</code> <code>5</code> <code>4</code>&nbsp;（三个数字），被自动补足为&nbsp;<code>0954</code>&nbsp;，并表示&nbsp;<code>9</code>&nbsp;分&nbsp;<code>54</code>&nbsp;秒。</li>
	<li>你输入&nbsp;<code>0</code> <code>0</code> <code>0</code> <code>8</code>&nbsp;（四个数字），表示&nbsp;<code>0</code>&nbsp;分&nbsp;<code>8</code>&nbsp;秒。</li>
	<li>你输入&nbsp;<code>8</code> <code>0</code> <code>9</code> <code>0</code>&nbsp;，表示&nbsp;<code>80</code>&nbsp;分&nbsp;<code>90</code>&nbsp;秒。</li>
	<li>你输入&nbsp;<code>8</code> <code>1</code> <code>3</code> <code>0</code>&nbsp;，表示&nbsp;<code>81</code>&nbsp;分&nbsp;<code>30</code>&nbsp;秒。</li>
</ul>

<p>给你整数&nbsp;<code>startAt</code>&nbsp;，<code>moveCost</code>&nbsp;，<code>pushCost</code>&nbsp;和&nbsp;<code>targetSeconds</code>&nbsp;。<strong>一开始</strong>，你的手指在数字&nbsp;<code>startAt</code>&nbsp;处。将手指移到<strong>&nbsp;任何其他数字</strong>&nbsp;，需要花费&nbsp;<code>moveCost</code>&nbsp;的单位代价。<strong>每</strong>&nbsp;输入你手指所在位置的数字一次，需要花费&nbsp;<code>pushCost</code>&nbsp;的单位代价。</p>

<p>要设置&nbsp;<code>targetSeconds</code>&nbsp;秒的加热时间，可能会有多种设置方法。你想要知道这些方法中，总代价最小为多少。</p>

<p>请你能返回设置&nbsp;<code>targetSeconds</code>&nbsp;秒钟加热时间需要花费的最少代价。</p>

<p>请记住，虽然微波炉的秒数最多可以设置到 <code>99</code>&nbsp;秒，但一分钟等于&nbsp;<code>60</code>&nbsp;秒。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/30/1.png" style="width: 506px; height: 210px;"></p>

<pre><b>输入：</b>startAt = 1, moveCost = 2, pushCost = 1, targetSeconds = 600
<b>输出：</b>6
<b>解释：</b>以下为设置加热时间的所有方法。
- 1 0 0 0 ，表示 10 分 0 秒。
&nbsp; 手指一开始就在数字 1 处，输入 1 （代价为 1），移到 0 处（代价为 2），输入 0（代价为 1），输入 0（代价为 1），输入 0（代价为 1）。
&nbsp; 总代价为：1 + 2 + 1 + 1 + 1 = 6 。这是所有方案中的最小代价。
- 0 9 6 0，表示 9 分 60 秒。它也表示 600 秒。
&nbsp; 手指移到 0 处（代价为 2），输入 0 （代价为 1），移到 9 处（代价为 2），输入 9（代价为 1），移到 6 处（代价为 2），输入 6（代价为 1），移到 0 处（代价为 2），输入 0（代价为 1）。
&nbsp; 总代价为：2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 = 12 。
- 9 6 0，微波炉自动补全为 0960 ，表示 9 分 60 秒。
&nbsp; 手指移到 9 处（代价为 2），输入 9 （代价为 1），移到 6 处（代价为 2），输入 6（代价为 1），移到 0 处（代价为 2），输入 0（代价为 1）。
&nbsp; 总代价为：2 + 1 + 2 + 1 + 2 + 1 = 9 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/30/2.png" style="width: 505px; height: 73px;"></p>

<pre><b>输入：</b>startAt = 0, moveCost = 1, pushCost = 2, targetSeconds = 76
<b>输出：</b>6
<b>解释：</b>最优方案为输入两个数字 7 6，表示 76 秒。
手指移到 7 处（代价为 1），输入 7 （代价为 2），移到 6 处（代价为 1），输入 6（代价为 2）。总代价为：1 + 2 + 1 + 2 = 6
其他可行方案为 0076 ，076 ，0116 和 116 ，但是它们的代价都比 6 大。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= startAt &lt;= 9</code></li>
	<li><code>1 &lt;= moveCost, pushCost &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= targetSeconds &lt;= 6039</code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 枚举

## 提示

1. Define a separate function Cost(mm, ss) where 0 <= mm <= 99 and 0 <= ss <= 99. This function should calculate the cost of setting the cooking time to mm minutes and ss seconds
2. The range of the minutes is small (i.e., [0, 99]), how can you use that?
3. For every mm in [0, 99], calculate the needed ss to make mm:ss equal to targetSeconds and minimize the cost of setting the cooking time to mm:ss
4. Be careful in some cases when ss is not in the valid range [0, 99].

## 示例

```
1
2
1
600
0
1
2
76
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        """
        :type startAt: int
        :type moveCost: int
        :type pushCost: int
        :type targetSeconds: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        
```

### C

```c
int minCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} startAt
 * @param {number} moveCost
 * @param {number} pushCost
 * @param {number} targetSeconds
 * @return {number}
 */
var minCostSetTime = function(startAt, moveCost, pushCost, targetSeconds) {
    
};
```

### TypeScript

```typescript
function minCostSetTime(startAt: number, moveCost: number, pushCost: number, targetSeconds: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $startAt
     * @param Integer $moveCost
     * @param Integer $pushCost
     * @param Integer $targetSeconds
     * @return Integer
     */
    function minCostSetTime($startAt, $moveCost, $pushCost, $targetSeconds) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCostSetTime(_ startAt: Int, _ moveCost: Int, _ pushCost: Int, _ targetSeconds: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCostSetTime(startAt: Int, moveCost: Int, pushCost: Int, targetSeconds: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
    
  }
}
```

### Go

```golang
func minCostSetTime(startAt int, moveCost int, pushCost int, targetSeconds int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} start_at
# @param {Integer} move_cost
# @param {Integer} push_cost
# @param {Integer} target_seconds
# @return {Integer}
def min_cost_set_time(start_at, move_cost, push_cost, target_seconds)
    
end
```

### Scala

```scala
object Solution {
    def minCostSetTime(startAt: Int, moveCost: Int, pushCost: Int, targetSeconds: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost_set_time(start_at: i32, move_cost: i32, push_cost: i32, target_seconds: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost-set-time startAt moveCost pushCost targetSeconds)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost_set_time(StartAt :: integer(), MoveCost :: integer(), PushCost :: integer(), TargetSeconds :: integer()) -> integer().
min_cost_set_time(StartAt, MoveCost, PushCost, TargetSeconds) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost_set_time(start_at :: integer, move_cost :: integer, push_cost :: integer, target_seconds :: integer) :: integer
  def min_cost_set_time(start_at, move_cost, push_cost, target_seconds) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCostSetTime(startAt: Int64, moveCost: Int64, pushCost: Int64, targetSeconds: Int64): Int64 {

    }
}
```

