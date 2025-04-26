# 1449. 数位成本和为目标值的最大数字

## 题目描述

<p>给你一个整数数组 <code>cost</code> 和一个整数 <code>target</code> 。请你返回满足如下规则可以得到的 <strong>最大</strong> 整数：</p>

<ul>
	<li>给当前结果添加一个数位（<code>i + 1</code>）的成本为 <code>cost[i]</code> （<code>cost</code> 数组下标从 0 开始）。</li>
	<li>总成本必须恰好等于 <code>target</code> 。</li>
	<li>添加的数位中没有数字 0 。</li>
</ul>

<p>由于答案可能会很大，请你以字符串形式返回。</p>

<p>如果按照上述要求无法得到任何整数，请你返回 "0" 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>cost = [4,3,2,5,6,7,2,5,5], target = 9
<strong>输出：</strong>"7772"
<strong>解释：</strong>添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。 "977" 也是满足要求的数字，但 "7772" 是较大的数字。
<strong> 数字     成本</strong>
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>cost = [7,6,5,5,5,6,8,7,8], target = 12
<strong>输出：</strong>"85"
<strong>解释：</strong>添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>cost = [2,4,6,2,4,6,4,4,4], target = 5
<strong>输出：</strong>"0"
<strong>解释：</strong>总成本是 target 的条件下，无法生成任何整数。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>cost = [6,10,15,40,40,40,40,40,40], target = 47
<strong>输出：</strong>"32211"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>cost.length == 9</code></li>
	<li><code>1 <= cost[i] <= 5000</code></li>
	<li><code>1 <= target <= 5000</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. Use dynamic programming to find the maximum digits to paint given a total cost.
2. Build the largest number possible using this DP table.

## 示例

```
[4,3,2,5,6,7,2,5,5]
9
[7,6,5,5,5,6,8,7,8]
12
[2,4,6,2,4,6,4,4,4]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string largestNumber(vector<int>& cost, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public String largestNumber(int[] cost, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        
```

### C

```c
char* largestNumber(int* cost, int costSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public string LargestNumber(int[] cost, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} cost
 * @param {number} target
 * @return {string}
 */
var largestNumber = function(cost, target) {
    
};
```

### TypeScript

```typescript
function largestNumber(cost: number[], target: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $cost
     * @param Integer $target
     * @return String
     */
    function largestNumber($cost, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestNumber(_ cost: [Int], _ target: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestNumber(cost: IntArray, target: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String largestNumber(List<int> cost, int target) {
    
  }
}
```

### Go

```golang
func largestNumber(cost []int, target int) string {
    
}
```

### Ruby

```ruby
# @param {Integer[]} cost
# @param {Integer} target
# @return {String}
def largest_number(cost, target)
    
end
```

### Scala

```scala
object Solution {
    def largestNumber(cost: Array[Int], target: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_number(cost: Vec<i32>, target: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (largest-number cost target)
  (-> (listof exact-integer?) exact-integer? string?)
  )
```

### Erlang

```erlang
-spec largest_number(Cost :: [integer()], Target :: integer()) -> unicode:unicode_binary().
largest_number(Cost, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_number(cost :: [integer], target :: integer) :: String.t
  def largest_number(cost, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestNumber(cost: Array<Int64>, target: Int64): String {

    }
}
```

