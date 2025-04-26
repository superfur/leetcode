# 2565. 最少得分子序列

## 题目描述

<p>给你两个字符串&nbsp;<code>s</code> 和&nbsp;<code>t</code>&nbsp;。</p>

<p>你可以从字符串 <code>t</code>&nbsp;中删除任意数目的字符。</p>

<p>如果没有从字符串&nbsp;<code>t</code>&nbsp;中删除字符，那么得分为&nbsp;<code>0</code>&nbsp;，否则：</p>

<ul>
	<li>令&nbsp;<code>left</code>&nbsp;为删除字符中的最小下标。</li>
	<li>令&nbsp;<code>right</code>&nbsp;为删除字符中的最大下标。</li>
</ul>

<p>字符串的得分为&nbsp;<code>right - left + 1</code>&nbsp;。</p>

<p>请你返回使<em>&nbsp;</em><code>t</code><em> </em>成为<em>&nbsp;</em><code>s</code>&nbsp;子序列的最小得分。</p>

<p>一个字符串的 <strong>子序列</strong>&nbsp;是从原字符串中删除一些字符后（也可以一个也不删除），剩余字符不改变顺序得到的字符串。（比方说&nbsp;<code>"ace"</code> 是&nbsp;<code>"<strong><em>a</em></strong>b<strong><em>c</em></strong>d<strong><em>e</em></strong>"</code>&nbsp;的子序列，但是&nbsp;<code>"aec"</code>&nbsp;不是）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "abacaba", t = "bzaa"
<b>输出：</b>1
<b>解释：</b>这个例子中，我们删除下标 1 处的字符 "z" （下标从 0 开始）。
字符串 t 变为 "baa" ，它是字符串 "abacaba" 的子序列，得分为 1 - 1 + 1 = 1 。
1 是能得到的最小得分。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "cde", t = "xyz"
<b>输出：</b>3
<b>解释：</b>这个例子中，我们将下标为 0， 1 和 2 处的字符 "x" ，"y" 和 "z" 删除（下标从 0 开始）。
字符串变成 "" ，它是字符串 "cde" 的子序列，得分为 2 - 0 + 1 = 3 。
3 是能得到的最小得分。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 和&nbsp;<code>t</code>&nbsp;都只包含小写英文字母。</li>
</ul>

<p>&nbsp;</p>


## 难度

Hard

## 标签

- 双指针
- 字符串
- 二分查找

## 提示

1. Maintain two pointers: i and j. We need to perform a similar operation: while t[0:i] + t[j:n] is not a subsequence of the string s, increase j.
2. We can check the condition greedily. Create the array leftmost[i] which denotes minimum index k, such that in prefix s[0:k] exists subsequence t[0:i]. Similarly, we define rightmost[i].
3. If leftmost[i] < rightmost[j] then t[0:i] + t[j:n] is the subsequence of s.

## 示例

```
"abacaba"
"bzaa"
"cde"
"xyz"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumScore(string s, string t) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumScore(String s, String t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumScore(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        
```

### C

```c
int minimumScore(char* s, char* t) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumScore(string s, string t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var minimumScore = function(s, t) {
    
};
```

### TypeScript

```typescript
function minimumScore(s: string, t: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function minimumScore($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumScore(_ s: String, _ t: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumScore(s: String, t: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumScore(String s, String t) {
    
  }
}
```

### Go

```golang
func minimumScore(s string, t string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Integer}
def minimum_score(s, t)
    
end
```

### Scala

```scala
object Solution {
    def minimumScore(s: String, t: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_score(s: String, t: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-score s t)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_score(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
minimum_score(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_score(s :: String.t, t :: String.t) :: integer
  def minimum_score(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumScore(s: String, t: String): Int64 {

    }
}
```

