# 2911. 得到 K 个半回文串的最少修改次数

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;，请你将&nbsp;<code>s</code> 分成&nbsp;<code>k</code>&nbsp;个<strong>&nbsp;子字符串</strong>&nbsp;，使得每个 <strong>子字符串</strong>&nbsp;变成&nbsp;<strong>半回文串</strong>&nbsp;需要修改的字符数目最少。</p>

<p>请你返回一个整数，表示需要修改的 <strong>最少</strong>&nbsp;字符数目。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>如果一个字符串从左往右和从右往左读是一样的，那么它是一个 <strong>回文串</strong>&nbsp;。</li>
	<li>如果长度为 <code>len</code>&nbsp;的字符串存在一个满足&nbsp;<code>1 &lt;= d &lt; len</code>&nbsp;的正整数&nbsp;<code>d</code>&nbsp;，<code>len % d == 0</code>&nbsp;成立且所有对 <code>d</code>&nbsp;做除法余数相同的下标对应的字符连起来得到的字符串都是 <strong>回文串</strong>&nbsp;，那么我们说这个字符串是 <strong>半回文串</strong>&nbsp;。比方说&nbsp;<code>"aa"</code>&nbsp;，<code>"aba"</code> ，<code>"adbgad"</code>&nbsp;和&nbsp;<code>"abab"</code>&nbsp;都是 <strong>半回文串</strong>&nbsp;，而&nbsp;<code>"a"</code>&nbsp;，<code>"ab"</code>&nbsp;和&nbsp;<code>"abca"</code>&nbsp;不是。</li>
	<li><strong>子字符串</strong>&nbsp;指的是一个字符串中一段连续的字符序列。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>s = "abcac", k = 2
<b>输出：</b>1
<b>解释：</b>我们可以将 s 分成子字符串 "ab" 和 "cac" 。子字符串 "cac" 已经是半回文串。如果我们将 "ab" 变成 "aa" ，它也会变成一个 d = 1 的半回文串。
该方案是将 s 分成 2 个子字符串的前提下，得到 2 个半回文子字符串需要的最少修改次数。所以答案为 1 。</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<b>输入：</b>s = "abcdef", k = 2
<b>输出：</b>2
<b>解释：</b>我们可以将 s 分成子字符串 "abc" 和 "def" 。子字符串 "abc" 和 "def" 都需要修改一个字符得到半回文串，所以我们总共需要 2 次字符修改使所有子字符串变成半回文串。
该方案是将 s 分成 2 个子字符串的前提下，得到 2 个半回文子字符串需要的最少修改次数。所以答案为 2 。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>s = "aabbaa", k = 3
<b>输出：</b>0
<b>解释：</b>我们可以将 s 分成子字符串 "aa" ，"bb" 和 "aa" 。
字符串 "aa" 和 "bb" 都已经是半回文串了。所以答案为 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 200</code></li>
	<li><code>1 &lt;= k &lt;= s.length / 2</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 双指针
- 字符串
- 动态规划

## 提示

1. Define <code>dp[i][j]</code> as the minimum count of letter changes needed to split the suffix of string <code>s</code> starting from <code>s[i]</code> into <code>j</code> valid parts.
2. We have <code>dp[i][j] = min(dp[x + 1][j - 1] + v[i][x])</code>. Here <code>v[i][x]</code> is the minimum number of letter changes to change substring <code>s[i..x]</code> into semi-palindrome.
3. <code>v[i][j]</code> can be calculated separately by <b>brute-force</b>. We can create a table of <code>v[i][j]</code> independently to improve the complexity. Also note that semi-palindrome’s length is at least <code>2</code>.

## 示例

```
"abcac"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumChanges(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumChanges(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        
```

### C

```c
int minimumChanges(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumChanges(string s, int k) {
        
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
var minimumChanges = function(s, k) {
    
};
```

### TypeScript

```typescript
function minimumChanges(s: string, k: number): number {
    
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
    function minimumChanges($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumChanges(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumChanges(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumChanges(String s, int k) {
    
  }
}
```

### Go

```golang
func minimumChanges(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def minimum_changes(s, k)
    
end
```

### Scala

```scala
object Solution {
    def minimumChanges(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_changes(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-changes s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_changes(S :: unicode:unicode_binary(), K :: integer()) -> integer().
minimum_changes(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_changes(s :: String.t, k :: integer) :: integer
  def minimum_changes(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumChanges(s: String, k: Int64): Int64 {

    }
}
```

