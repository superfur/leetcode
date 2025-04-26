# 1456. 定长子串中元音的最大数目

## 题目描述

<p>给你字符串 <code>s</code> 和整数 <code>k</code> 。</p>

<p>请返回字符串 <code>s</code> 中长度为 <code>k</code> 的单个子字符串中可能包含的最大元音字母数。</p>

<p>英文中的 <strong>元音字母 </strong>为（<code>a</code>, <code>e</code>, <code>i</code>, <code>o</code>, <code>u</code>）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;abciiidef&quot;, k = 3
<strong>输出：</strong>3
<strong>解释：</strong>子字符串 &quot;iii&quot; 包含 3 个元音字母。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;aeiou&quot;, k = 2
<strong>输出：</strong>2
<strong>解释：</strong>任意长度为 2 的子字符串都包含 2 个元音字母。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;leetcode&quot;, k = 3
<strong>输出：</strong>2
<strong>解释：</strong>&quot;lee&quot;、&quot;eet&quot; 和 &quot;ode&quot; 都包含 2 个元音字母。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = &quot;rhythms&quot;, k = 4
<strong>输出：</strong>0
<strong>解释：</strong>字符串 s 中不含任何元音字母。
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>s = &quot;tryhard&quot;, k = 4
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>s</code> 由小写英文字母组成</li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 滑动窗口

## 提示

1. Keep a window of size k and maintain the number of vowels in it.
2. Keep moving the window and update the number of vowels while moving. Answer is max number of vowels of any window.

## 示例

```
"abciiidef"
3
"aeiou"
2
"leetcode"
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxVowels(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxVowels(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
```

### C

```c
int maxVowels(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxVowels(string s, int k) {
        
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
var maxVowels = function(s, k) {
    
};
```

### TypeScript

```typescript
function maxVowels(s: string, k: number): number {
    
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
    function maxVowels($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxVowels(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxVowels(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxVowels(String s, int k) {
    
  }
}
```

### Go

```golang
func maxVowels(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_vowels(s, k)
    
end
```

### Scala

```scala
object Solution {
    def maxVowels(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_vowels(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-vowels s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_vowels(S :: unicode:unicode_binary(), K :: integer()) -> integer().
max_vowels(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_vowels(s :: String.t, k :: integer) :: integer
  def max_vowels(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxVowels(s: String, k: Int64): Int64 {

    }
}
```

