# 816. 模糊坐标

## 题目描述

<p>我们有一些二维坐标，如&nbsp;<code>&quot;(1, 3)&quot;</code>&nbsp;或&nbsp;<code>&quot;(2, 0.5)&quot;</code>，然后我们移除所有逗号，小数点和空格，得到一个字符串<code>S</code>。返回所有可能的原始字符串到一个列表中。</p>

<p>原始的坐标表示法不会存在多余的零，所以不会出现类似于&quot;00&quot;, &quot;0.0&quot;, &quot;0.00&quot;, &quot;1.0&quot;, &quot;001&quot;, &quot;00.01&quot;或一些其他更小的数来表示坐标。此外，一个小数点前至少存在一个数，所以也不会出现&ldquo;.1&rdquo;形式的数字。</p>

<p>最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。</p>

<p>&nbsp;</p>

<pre>
<strong>示例 1:</strong>
<strong>输入:</strong> &quot;(123)&quot;
<strong>输出:</strong> [&quot;(1, 23)&quot;, &quot;(12, 3)&quot;, &quot;(1.2, 3)&quot;, &quot;(1, 2.3)&quot;]
</pre>

<pre>
<strong>示例 2:</strong>
<strong>输入:</strong> &quot;(00011)&quot;
<strong>输出:</strong> &nbsp;[&quot;(0.001, 1)&quot;, &quot;(0, 0.011)&quot;]
<strong>解释:</strong> 
0.0, 00, 0001 或 00.01 是不被允许的。
</pre>

<pre>
<strong>示例 3:</strong>
<strong>输入:</strong> &quot;(0123)&quot;
<strong>输出:</strong> [&quot;(0, 123)&quot;, &quot;(0, 12.3)&quot;, &quot;(0, 1.23)&quot;, &quot;(0.1, 23)&quot;, &quot;(0.1, 2.3)&quot;, &quot;(0.12, 3)&quot;]
</pre>

<pre>
<strong>示例 4:</strong>
<strong>输入:</strong> &quot;(100)&quot;
<strong>输出:</strong> [(10, 0)]
<strong>解释:</strong> 
1.0 是不被允许的。
</pre>

<p>&nbsp;</p>

<p><strong>提示: </strong></p>

<ul>
	<li><code>4 &lt;= S.length &lt;= 12</code>.</li>
	<li><code>S[0]</code> = &quot;(&quot;, <code>S[S.length - 1]</code> = &quot;)&quot;, 且字符串&nbsp;<code>S</code>&nbsp;中的其他元素都是数字。</li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 字符串
- 回溯
- 枚举

## 示例

```
"(123)"
"(0123)"
"(00011)"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> ambiguousCoordinates(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> ambiguousCoordinates(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** ambiguousCoordinates(char* s, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> AmbiguousCoordinates(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var ambiguousCoordinates = function(s) {
    
};
```

### TypeScript

```typescript
function ambiguousCoordinates(s: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function ambiguousCoordinates($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func ambiguousCoordinates(_ s: String) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun ambiguousCoordinates(s: String): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> ambiguousCoordinates(String s) {
    
  }
}
```

### Go

```golang
func ambiguousCoordinates(s string) []string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String[]}
def ambiguous_coordinates(s)
    
end
```

### Scala

```scala
object Solution {
    def ambiguousCoordinates(s: String): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ambiguous_coordinates(s: String) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (ambiguous-coordinates s)
  (-> string? (listof string?))
  )
```

### Erlang

```erlang
-spec ambiguous_coordinates(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
ambiguous_coordinates(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ambiguous_coordinates(s :: String.t) :: [String.t]
  def ambiguous_coordinates(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func ambiguousCoordinates(s: String): ArrayList<String> {

    }
}
```

