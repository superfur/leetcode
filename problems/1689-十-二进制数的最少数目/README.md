# 1689. 十-二进制数的最少数目

## 题目描述

<p>如果一个十进制数字不含任何前导零，且每一位上的数字不是 <code>0</code> 就是 <code>1</code> ，那么该数字就是一个 <strong>十-二进制数</strong> 。例如，<code>101</code> 和 <code>1100</code> 都是 <strong>十-二进制数</strong>，而 <code>112</code> 和 <code>3001</code> 不是。</p>

<p>给你一个表示十进制整数的字符串 <code>n</code> ，返回和为 <code>n</code> 的 <strong>十-二进制数 </strong>的最少数目。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = "32"
<strong>输出：</strong>3
<strong>解释：</strong>10 + 11 + 11 = 32
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = "82734"
<strong>输出：</strong>8
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = "27346209830709182346"
<strong>输出：</strong>9
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n.length &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> 仅由数字组成</li>
	<li><code>n</code> 不含任何前导零并总是表示正整数</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串

## 提示

1. Think about if the input was only one digit. Then you need to add up as many ones as the value of this digit.
2. If the input has multiple digits, then you can solve for each digit independently, and merge the answers to form numbers that add up to that input.
3. Thus the answer is equal to the max digit.

## 示例

```
"32"
"82734"
"27346209830709182346"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minPartitions(string n) {
        
    }
};
```

### Java

```java
class Solution {
    public int minPartitions(String n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minPartitions(self, n: str) -> int:
        
```

### C

```c
int minPartitions(char* n) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinPartitions(string n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} n
 * @return {number}
 */
var minPartitions = function(n) {
    
};
```

### TypeScript

```typescript
function minPartitions(n: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $n
     * @return Integer
     */
    function minPartitions($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minPartitions(_ n: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minPartitions(n: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minPartitions(String n) {
    
  }
}
```

### Go

```golang
func minPartitions(n string) int {
    
}
```

### Ruby

```ruby
# @param {String} n
# @return {Integer}
def min_partitions(n)
    
end
```

### Scala

```scala
object Solution {
    def minPartitions(n: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_partitions(n: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-partitions n)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_partitions(N :: unicode:unicode_binary()) -> integer().
min_partitions(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_partitions(n :: String.t) :: integer
  def min_partitions(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minPartitions(n: String): Int64 {

    }
}
```

