# 1124. 表现良好的最长时间段

## 题目描述

<p>给你一份工作时间表&nbsp;<code>hours</code>，上面记录着某一位员工每天的工作小时数。</p>

<p>我们认为当员工一天中的工作小时数大于&nbsp;<code>8</code> 小时的时候，那么这一天就是「<strong>劳累的一天</strong>」。</p>

<p>所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格<strong> 大于</strong>「不劳累的天数」。</p>

<p>请你返回「表现良好时间段」的最大长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>hours = [9,9,6,0,6,6,9]
<strong>输出：</strong>3
<strong>解释：</strong>最长的表现良好时间段是 [9,9,6]。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>hours = [6,6,6]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= hours.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= hours[i] &lt;= 16</code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数组
- 哈希表
- 前缀和
- 单调栈

## 提示

1. Make a new array A of +1/-1s corresponding to if hours[i] is > 8 or not. The goal is to find the longest subarray with positive sum.
2. Using prefix sums (PrefixSum[i+1] = A[0] + A[1] + ... + A[i]), you need to find for each j, the smallest i < j with PrefixSum[i] + 1 == PrefixSum[j].

## 示例

```
[9,9,6,0,6,6,9]
[6,6,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestWPI(vector<int>& hours) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestWPI(int[] hours) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
```

### C

```c
int longestWPI(int* hours, int hoursSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestWPI(int[] hours) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} hours
 * @return {number}
 */
var longestWPI = function(hours) {
    
};
```

### TypeScript

```typescript
function longestWPI(hours: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $hours
     * @return Integer
     */
    function longestWPI($hours) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestWPI(_ hours: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestWPI(hours: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestWPI(List<int> hours) {
    
  }
}
```

### Go

```golang
func longestWPI(hours []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} hours
# @return {Integer}
def longest_wpi(hours)
    
end
```

### Scala

```scala
object Solution {
    def longestWPI(hours: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_wpi(hours: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-wpi hours)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_wpi(Hours :: [integer()]) -> integer().
longest_wpi(Hours) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_wpi(hours :: [integer]) :: integer
  def longest_wpi(hours) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestWPI(hours: Array<Int64>): Int64 {

    }
}
```

