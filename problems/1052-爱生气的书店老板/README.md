# 1052. 爱生气的书店老板

## 题目描述

<p>有一个书店老板，他的书店开了&nbsp;<code>n</code>&nbsp;分钟。每分钟都有一些顾客进入这家商店。给定一个长度为 <code>n</code> 的整数数组 <code>customers</code> ，其中 <code>customers[i]</code> 是在第 <code>i</code> 分钟开始时进入商店的顾客数量，所有这些顾客在第 <code>i</code> 分钟结束后离开。</p>

<p>在某些分钟内，书店老板会生气。 如果书店老板在第 <code>i</code> 分钟生气，那么 <code>grumpy[i] = 1</code>，否则 <code>grumpy[i] = 0</code>。</p>

<p>当书店老板生气时，那一分钟的顾客就会不满意，若老板不生气则顾客是满意的。</p>

<p>书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续&nbsp;<code>minutes</code>&nbsp;分钟不生气，但却只能使用一次。</p>

<p>请你返回 <em>这一天营业下来，最多有多少客户能够感到满意</em> 。<br />
&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
<strong>输出：</strong>16
<strong>解释：</strong>书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>customers = [1], grumpy = [0], minutes = 1
<strong>输出：</strong>1</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == customers.length == grumpy.length</code></li>
	<li><code>1 &lt;= minutes &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= customers[i] &lt;= 1000</code></li>
	<li><code>grumpy[i] == 0 or 1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 滑动窗口

## 提示

1. Say the store owner uses their power in minute 1 to X and we have some answer A.  If they instead use their power from minute 2 to X+1, we only have to use data from minutes 1, 2, X and X+1 to update our answer A.

## 示例

```
[1,0,1,2,1,1,7,5]
[0,1,0,1,0,1,0,1]
3
[1]
[0]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
```

### C

```c
int maxSatisfied(int* customers, int customersSize, int* grumpy, int grumpySize, int minutes) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSatisfied(int[] customers, int[] grumpy, int minutes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} customers
 * @param {number[]} grumpy
 * @param {number} minutes
 * @return {number}
 */
var maxSatisfied = function(customers, grumpy, minutes) {
    
};
```

### TypeScript

```typescript
function maxSatisfied(customers: number[], grumpy: number[], minutes: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $customers
     * @param Integer[] $grumpy
     * @param Integer $minutes
     * @return Integer
     */
    function maxSatisfied($customers, $grumpy, $minutes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSatisfied(_ customers: [Int], _ grumpy: [Int], _ minutes: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSatisfied(customers: IntArray, grumpy: IntArray, minutes: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSatisfied(List<int> customers, List<int> grumpy, int minutes) {
    
  }
}
```

### Go

```golang
func maxSatisfied(customers []int, grumpy []int, minutes int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} customers
# @param {Integer[]} grumpy
# @param {Integer} minutes
# @return {Integer}
def max_satisfied(customers, grumpy, minutes)
    
end
```

### Scala

```scala
object Solution {
    def maxSatisfied(customers: Array[Int], grumpy: Array[Int], minutes: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_satisfied(customers: Vec<i32>, grumpy: Vec<i32>, minutes: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-satisfied customers grumpy minutes)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_satisfied(Customers :: [integer()], Grumpy :: [integer()], Minutes :: integer()) -> integer().
max_satisfied(Customers, Grumpy, Minutes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_satisfied(customers :: [integer], grumpy :: [integer], minutes :: integer) :: integer
  def max_satisfied(customers, grumpy, minutes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSatisfied(customers: Array<Int64>, grumpy: Array<Int64>, minutes: Int64): Int64 {

    }
}
```

