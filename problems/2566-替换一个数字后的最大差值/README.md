# 2566. 替换一个数字后的最大差值

## 题目描述

<p>给你一个整数&nbsp;<code>num</code>&nbsp;。你知道 Danny Mittal 会偷偷将 <code>0</code>&nbsp;到 <code>9</code>&nbsp;中的一个数字 <strong>替换</strong> 成另一个数字。</p>

<p>请你返回将 <code>num</code>&nbsp;中&nbsp;<strong>恰好一个</strong>&nbsp;数字进行替换后，得到的最大值和最小值的差为多少。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>当 Danny 将一个数字 <code>d1</code> 替换成另一个数字 <code>d2</code> 时，Danny 需要将&nbsp;<code>nums</code>&nbsp;中所有 <code>d1</code>&nbsp;都替换成&nbsp;<code>d2</code>&nbsp;。</li>
	<li>Danny 可以将一个数字替换成它自己，也就是说&nbsp;<code>num</code>&nbsp;可以不变。</li>
	<li>Danny 可以将数字分别替换成两个不同的数字分别得到最大值和最小值。</li>
	<li>替换后得到的数字可以包含前导 0 。</li>
	<li>Danny Mittal 获得周赛 326 前 10 名，让我们恭喜他。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>num = 11891
<b>输出：</b>99009
<b>解释：</b>
为了得到最大值，我们将数字 1 替换成数字 9 ，得到 99899 。
为了得到最小值，我们将数字 1 替换成数字 0 ，得到 890 。
两个数字的差值为 99009 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>num = 90
<b>输出：</b>99
<strong>解释：</strong>
可以得到的最大值是 99（将 0 替换成 9），最小值是 0（将 9 替换成 0）。
所以我们得到 99 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>8</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数学

## 提示

1. Try to remap the first non-nine digit to 9 to obtain the maximum number.
2. Try to remap the first non-zero digit to 0 to obtain the minimum number.

## 示例

```
11891
90
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minMaxDifference(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public int minMaxDifference(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minMaxDifference(self, num: int) -> int:
        
```

### C

```c
int minMaxDifference(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinMaxDifference(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var minMaxDifference = function(num) {
    
};
```

### TypeScript

```typescript
function minMaxDifference(num: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function minMaxDifference($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minMaxDifference(_ num: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minMaxDifference(num: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minMaxDifference(int num) {
    
  }
}
```

### Go

```golang
func minMaxDifference(num int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer}
def min_max_difference(num)
    
end
```

### Scala

```scala
object Solution {
    def minMaxDifference(num: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_max_difference(num: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-max-difference num)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_max_difference(Num :: integer()) -> integer().
min_max_difference(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_max_difference(num :: integer) :: integer
  def min_max_difference(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minMaxDifference(num: Int64): Int64 {

    }
}
```

