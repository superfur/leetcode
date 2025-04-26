# 3100. 换水问题 II

## 题目描述

<p>给你两个整数 <code>numBottles</code> 和 <code>numExchange</code> 。</p>

<p><code>numBottles</code> 代表你最初拥有的满水瓶数量。在一次操作中，你可以执行以下操作之一：</p>

<ul>
	<li>喝掉任意数量的满水瓶，使它们变成空水瓶。</li>
	<li>用 <code>numExchange</code> 个空水瓶交换一个满水瓶。然后，将 <code>numExchange</code> 的值增加 1 。</li>
</ul>

<p>注意，你不能使用相同的 <code>numExchange</code> 值交换多批空水瓶。例如，如果 <code>numBottles == 3</code> 并且 <code>numExchange == 1</code> ，则不能用 <code>3</code> 个空水瓶交换成 <code>3</code> 个满水瓶。</p>

<p>返回你 <strong>最多</strong> 可以喝到多少瓶水。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/28/exampleone1.png" style="width: 948px; height: 482px; padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>输入：</strong>numBottles = 13, numExchange = 6
<strong>输出：</strong>15
<strong>解释：</strong>上表显示了满水瓶的数量、空水瓶的数量、numExchange 的值，以及累计喝掉的水瓶数量。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/28/example231.png" style="width: 990px; height: 642px; padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>输入：</strong>numBottles = 10, numExchange = 3
<strong>输出：</strong>13
<strong>解释：</strong>上表显示了满水瓶的数量、空水瓶的数量、numExchange 的值，以及累计喝掉的水瓶数量。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= numBottles &lt;= 100 </code></li>
	<li><code>1 &lt;= numExchange &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 模拟

## 提示

1. Simulate the process step by step. At each step, drink <code>numExchange</code> bottles of water then exchange them for a full bottle. Keep repeating this step until you cannot exchange  bottles anymore.

## 示例

```
13
6
10
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
```

### C

```c
int maxBottlesDrunk(int numBottles, int numExchange) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxBottlesDrunk(int numBottles, int numExchange) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var maxBottlesDrunk = function(numBottles, numExchange) {
    
};
```

### TypeScript

```typescript
function maxBottlesDrunk(numBottles: number, numExchange: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $numBottles
     * @param Integer $numExchange
     * @return Integer
     */
    function maxBottlesDrunk($numBottles, $numExchange) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxBottlesDrunk(_ numBottles: Int, _ numExchange: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxBottlesDrunk(numBottles: Int, numExchange: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxBottlesDrunk(int numBottles, int numExchange) {
    
  }
}
```

### Go

```golang
func maxBottlesDrunk(numBottles int, numExchange int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num_bottles
# @param {Integer} num_exchange
# @return {Integer}
def max_bottles_drunk(num_bottles, num_exchange)
    
end
```

### Scala

```scala
object Solution {
    def maxBottlesDrunk(numBottles: Int, numExchange: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_bottles_drunk(num_bottles: i32, num_exchange: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-bottles-drunk numBottles numExchange)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_bottles_drunk(NumBottles :: integer(), NumExchange :: integer()) -> integer().
max_bottles_drunk(NumBottles, NumExchange) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_bottles_drunk(num_bottles :: integer, num_exchange :: integer) :: integer
  def max_bottles_drunk(num_bottles, num_exchange) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxBottlesDrunk(numBottles: Int64, numExchange: Int64): Int64 {

    }
}
```

