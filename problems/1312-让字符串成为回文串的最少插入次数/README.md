# 1312. 让字符串成为回文串的最少插入次数

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，每一次操作你都可以在字符串的任意位置插入任意字符。</p>

<p>请你返回让&nbsp;<code>s</code>&nbsp;成为回文串的&nbsp;<strong>最少操作次数</strong>&nbsp;。</p>

<p>「回文串」是正读和反读都相同的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "zzazz"
<strong>输出：</strong>0
<strong>解释：</strong>字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "mbadm"
<strong>输出：</strong>2
<strong>解释：</strong>字符串可变为 "mbdadbm" 或者 "mdbabdm" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "leetcode"
<strong>输出：</strong>5
<strong>解释：</strong>插入 5 个字符后字符串变为 "leetcodocteel" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code>&nbsp;中所有字符都是小写字母。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. Is dynamic programming suitable for this problem ?
2. If we know the longest palindromic sub-sequence is x and the length of the string is n then, what is the answer to this problem? It is n - x as we need n - x insertions to make the remaining characters also palindrome.

## 示例

```
"zzazz"
"mbadm"
"leetcode"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minInsertions(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minInsertions(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minInsertions(self, s: str) -> int:
        
```

### C

```c
int minInsertions(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinInsertions(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minInsertions = function(s) {
    
};
```

### TypeScript

```typescript
function minInsertions(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minInsertions($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minInsertions(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minInsertions(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minInsertions(String s) {
    
  }
}
```

### Go

```golang
func minInsertions(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def min_insertions(s)
    
end
```

### Scala

```scala
object Solution {
    def minInsertions(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_insertions(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-insertions s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_insertions(S :: unicode:unicode_binary()) -> integer().
min_insertions(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_insertions(s :: String.t) :: integer
  def min_insertions(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minInsertions(s: String): Int64 {

    }
}
```

