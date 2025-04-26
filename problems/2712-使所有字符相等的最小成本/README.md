# 2712. 使所有字符相等的最小成本

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的二进制字符串 <code>s</code> ，你可以对其执行两种操作：</p>

<ul>
	<li>选中一个下标 <code>i</code> 并且反转从下标 <code>0</code> 到下标 <code>i</code>（包括下标 <code>0</code> 和下标 <code>i</code> ）的所有字符，成本为 <code>i + 1</code> 。</li>
	<li>选中一个下标 <code>i</code> 并且反转从下标 <code>i</code> 到下标 <code>n - 1</code>（包括下标 <code>i</code> 和下标 <code>n - 1</code> ）的所有字符，成本为 <code>n - i</code> 。</li>
</ul>

<p>返回使字符串内所有字符 <strong>相等</strong> 需要的 <strong>最小成本</strong> 。</p>

<p><strong>反转</strong> 字符意味着：如果原来的值是 '0' ，则反转后值变为 '1' ，反之亦然。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "0011"
<strong>输出：</strong>2
<strong>解释：</strong>执行第二种操作，选中下标 <code>i = 2</code> ，可以得到 <code>s = "0000" ，成本为 2</code> 。可以证明 2 是使所有字符相等的最小成本。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "010101"
<strong>输出：</strong>9
<strong>解释：</strong>执行第一种操作，选中下标 i = 2 ，可以得到 s = "101101" ，成本为 3 。
执行第一种操作，选中下标 i = 1 ，可以得到 s = "011101" ，成本为 2 。
执行第一种操作，选中下标 i = 0 ，可以得到 s = "111101" ，成本为 1 。
执行第二种操作，选中下标 i = 4 ，可以得到 s = "111110" ，成本为 2 。
执行第二种操作，选中下标 i = 5 ，可以得到 s = "111111" ，成本为 1 。
使所有字符相等的总成本等于 9 。可以证明 9 是使所有字符相等的最小成本。 </pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length == n &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串
- 动态规划

## 提示

1. For every index i, calculate the number of operations required to make the prefix [0, i - 1] equal to the character at index i, denoted prefix[i].
2. For every index i, calculate the number of operations required to make the suffix [i + 1, n - 1] equal to the character at index i, denoted suffix[i].
3. The final string will contain at least one character that is left unchanged; Therefore, the answer is the minimum of prefix[i] + suffix[i] for every i in [0, n - 1].

## 示例

```
"0011"
"010101"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumCost(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumCost(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumCost(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumCost(self, s: str) -> int:
        
```

### C

```c
long long minimumCost(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumCost(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumCost = function(s) {
    
};
```

### TypeScript

```typescript
function minimumCost(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumCost($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumCost(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCost(s: String): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumCost(String s) {
    
  }
}
```

### Go

```golang
func minimumCost(s string) int64 {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def minimum_cost(s)
    
end
```

### Scala

```scala
object Solution {
    def minimumCost(s: String): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_cost(s: String) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-cost s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_cost(S :: unicode:unicode_binary()) -> integer().
minimum_cost(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(s :: String.t) :: integer
  def minimum_cost(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCost(s: String): Int64 {

    }
}
```

