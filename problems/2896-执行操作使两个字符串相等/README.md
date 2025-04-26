# 2896. 执行操作使两个字符串相等

## 题目描述

<p>给你两个下标从 <strong>0</strong>&nbsp;开始的二进制字符串&nbsp;<code>s1</code> 和&nbsp;<code>s2</code>&nbsp;，两个字符串的长度都是&nbsp;<code>n</code>&nbsp;，再给你一个正整数&nbsp;<code>x</code>&nbsp;。</p>

<p>你可以对字符串 <code>s1</code>&nbsp;执行以下操作 <strong>任意次</strong>&nbsp;：</p>

<ul>
	<li>选择两个下标&nbsp;<code>i</code>&nbsp;和&nbsp;<code>j</code>&nbsp;，将&nbsp;<code>s1[i]</code> 和&nbsp;<code>s1[j]</code>&nbsp;都反转，操作的代价为&nbsp;<code>x</code>&nbsp;。</li>
	<li>选择满足 <code>i &lt; n - 1</code>&nbsp;的下标&nbsp;<code>i</code>&nbsp;，反转&nbsp;<code>s1[i]</code> 和&nbsp;<code>s1[i + 1]</code>&nbsp;，操作的代价为&nbsp;<code>1</code>&nbsp;。</li>
</ul>

<p>请你返回使字符串&nbsp;<code>s1</code>&nbsp;和&nbsp;<code>s2</code>&nbsp;相等的&nbsp;<strong>最小</strong>&nbsp;操作代价之和，如果无法让二者相等，返回&nbsp;<code>-1</code>&nbsp;。</p>

<p><strong>注意</strong>&nbsp;，反转字符的意思是将&nbsp;<code>0</code>&nbsp;变成&nbsp;<code>1</code>&nbsp;，或者 <code>1</code>&nbsp;变成 <code>0</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>s1 = "1100011000", s2 = "0101001010", x = 2
<b>输出：</b>4
<b>解释：</b>我们可以执行以下操作：
- 选择 i = 3 执行第二个操作。结果字符串是 s1 = "110<em><strong>11</strong></em>11000" 。
- 选择 i = 4 执行第二个操作。结果字符串是 s1 = "1101<em><strong>00</strong></em>1000" 。
- 选择 i = 0 和 j = 8 ，执行第一个操作。结果字符串是 s1 = "<em><strong>0</strong></em>1010010<em><strong>1</strong></em>0" = s2 。
总代价是 1 + 1 + 2 = 4 。这是最小代价和。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>s1 = "10110", s2 = "00011", x = 4
<b>输出：</b>-1
<b>解释：</b>无法使两个字符串相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == s1.length == s2.length</code></li>
	<li><code>1 &lt;= n, x &lt;= 500</code></li>
	<li><code>s1</code> 和&nbsp;<code>s2</code>&nbsp;只包含字符&nbsp;<code>'0'</code> 和&nbsp;<code>'1'</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 动态规划

## 提示

1. Save all the indices that have different characters on <code>s1</code> and <code>s2</code> into a list, and work only with this list.
2. Try to use dynamic programming on this list to solve the problem. What will be the states and transitions of this dp?

## 示例

```
"1100011000"
"0101001010"
2
"10110"
"00011"
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(string s1, string s2, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(String s1, String s2, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, s1, s2, x):
        """
        :type s1: str
        :type s2: str
        :type x: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        
```

### C

```c
int minOperations(char* s1, char* s2, int x) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(string s1, string s2, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @param {number} x
 * @return {number}
 */
var minOperations = function(s1, s2, x) {
    
};
```

### TypeScript

```typescript
function minOperations(s1: string, s2: string, x: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @param Integer $x
     * @return Integer
     */
    function minOperations($s1, $s2, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ s1: String, _ s2: String, _ x: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(s1: String, s2: String, x: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(String s1, String s2, int x) {
    
  }
}
```

### Go

```golang
func minOperations(s1 string, s2 string, x int) int {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @param {Integer} x
# @return {Integer}
def min_operations(s1, s2, x)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(s1: String, s2: String, x: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(s1: String, s2: String, x: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations s1 s2 x)
  (-> string? string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary(), X :: integer()) -> integer().
min_operations(S1, S2, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(s1 :: String.t, s2 :: String.t, x :: integer) :: integer
  def min_operations(s1, s2, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(s1: String, s2: String, x: Int64): Int64 {

    }
}
```

