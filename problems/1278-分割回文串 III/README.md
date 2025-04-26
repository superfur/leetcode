# 1278. 分割回文串 III

## 题目描述

<p>给你一个由小写字母组成的字符串&nbsp;<code>s</code>，和一个整数&nbsp;<code>k</code>。</p>

<p>请你按下面的要求分割字符串：</p>

<ul>
	<li>首先，你可以将&nbsp;<code>s</code>&nbsp;中的部分字符修改为其他的小写英文字母。</li>
	<li>接着，你需要把&nbsp;<code>s</code>&nbsp;分割成&nbsp;<code>k</code>&nbsp;个非空且不相交的子串，并且每个子串都是回文串。</li>
</ul>

<p>请返回以这种方式分割字符串所需修改的最少字符数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;abc&quot;, k = 2
<strong>输出：</strong>1
<strong>解释：</strong>你可以把字符串分割成 &quot;ab&quot; 和 &quot;c&quot;，并修改 &quot;ab&quot; 中的 1 个字符，将它变成回文串。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;aabbc&quot;, k = 3
<strong>输出：</strong>0
<strong>解释：</strong>你可以把字符串分割成 &quot;aa&quot;、&quot;bb&quot; 和 &quot;c&quot;，它们都是回文串。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;leetcode&quot;, k = 8
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code>&nbsp;中只含有小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. For each substring calculate the minimum number of steps to make it palindrome and store it in a table.
2. Create a dp(pos, cnt) which means the minimum number of characters changed for the suffix of s starting on pos splitting the suffix on cnt chunks.

## 示例

```
"abc"
2
"aabbc"
3
"leetcode"
8
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int palindromePartition(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int palindromePartition(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        
```

### C

```c
int palindromePartition(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int PalindromePartition(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var palindromePartition = function(s, k) {
    
};
```

### TypeScript

```typescript
function palindromePartition(s: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function palindromePartition($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func palindromePartition(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun palindromePartition(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int palindromePartition(String s, int k) {
    
  }
}
```

### Go

```golang
func palindromePartition(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def palindrome_partition(s, k)
    
end
```

### Scala

```scala
object Solution {
    def palindromePartition(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn palindrome_partition(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (palindrome-partition s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec palindrome_partition(S :: unicode:unicode_binary(), K :: integer()) -> integer().
palindrome_partition(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec palindrome_partition(s :: String.t, k :: integer) :: integer
  def palindrome_partition(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func palindromePartition(s: String, k: Int64): Int64 {

    }
}
```

