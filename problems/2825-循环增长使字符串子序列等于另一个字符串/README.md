# 2825. 循环增长使字符串子序列等于另一个字符串

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>str1</code> 和&nbsp;<code>str2</code>&nbsp;。</p>

<p>一次操作中，你选择&nbsp;<code>str1</code>&nbsp;中的若干下标。对于选中的每一个下标&nbsp;<code>i</code>&nbsp;，你将&nbsp;<code>str1[i]</code>&nbsp;<strong>循环</strong>&nbsp;递增，变成下一个字符。也就是说&nbsp;<code>'a'</code>&nbsp;变成&nbsp;<code>'b'</code>&nbsp;，<code>'b'</code> 变成&nbsp;<code>'c'</code>&nbsp;，以此类推，<code>'z'</code> 变成&nbsp;<code>'a'</code>&nbsp;。</p>

<p>如果执行以上操作 <strong>至多一次</strong>&nbsp;，可以让 <code>str2</code>&nbsp;成为 <code>str1</code>&nbsp;的子序列，请你返回 <code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p><b>注意：</b>一个字符串的子序列指的是从原字符串中删除一些（可以一个字符也不删）字符后，剩下字符按照原本先后顺序组成的新字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>str1 = "abc", str2 = "ad"
<b>输出：</b>true
<b>解释：</b>选择 str1 中的下标 2 。
将 str1[2] 循环递增，得到 'd' 。
因此，str1 变成 "abd" 且 str2 现在是一个子序列。所以返回 true 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>str1 = "zc", str2 = "ad"
<b>输出：</b>true
<b>解释：</b>选择 str1 中的下标 0 和 1 。
将 str1[0] 循环递增得到 'a' 。
将 str1[1] 循环递增得到 'd' 。
因此，str1 变成 "ad" 且 str2 现在是一个子序列。所以返回 true 。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>str1 = "ab", str2 = "d"
<b>输出：</b>false
<b>解释：</b>这个例子中，没法在执行一次操作的前提下，将 str2 变为 str1 的子序列。
所以返回 false 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= str1.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= str2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>str1</code>&nbsp;和&nbsp;<code>str2</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 双指针
- 字符串

## 提示

1. <div class="_1l1MA">Consider the indices we will increment separately.</div>
2. <div class="_1l1MA">We can maintain two pointers: pointer <code>i</code> for <code>str1</code> and pointer <code>j</code> for <code>str2</code>, while ensuring they remain within the bounds of the strings.</div>
3. <div class="_1l1MA">If both <code>str1[i]</code> and <code>str2[j]</code> match, or if incrementing <code>str1[i]</code> matches <code>str2[j]</code>, we increase both pointers; otherwise, we increment only pointer <code>i</code>.</div>
4. <div class="_1l1MA">It is possible to make <code>str2</code> a subsequence of <code>str1</code> if <code>j</code> is at the end of <code>str2</code>, after we can no longer find a match.</div>

## 示例

```
"abc"
"ad"
"zc"
"ad"
"ab"
"d"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canMakeSubsequence(String str1, String str2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
```

### C

```c
bool canMakeSubsequence(char* str1, char* str2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanMakeSubsequence(string str1, string str2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} str1
 * @param {string} str2
 * @return {boolean}
 */
var canMakeSubsequence = function(str1, str2) {
    
};
```

### TypeScript

```typescript
function canMakeSubsequence(str1: string, str2: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $str1
     * @param String $str2
     * @return Boolean
     */
    function canMakeSubsequence($str1, $str2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canMakeSubsequence(_ str1: String, _ str2: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canMakeSubsequence(str1: String, str2: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canMakeSubsequence(String str1, String str2) {
    
  }
}
```

### Go

```golang
func canMakeSubsequence(str1 string, str2 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} str1
# @param {String} str2
# @return {Boolean}
def can_make_subsequence(str1, str2)
    
end
```

### Scala

```scala
object Solution {
    def canMakeSubsequence(str1: String, str2: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_make_subsequence(str1: String, str2: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-make-subsequence str1 str2)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec can_make_subsequence(Str1 :: unicode:unicode_binary(), Str2 :: unicode:unicode_binary()) -> boolean().
can_make_subsequence(Str1, Str2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_make_subsequence(str1 :: String.t, str2 :: String.t) :: boolean
  def can_make_subsequence(str1, str2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canMakeSubsequence(str1: String, str2: String): Bool {

    }
}
```

