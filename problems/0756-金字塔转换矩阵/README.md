# 756. 金字塔转换矩阵

## 题目描述

<p>你正在把积木堆成金字塔。每个块都有一个颜色，用一个字母表示。每一行的块比它下面的行 <strong>少一个块</strong> ，并且居中。</p>

<p>为了使金字塔美观，只有特定的 <strong>三角形图案</strong> 是允许的。一个三角形的图案由&nbsp;<strong>两个块</strong>&nbsp;和叠在上面的 <strong>单个块</strong> 组成。模式是以三个字母字符串的列表形式&nbsp;<code>allowed</code>&nbsp;给出的，其中模式的前两个字符分别表示左右底部块，第三个字符表示顶部块。</p>

<ul>
	<li>例如，<code>"ABC"</code>&nbsp;表示一个三角形图案，其中一个 <code>“C”</code> 块堆叠在一个&nbsp;<code>'A'</code>&nbsp;块(左)和一个&nbsp;<code>'B'</code>&nbsp;块(右)之上。请注意，这与 <code>"BAC"</code>&nbsp;不同，<code>"B"</code>&nbsp;在左下角，<code>"A"</code>&nbsp;在右下角。</li>
</ul>

<p>你从作为单个字符串给出的底部的一排积木&nbsp;<code>bottom</code>&nbsp;开始，<strong>必须</strong>&nbsp;将其作为金字塔的底部。</p>

<p>在给定&nbsp;<code>bottom</code>&nbsp;和&nbsp;<code>allowed</code>&nbsp;的情况下，如果你能一直构建到金字塔顶部，使金字塔中的 <strong>每个三角形图案</strong> 都是在&nbsp;<code>allowed</code>&nbsp;中的，则返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/08/26/pyramid1-grid.jpg" style="height: 232px; width: 600px;" /></p>

<pre>
<strong>输入：</strong>bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
<strong>输出：</strong>true
<strong>解释：</strong>允许的三角形图案显示在右边。
从最底层(第 3 层)开始，我们可以在第 2 层构建“CE”，然后在第 1 层构建“E”。
金字塔中有三种三角形图案，分别是 “BCC”、“CDE” 和 “CEA”。都是允许的。
</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/08/26/pyramid2-grid.jpg" style="height: 359px; width: 600px;" /></p>

<pre>
<strong>输入：</strong>bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
<strong>输出：</strong>false
<strong>解释：</strong>允许的三角形图案显示在右边。
从最底层(即第 4 层)开始，创造第 3 层有多种方法，但如果尝试所有可能性，你便会在创造第 1 层前陷入困境。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= bottom.length &lt;= 6</code></li>
	<li><code>0 &lt;= allowed.length &lt;= 216</code></li>
	<li><code>allowed[i].length == 3</code></li>
	<li>所有输入字符串中的字母来自集合&nbsp;<code>{'A', 'B', 'C', 'D', 'E', 'F'}</code>。</li>
	<li>&nbsp;<code>allowed</code>&nbsp;中所有值都是 <strong>唯一的</strong></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 深度优先搜索
- 广度优先搜索

## 示例

```
"BCD"
["BCC","CDE","CEA","FFF"]
"AAAA"
["AAB","AAC","BCD","BBE","DEF"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean pyramidTransition(String bottom, List<String> allowed) {
        
    }
}
```

### Python

```python
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
```

### C

```c
bool pyramidTransition(char* bottom, char** allowed, int allowedSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool PyramidTransition(string bottom, IList<string> allowed) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} bottom
 * @param {string[]} allowed
 * @return {boolean}
 */
var pyramidTransition = function(bottom, allowed) {
    
};
```

### TypeScript

```typescript
function pyramidTransition(bottom: string, allowed: string[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $bottom
     * @param String[] $allowed
     * @return Boolean
     */
    function pyramidTransition($bottom, $allowed) {
        
    }
}
```

### Swift

```swift
class Solution {
    func pyramidTransition(_ bottom: String, _ allowed: [String]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun pyramidTransition(bottom: String, allowed: List<String>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool pyramidTransition(String bottom, List<String> allowed) {
    
  }
}
```

### Go

```golang
func pyramidTransition(bottom string, allowed []string) bool {
    
}
```

### Ruby

```ruby
# @param {String} bottom
# @param {String[]} allowed
# @return {Boolean}
def pyramid_transition(bottom, allowed)
    
end
```

### Scala

```scala
object Solution {
    def pyramidTransition(bottom: String, allowed: List[String]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn pyramid_transition(bottom: String, allowed: Vec<String>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (pyramid-transition bottom allowed)
  (-> string? (listof string?) boolean?)
  )
```

### Erlang

```erlang
-spec pyramid_transition(Bottom :: unicode:unicode_binary(), Allowed :: [unicode:unicode_binary()]) -> boolean().
pyramid_transition(Bottom, Allowed) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec pyramid_transition(bottom :: String.t, allowed :: [String.t]) :: boolean
  def pyramid_transition(bottom, allowed) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func pyramidTransition(bottom: String, allowed: ArrayList<String>): Bool {

    }
}
```

