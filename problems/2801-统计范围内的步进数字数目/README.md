# 2801. 统计范围内的步进数字数目

## 题目描述

<p>给你两个正整数&nbsp;<code>low</code> 和&nbsp;<code>high</code>&nbsp;，都用字符串表示，请你统计闭区间 <code>[low, high]</code>&nbsp;内的 <strong>步进数字</strong>&nbsp;数目。</p>

<p>如果一个整数相邻数位之间差的绝对值都 <strong>恰好</strong>&nbsp;是 <code>1</code>&nbsp;，那么这个数字被称为 <strong>步进数字</strong>&nbsp;。</p>

<p>请你返回一个整数，表示闭区间&nbsp;<code>[low, high]</code>&nbsp;之间步进数字的数目。</p>

<p>由于答案可能很大，请你将它对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p><b>注意：</b>步进数字不能有前导 0 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>low = "1", high = "11"
<b>输出：</b>10
<strong>解释：</strong>区间 [1,11] 内的步进数字为 1 ，2 ，3 ，4 ，5 ，6 ，7 ，8 ，9 和 10 。总共有 10 个步进数字。所以输出为 10 。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>low = "90", high = "101"
<b>输出：</b>2
<strong>解释：</strong>区间 [90,101] 内的步进数字为 98 和 101 。总共有 2 个步进数字。所以输出为 2 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= int(low) &lt;= int(high) &lt; 10<sup>100</sup></code></li>
	<li><code>1 &lt;= low.length, high.length &lt;= 100</code></li>
	<li><code>low</code> 和&nbsp;<code>high</code>&nbsp;只包含数字。</li>
	<li><code>low</code> 和&nbsp;<code>high</code>&nbsp;都不含前导 0 。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. Calculate the number of stepping numbers in the range [1, high] and subtract the number of stepping numbers in the range [1, low - 1].
2. The main problem is calculating the number of stepping numbers in the range [1, x].
3. First, calculate the number of stepping numbers shorter than x in length, which can be done using dynamic programming. (dp[i][j] is the number of i-digit stepping numbers ending with digit j).
4. Finally, calculate the number of stepping numbers that have the same length as x similarly. However, this time we need to maintain whether the prefix (in string) is smaller than or equal to x in the DP state.

## 示例

```
"1"
"11"
"90"
"101"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countSteppingNumbers(string low, string high) {
        
    }
};
```

### Java

```java
class Solution {
    public int countSteppingNumbers(String low, String high) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        
```

### C

```c
int countSteppingNumbers(char* low, char* high) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountSteppingNumbers(string low, string high) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} low
 * @param {string} high
 * @return {number}
 */
var countSteppingNumbers = function(low, high) {
    
};
```

### TypeScript

```typescript
function countSteppingNumbers(low: string, high: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $low
     * @param String $high
     * @return Integer
     */
    function countSteppingNumbers($low, $high) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSteppingNumbers(_ low: String, _ high: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSteppingNumbers(low: String, high: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSteppingNumbers(String low, String high) {
    
  }
}
```

### Go

```golang
func countSteppingNumbers(low string, high string) int {
    
}
```

### Ruby

```ruby
# @param {String} low
# @param {String} high
# @return {Integer}
def count_stepping_numbers(low, high)
    
end
```

### Scala

```scala
object Solution {
    def countSteppingNumbers(low: String, high: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_stepping_numbers(low: String, high: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-stepping-numbers low high)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_stepping_numbers(Low :: unicode:unicode_binary(), High :: unicode:unicode_binary()) -> integer().
count_stepping_numbers(Low, High) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_stepping_numbers(low :: String.t, high :: String.t) :: integer
  def count_stepping_numbers(low, high) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSteppingNumbers(low: String, high: String): Int64 {

    }
}
```

