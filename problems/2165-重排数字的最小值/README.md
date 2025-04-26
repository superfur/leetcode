# 2165. 重排数字的最小值

## 题目描述

<p>给你一个整数 <code>num</code> 。<strong>重排</strong> <code>num</code> 中的各位数字，使其值 <strong>最小化</strong> 且不含 <strong>任何</strong> 前导零。</p>

<p>返回不含前导零且值最小的重排数字。</p>

<p>注意，重排各位数字后，<code>num</code> 的符号不会改变。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>num = 310
<strong>输出：</strong>103
<strong>解释：</strong>310 中各位数字的可行排列有：013、031、103、130、301、310 。
不含任何前导零且值最小的重排数字是 103 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>num = -7605
<strong>输出：</strong>-7650
<strong>解释：</strong>-7605 中各位数字的部分可行排列为：-7650、-6705、-5076、-0567。
不含任何前导零且值最小的重排数字是 -7650 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-10<sup>15</sup> &lt;= num &lt;= 10<sup>15</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 排序

## 提示

1. For positive numbers, the leading digit should be the smallest nonzero digit. Then the remaining digits follow in ascending order.
2. For negative numbers, the digits should be arranged in descending order.

## 示例

```
310
-7605
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long smallestNumber(long long num) {
        
    }
};
```

### Java

```java
class Solution {
    public long smallestNumber(long num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def smallestNumber(self, num: int) -> int:
        
```

### C

```c
long long smallestNumber(long long num) {
    
}
```

### C#

```csharp
public class Solution {
    public long SmallestNumber(long num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var smallestNumber = function(num) {
    
};
```

### TypeScript

```typescript
function smallestNumber(num: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function smallestNumber($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestNumber(_ num: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestNumber(num: Long): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int smallestNumber(int num) {
    
  }
}
```

### Go

```golang
func smallestNumber(num int64) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer}
def smallest_number(num)
    
end
```

### Scala

```scala
object Solution {
    def smallestNumber(num: Long): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_number(num: i64) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-number num)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec smallest_number(Num :: integer()) -> integer().
smallest_number(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_number(num :: integer) :: integer
  def smallest_number(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestNumber(num: Int64): Int64 {

    }
}
```

