# 2160. 拆分数位后四位数字的最小和

## 题目描述

<p>给你一个四位&nbsp;<strong>正</strong>&nbsp;整数&nbsp;<code>num</code>&nbsp;。请你使用 <code>num</code>&nbsp;中的 <strong>数位</strong> ，将&nbsp;<code>num</code>&nbsp;拆成两个新的整数&nbsp;<code>new1</code>&nbsp;和&nbsp;<code>new2</code>&nbsp;。<code>new1</code> 和&nbsp;<code>new2</code>&nbsp;中可以有&nbsp;<strong>前导 0</strong>&nbsp;，且&nbsp;<code>num</code>&nbsp;中 <strong>所有</strong>&nbsp;数位都必须使用。</p>

<ul>
	<li>比方说，给你&nbsp;<code>num = 2932</code>&nbsp;，你拥有的数位包括：两个&nbsp;<code>2</code>&nbsp;，一个&nbsp;<code>9</code>&nbsp;和一个&nbsp;<code>3</code>&nbsp;。一些可能的&nbsp;<code>[new1, new2]</code>&nbsp;数对为&nbsp;<code>[22, 93]</code>，<code>[23, 92]</code>，<code>[223, 9]</code> 和&nbsp;<code>[2, 329]</code>&nbsp;。</li>
</ul>

<p>请你返回可以得到的&nbsp;<code>new1</code>&nbsp;和 <code>new2</code>&nbsp;的 <strong>最小</strong>&nbsp;和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>num = 2932
<b>输出：</b>52
<b>解释：</b>可行的 [new1, new2] 数对为 [29, 23] ，[223, 9] 等等。
最小和为数对 [29, 23] 的和：29 + 23 = 52 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>num = 4009
<b>输出：</b>13
<b>解释：</b>可行的 [new1, new2] 数对为 [0, 49] ，[490, 0] 等等。
最小和为数对 [4, 9] 的和：4 + 9 = 13 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1000 &lt;= num &lt;= 9999</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数学
- 排序

## 提示

1. Notice that the most optimal way to obtain the minimum possible sum using 4 digits is by summing up two 2-digit numbers.
2. We can use the two smallest digits out of the four as the digits found in the tens place respectively.
3. Similarly, we use the final 2 larger digits as the digits found in the ones place.

## 示例

```
2932
4009
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumSum(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumSum(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumSum(self, num: int) -> int:
        
```

### C

```c
int minimumSum(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumSum(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var minimumSum = function(num) {
    
};
```

### TypeScript

```typescript
function minimumSum(num: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function minimumSum($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumSum(_ num: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumSum(num: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumSum(int num) {
    
  }
}
```

### Go

```golang
func minimumSum(num int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer}
def minimum_sum(num)
    
end
```

### Scala

```scala
object Solution {
    def minimumSum(num: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_sum(num: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-sum num)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_sum(Num :: integer()) -> integer().
minimum_sum(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_sum(num :: integer) :: integer
  def minimum_sum(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumSum(num: Int64): Int64 {

    }
}
```

