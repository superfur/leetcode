# 2380. 二进制字符串重新安排顺序需要的时间

## 题目描述

<p>给你一个二进制字符串&nbsp;<code>s</code>&nbsp;。在一秒之中，<strong>所有</strong>&nbsp;子字符串&nbsp;<code>"01"</code> <strong>同时</strong>&nbsp;被替换成&nbsp;<code>"10"</code>&nbsp;。这个过程持续进行到没有&nbsp;<code>"01"</code>&nbsp;存在。</p>

<p>请你返回完成这个过程所需要的秒数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "0110101"
<b>输出：</b>4
<b>解释：</b>
一秒后，s 变成 "1011010" 。
再过 1 秒后，s 变成 "1101100" 。
第三秒过后，s 变成 "1110100" 。
第四秒后，s 变成 "1111000" 。
此时没有 "01" 存在，整个过程花费 4 秒。
所以我们返回 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "11100"
<b>输出：</b>0
<strong>解释：</strong>
s 中没有 "01" 存在，整个过程花费 0 秒。
所以我们返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code>&nbsp;要么是&nbsp;<code>'0'</code>&nbsp;，要么是&nbsp;<code>'1'</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<p>你能以 O(n) 的时间复杂度解决这个问题吗？</p>


## 难度

Medium

## 标签

- 字符串
- 动态规划
- 模拟

## 提示

1. Try replicating the steps from the problem statement.
2. Perform the replacements simultaneously, and return the number of times the process repeats.

## 示例

```
"0110101"
"11100"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int secondsToRemoveOccurrences(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int secondsToRemoveOccurrences(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def secondsToRemoveOccurrences(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        
```

### C

```c
int secondsToRemoveOccurrences(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int SecondsToRemoveOccurrences(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var secondsToRemoveOccurrences = function(s) {
    
};
```

### TypeScript

```typescript
function secondsToRemoveOccurrences(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function secondsToRemoveOccurrences($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func secondsToRemoveOccurrences(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun secondsToRemoveOccurrences(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int secondsToRemoveOccurrences(String s) {
    
  }
}
```

### Go

```golang
func secondsToRemoveOccurrences(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def seconds_to_remove_occurrences(s)
    
end
```

### Scala

```scala
object Solution {
    def secondsToRemoveOccurrences(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn seconds_to_remove_occurrences(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (seconds-to-remove-occurrences s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec seconds_to_remove_occurrences(S :: unicode:unicode_binary()) -> integer().
seconds_to_remove_occurrences(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec seconds_to_remove_occurrences(s :: String.t) :: integer
  def seconds_to_remove_occurrences(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func secondsToRemoveOccurrences(s: String): Int64 {

    }
}
```

