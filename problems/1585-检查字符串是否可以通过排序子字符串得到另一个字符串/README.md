# 1585. 检查字符串是否可以通过排序子字符串得到另一个字符串

## 题目描述

<p>给你两个字符串&nbsp;<code>s</code> 和&nbsp;<code>t</code>&nbsp;，请你通过若干次以下操作将字符串&nbsp;<code>s</code>&nbsp;转化成字符串&nbsp;<code>t</code>&nbsp;：</p>

<ul>
	<li>选择 <code>s</code>&nbsp;中一个 <strong>非空</strong>&nbsp;子字符串并将它包含的字符就地 <strong>升序</strong>&nbsp;排序。</li>
</ul>

<p>比方说，对下划线所示的子字符串进行操作可以由&nbsp;<code>&quot;1<strong>4234</strong>&quot;</code>&nbsp;得到&nbsp;<code>&quot;1<strong>2344</strong>&quot;</code>&nbsp;。</p>

<p>如果可以将字符串 <code>s</code>&nbsp;变成 <code>t</code>&nbsp;，返回 <code>true</code>&nbsp;。否则，返回 <code>false</code>&nbsp;。</p>

<p>一个 <strong>子字符串</strong>&nbsp;定义为一个字符串中连续的若干字符。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;84532&quot;, t = &quot;34852&quot;
<strong>输出：</strong>true
<strong>解释：</strong>你可以按以下操作将 s 转变为 t ：
&quot;84<strong>53</strong>2&quot; （从下标 2 到下标 3）-&gt; &quot;84<strong>35</strong>2&quot;
&quot;<strong>843</strong>52&quot; （从下标 0 到下标 2） -&gt; &quot;<strong>348</strong>52&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;34521&quot;, t = &quot;23415&quot;
<strong>输出：</strong>true
<strong>解释：</strong>你可以按以下操作将 s 转变为 t ：
&quot;<strong>3452</strong>1&quot; -&gt; &quot;<strong>2345</strong>1&quot;
&quot;234<strong>51</strong>&quot; -&gt; &quot;234<strong>15</strong>&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;12345&quot;, t = &quot;12435&quot;
<strong>输出：</strong>false
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;1&quot;, t = &quot;2&quot;
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>s.length == t.length</code></li>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 和&nbsp;<code>t</code>&nbsp;都只包含数字字符，即&nbsp;<code>&#39;0&#39;</code>&nbsp;到&nbsp;<code>&#39;9&#39;</code> 。</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 字符串
- 排序

## 提示

1. Suppose the first digit you need is 'd'. How can you determine if it's possible to get that digit there?
2. Consider swapping adjacent characters to maintain relative ordering.

## 示例

```
"84532"
"34852"
"34521"
"23415"
"12345"
"12435"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isTransformable(string s, string t) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isTransformable(String s, String t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        
```

### C

```c
bool isTransformable(char* s, char* t) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsTransformable(string s, string t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isTransformable = function(s, t) {
    
};
```

### TypeScript

```typescript
function isTransformable(s: string, t: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isTransformable($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isTransformable(_ s: String, _ t: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isTransformable(s: String, t: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isTransformable(String s, String t) {
    
  }
}
```

### Go

```golang
func isTransformable(s string, t string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Boolean}
def is_transformable(s, t)
    
end
```

### Scala

```scala
object Solution {
    def isTransformable(s: String, t: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_transformable(s: String, t: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-transformable s t)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec is_transformable(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> boolean().
is_transformable(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_transformable(s :: String.t, t :: String.t) :: boolean
  def is_transformable(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isTransformable(s: String, t: String): Bool {

    }
}
```

