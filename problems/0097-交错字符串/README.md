# 97. 交错字符串

## 题目描述

<p>给定三个字符串&nbsp;<code>s1</code>、<code>s2</code>、<code>s3</code>，请你帮忙验证&nbsp;<code>s3</code>&nbsp;是否是由&nbsp;<code>s1</code>&nbsp;和&nbsp;<code>s2</code><em> </em><strong>交错 </strong>组成的。</p>

<p>两个字符串 <code>s</code> 和 <code>t</code> <strong>交错</strong> 的定义与过程如下，其中每个字符串都会被分割成若干 <strong>非空</strong> <span data-keyword="substring-nonempty">子字符串</span>：</p>

<ul>
	<li><code>s = s<sub>1</sub> + s<sub>2</sub> + ... + s<sub>n</sub></code></li>
	<li><code>t = t<sub>1</sub> + t<sub>2</sub> + ... + t<sub>m</sub></code></li>
	<li><code>|n - m| &lt;= 1</code></li>
	<li><strong>交错</strong> 是 <code>s<sub>1</sub> + t<sub>1</sub> + s<sub>2</sub> + t<sub>2</sub> + s<sub>3</sub> + t<sub>3</sub> + ...</code> 或者 <code>t<sub>1</sub> + s<sub>1</sub> + t<sub>2</sub> + s<sub>2</sub> + t<sub>3</sub> + s<sub>3</sub> + ...</code></li>
</ul>

<p><strong>注意：</strong><code>a + b</code> 意味着字符串 <code>a</code> 和 <code>b</code> 连接。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg" />
<pre>
<strong>输入：</strong>s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s1 = "", s2 = "", s3 = ""
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s1.length, s2.length &lt;= 100</code></li>
	<li><code>0 &lt;= s3.length &lt;= 200</code></li>
	<li><code>s1</code>、<code>s2</code>、和 <code>s3</code> 都由小写英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>您能否仅使用 <code>O(s2.length)</code> 额外的内存空间来解决它?</p>


## 难度

Medium

## 标签

- 字符串
- 动态规划

## 示例

```
"aabcc"
"dbbca"
"aadbbcbcac"
"aabcc"
"dbbca"
"aadbbbaccc"
""
""
""
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
```

### C

```c
bool isInterleave(char* s1, char* s2, char* s3) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsInterleave(string s1, string s2, string s3) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
var isInterleave = function(s1, s2, s3) {
    
};
```

### TypeScript

```typescript
function isInterleave(s1: string, s2: string, s3: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @param String $s3
     * @return Boolean
     */
    function isInterleave($s1, $s2, $s3) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isInterleave(_ s1: String, _ s2: String, _ s3: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isInterleave(s1: String, s2: String, s3: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isInterleave(String s1, String s2, String s3) {
    
  }
}
```

### Go

```golang
func isInterleave(s1 string, s2 string, s3 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @param {String} s3
# @return {Boolean}
def is_interleave(s1, s2, s3)
    
end
```

### Scala

```scala
object Solution {
    def isInterleave(s1: String, s2: String, s3: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-interleave s1 s2 s3)
  (-> string? string? string? boolean?)
  )
```

### Erlang

```erlang
-spec is_interleave(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary(), S3 :: unicode:unicode_binary()) -> boolean().
is_interleave(S1, S2, S3) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_interleave(s1 :: String.t, s2 :: String.t, s3 :: String.t) :: boolean
  def is_interleave(s1, s2, s3) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isInterleave(s1: String, s2: String, s3: String): Bool {

    }
}
```

