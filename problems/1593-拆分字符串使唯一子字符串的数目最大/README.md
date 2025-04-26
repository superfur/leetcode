# 1593. 拆分字符串使唯一子字符串的数目最大

## 题目描述

<p>给你一个字符串 <code>s</code> ，请你拆分该字符串，并返回拆分后唯一子字符串的最大数目。</p>

<p>字符串 <code>s</code> 拆分后可以得到若干 <strong>非空子字符串</strong> ，这些子字符串连接后应当能够还原为原字符串。但是拆分出来的每个子字符串都必须是 <strong>唯一的</strong> 。</p>

<p>注意：<strong>子字符串</strong> 是字符串中的一个连续字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;ababccc&quot;
<strong>输出：</strong>5
<strong>解释：</strong>一种最大拆分方法为 [&#39;a&#39;, &#39;b&#39;, &#39;ab&#39;, &#39;c&#39;, &#39;cc&#39;] 。像 [&#39;a&#39;, &#39;b&#39;, &#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;cc&#39;] 这样拆分不满足题目要求，因为其中的 &#39;a&#39; 和 &#39;b&#39; 都出现了不止一次。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;aba&quot;
<strong>输出：</strong>2
<strong>解释：</strong>一种最大拆分方法为 [&#39;a&#39;, &#39;ba&#39;] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;aa&quot;
<strong>输出：</strong>1
<strong>解释：</strong>无法进一步拆分字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>
	<p><code>1 &lt;= s.length&nbsp;&lt;= 16</code></p>
	</li>
	<li>
	<p><code>s</code> 仅包含小写英文字母</p>
	</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 回溯

## 提示

1. Use a set to keep track of which substrings have been used already
2. Try each possible substring at every position and backtrack if a complete split is not possible

## 示例

```
"ababccc"
"aba"
"aa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxUniqueSplit(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxUniqueSplit(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
```

### C

```c
int maxUniqueSplit(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxUniqueSplit(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxUniqueSplit = function(s) {
    
};
```

### TypeScript

```typescript
function maxUniqueSplit(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxUniqueSplit($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxUniqueSplit(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxUniqueSplit(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxUniqueSplit(String s) {
    
  }
}
```

### Go

```golang
func maxUniqueSplit(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def max_unique_split(s)
    
end
```

### Scala

```scala
object Solution {
    def maxUniqueSplit(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_unique_split(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-unique-split s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_unique_split(S :: unicode:unicode_binary()) -> integer().
max_unique_split(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_unique_split(s :: String.t) :: integer
  def max_unique_split(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxUniqueSplit(s: String): Int64 {

    }
}
```

