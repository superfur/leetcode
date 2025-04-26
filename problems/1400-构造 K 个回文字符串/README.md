# 1400. 构造 K 个回文字符串

## 题目描述

<p>给你一个字符串 <code>s</code>&nbsp;和一个整数 <code>k</code>&nbsp;。请你用 <code>s</code>&nbsp;字符串中 <strong>所有字符</strong>&nbsp;构造 <code>k</code>&nbsp;个<strong>非空</strong> <span data-keyword="palindrome-string">回文串</span>&nbsp;。</p>

<p>如果你可以用&nbsp;<code>s</code>&nbsp;中所有字符构造&nbsp;<code>k</code>&nbsp;个回文字符串，那么请你返回 <strong>True</strong>&nbsp;，否则返回&nbsp;<strong>False</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "annabelle", k = 2
<strong>输出：</strong>true
<strong>解释：</strong>可以用 s 中所有字符构造 2 个回文字符串。
一些可行的构造方案包括："anna" + "elble"，"anbna" + "elle"，"anellena" + "b"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "leetcode", k = 3
<strong>输出：</strong>false
<strong>解释：</strong>无法用 s 中所有字符构造 3 个回文串。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "true", k = 4
<strong>输出：</strong>true
<strong>解释：</strong>唯一可行的方案是让 s 中每个字符单独构成一个字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;中所有字符都是小写英文字母。</li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 哈希表
- 字符串
- 计数

## 提示

1. If the s.length < k we cannot construct k strings from s and answer is false.
2. If the number of characters that have odd counts is > k then the minimum number of palindrome strings we can construct is > k and answer is false.
3. Otherwise you can construct exactly k palindrome strings and answer is true (why ?).

## 示例

```
"annabelle"
2
"leetcode"
3
"true"
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canConstruct(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canConstruct(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
```

### C

```c
bool canConstruct(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanConstruct(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var canConstruct = function(s, k) {
    
};
```

### TypeScript

```typescript
function canConstruct(s: string, k: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Boolean
     */
    function canConstruct($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canConstruct(_ s: String, _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canConstruct(s: String, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canConstruct(String s, int k) {
    
  }
}
```

### Go

```golang
func canConstruct(s string, k int) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Boolean}
def can_construct(s, k)
    
end
```

### Scala

```scala
object Solution {
    def canConstruct(s: String, k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_construct(s: String, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-construct s k)
  (-> string? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec can_construct(S :: unicode:unicode_binary(), K :: integer()) -> boolean().
can_construct(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_construct(s :: String.t, k :: integer) :: boolean
  def can_construct(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canConstruct(s: String, k: Int64): Bool {

    }
}
```

