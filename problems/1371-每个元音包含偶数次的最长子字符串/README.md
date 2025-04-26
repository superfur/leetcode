# 1371. 每个元音包含偶数次的最长子字符串

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即&nbsp;&#39;a&#39;，&#39;e&#39;，&#39;i&#39;，&#39;o&#39;，&#39;u&#39; ，在子字符串中都恰好出现了偶数次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;eleetminicoworoep&quot;
<strong>输出：</strong>13
<strong>解释：</strong>最长子字符串是 &quot;leetminicowor&quot; ，它包含 <strong>e，i，o</strong>&nbsp;各 2 个，以及 0 个 <strong>a</strong>，<strong>u </strong>。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;leetcodeisgreat&quot;
<strong>输出：</strong>5
<strong>解释：</strong>最长子字符串是 &quot;leetc&quot; ，其中包含 2 个 <strong>e</strong> 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;bcbcbc&quot;
<strong>输出：</strong>6
<strong>解释：</strong>这个示例中，字符串 &quot;bcbcbc&quot; 本身就是最长的，因为所有的元音 <strong>a，</strong><strong>e，</strong><strong>i，</strong><strong>o，</strong><strong>u</strong> 都出现了 0 次。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 x 10^5</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 哈希表
- 字符串
- 前缀和

## 提示

1. Represent the counts (odd or even) of vowels with a bitmask.
2. Precompute the prefix xor for the bitmask of vowels and then get the longest valid substring.

## 示例

```
"eleetminicoworoep"
"leetcodeisgreat"
"bcbcbc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findTheLongestSubstring(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int findTheLongestSubstring(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
```

### C

```c
int findTheLongestSubstring(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindTheLongestSubstring(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var findTheLongestSubstring = function(s) {
    
};
```

### TypeScript

```typescript
function findTheLongestSubstring(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function findTheLongestSubstring($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findTheLongestSubstring(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findTheLongestSubstring(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findTheLongestSubstring(String s) {
    
  }
}
```

### Go

```golang
func findTheLongestSubstring(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def find_the_longest_substring(s)
    
end
```

### Scala

```scala
object Solution {
    def findTheLongestSubstring(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_the_longest_substring(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-the-longest-substring s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_the_longest_substring(S :: unicode:unicode_binary()) -> integer().
find_the_longest_substring(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_the_longest_substring(s :: String.t) :: integer
  def find_the_longest_substring(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findTheLongestSubstring(s: String): Int64 {

    }
}
```

