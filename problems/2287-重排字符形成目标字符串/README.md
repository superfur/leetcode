# 2287. 重排字符形成目标字符串

## 题目描述

<p>给你两个下标从 <strong>0</strong> 开始的字符串 <code>s</code> 和 <code>target</code> 。你可以从 <code>s</code> 取出一些字符并将其重排，得到若干新的字符串。</p>

<p>从 <code>s</code> 中取出字符并重新排列，返回可以形成 <code>target</code> 的 <strong>最大</strong> 副本数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ilovecodingonleetcode", target = "code"
<strong>输出：</strong>2
<strong>解释：</strong>
对于 "code" 的第 1 个副本，选取下标为 4 、5 、6 和 7 的字符。
对于 "code" 的第 2 个副本，选取下标为 17 、18 、19 和 20 的字符。
形成的字符串分别是 "ecod" 和 "code" ，都可以重排为 "code" 。
可以形成最多 2 个 "code" 的副本，所以返回 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcba", target = "abc"
<strong>输出：</strong>1
<strong>解释：</strong>
选取下标为 0 、1 和 2 的字符，可以形成 "abc" 的 1 个副本。 
可以形成最多 1 个 "abc" 的副本，所以返回 1 。
注意，尽管下标 3 和 4 分别有额外的 'a' 和 'b' ，但不能重用下标 2 处的 'c' ，所以无法形成 "abc" 的第 2 个副本。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "abbaccaddaeea", target = "aaaaa"
<strong>输出：</strong>1
<strong>解释：</strong>
选取下标为 0 、3 、6 、9 和 12 的字符，可以形成 "aaaaa" 的 1 个副本。
可以形成最多 1 个 "aaaaa" 的副本，所以返回 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>1 &lt;= target.length &lt;= 10</code></li>
	<li><code>s</code> 和 <code>target</code> 由小写英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与&nbsp;<a href="https://leetcode.cn/problems/maximum-number-of-balloons/">1189. “气球” 的最大数量</a> 相同。</p>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. Count the frequency of each character in s and target.
2. Consider each letter one at a time. If there are x occurrences of a letter in s and y occurrences of the same letter in target, how many copies of this letter can we make?
3. We can make floor(x / y) copies of the letter.

## 示例

```
"ilovecodingonleetcode"
"code"
"abcba"
"abc"
"abbaccaddaeea"
"aaaaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int rearrangeCharacters(string s, string target) {
        
    }
};
```

### Java

```java
class Solution {
    public int rearrangeCharacters(String s, String target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        
```

### C

```c
int rearrangeCharacters(char* s, char* target) {
    
}
```

### C#

```csharp
public class Solution {
    public int RearrangeCharacters(string s, string target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} target
 * @return {number}
 */
var rearrangeCharacters = function(s, target) {
    
};
```

### TypeScript

```typescript
function rearrangeCharacters(s: string, target: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $target
     * @return Integer
     */
    function rearrangeCharacters($s, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func rearrangeCharacters(_ s: String, _ target: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun rearrangeCharacters(s: String, target: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int rearrangeCharacters(String s, String target) {
    
  }
}
```

### Go

```golang
func rearrangeCharacters(s string, target string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} target
# @return {Integer}
def rearrange_characters(s, target)
    
end
```

### Scala

```scala
object Solution {
    def rearrangeCharacters(s: String, target: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn rearrange_characters(s: String, target: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (rearrange-characters s target)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec rearrange_characters(S :: unicode:unicode_binary(), Target :: unicode:unicode_binary()) -> integer().
rearrange_characters(S, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec rearrange_characters(s :: String.t, target :: String.t) :: integer
  def rearrange_characters(s, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func rearrangeCharacters(s: String, target: String): Int64 {

    }
}
```

